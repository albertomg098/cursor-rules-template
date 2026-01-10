import importlib
import os
import pathlib
from abc import ABC
from enum import Enum
import threading
from typing import ClassVar, List, Type, TypeVar, Generic, Optional, Any

# NOTE: When copying to your project, update this import path to match your project structure
# Example: from your_project.domain.exceptions.registry import (
#     RegistryAutoPopulationError,
#     SubclassesLocationsNotDefined,
#     SubclassLabelNotDefined,
# )
# For now, using relative import for reference implementation:
from .exceptions import (
    RegistryAutoPopulationError,
    SubclassesLocationsNotDefined,
    SubclassLabelNotDefined,
)

T = TypeVar('T', bound='BaseRegistry')


class RegistryDict(dict):
    """
    Class to extend the built-in dict type so it displays available keys in case of a KeyError
    It is used as the `registry` property in the BaseRegistry implementations
    """

    def __init__(self, owner_class_name: str):
        """
        Constructor method

        Parameters
        ----------
        owner_class_name: str
            Name of the parent class which contains an instance of RegistryDict
        """
        self.owner_class_name = owner_class_name
        super().__init__()

    def __getitem__(self, label: str):
        """
        Extend the dict's built-in `__getitem__` to it informs the user of the available labels, or
        keys, in the registry's dictionary in case of a KeyError

        Parameters
        ----------
        label: str
            Label or key that is being retreived from the registry's dictionary
        """
        try:
            return super().__getitem__(label)
        except KeyError as e:
            raise KeyError(
                f"Label '{label}' not found in registry of class `{self.owner_class_name}`. "
                f"Available labels are: {list(self.keys())}"
            ) from e


class ClassProperty(Generic[T]):
    """
    Descriptor that allows accessing a class method as a property.
    
    This enables the syntax `Class.registry[key]` instead of `Class.registry()[key]`
    while maintaining lazy loading functionality.
    """

    def __init__(self, func_name: str):
        """
        Initialize the descriptor.

        Parameters
        ----------
        func_name
            The name of the classmethod that should be accessible as a property.
        """
        self.func_name = func_name
        self.owner: Optional[Type[T]] = None
        self.name: Optional[str] = None

    def __set_name__(self, owner: Type[T], name: str) -> None:
        """
        Store the owner class and property name.

        Parameters
        ----------
        owner
            The class that owns this descriptor.
        name
            The name of the property.
        """
        self.owner = owner
        self.name = name

    def __get__(self, instance: Optional[Any], owner: Type[T]) -> RegistryDict:
        """
        Get the property value when accessed from a class.

        Parameters
        ----------
        instance
            The instance (not used for class properties).
        owner
            The class that owns this descriptor.

        Returns
        -------
        RegistryDict
            The registry dictionary for the class.
        """
        # Retrieve the method from the class using the provided function name.
        try:
            method = getattr(owner, self.func_name)
        except AttributeError as e:
            raise AttributeError(
                f"ClassProperty: class '{owner.__name__}' has no method '{self.func_name}'"
            ) from e

        # Ensure the retrieved attribute is actually callable.
        if not callable(method):
            raise TypeError(
                f"ClassProperty: '{self.func_name}' of class '{owner.__name__}' is not callable."
            )

        # Call the method to get the registry dictionary.
        result = method()

        # Verify that the result is a dictionary (to serve as a registry).
        if not isinstance(result, dict):
            raise TypeError(
                f"ClassProperty: method '{self.func_name}' must return a dict-like object, "
                f"got {type(result).__name__}."
            )

        return result


class BaseRegistry(ABC):
    """
    This is an abstract class desgined to effortlessly implement the `Registry Pattern
    Design`. It will add a `registry` property to the class implementing it, which is a
    dictionary mapping its subclasses from `label` to class types.

    Every subclass of a class implementing a BaseRegistry must then have a `label`: str
    property. And the parent class itself must have a `subclasses_locations`: List[str]
    property, which has the project modules containing the subclasses.

    Let's set an example:

    We define an abstract class with some implementations:
    - BaseFurniture(ABC)
      - Table(BaseFurniture)
      - Chair(BaseFurniture)
      - Sofa(BaseFurniture)

    We want to have a dictionary which maps a string to each of the implementations of
    BaseFurniture, and we don't want to worry too much about mantaining this dictionary.

    This dictionary is the `registry`, and it would be best for it to reside inside the
    main abstract class, BaseFurniture.

    For this to happen, with the BaseRegistry class, we just need to adjust our previous
    design to the following:
    - BaseFurniture(BaseRegistry) Has property `subclasses_locations`: List[str]
      - Table(BaseFurniture) Has property `label`: str
      - Chair(BaseFurniture) Has property `label`: str
      - Sofa(BaseFurniture) Has property `label`: str

    The BaseFurniture class will automatically have a property called `registry`
    which will return a dictionary mapping its subclasses.

    Properties:
    - subclasses_locations, List[str]:
        Directory modules to scan for subclasses to add to the main class registry.
        Format: {module}.{submodule}
    - label, str:
        Label which will map a subclass in its parent's registry to its class.

    Idea taken from https://stackoverflow.com/questions/57626912/registry-pattern-with-init-subclass-and-sub-classable-registry  # noqa
    """

    # Type hints for class attributes
    subclasses_locations: ClassVar[List[str]] = []
    label: ClassVar[str] = None
    _registry: ClassVar[RegistryDict]
    _registry_is_populated: ClassVar[bool]
    _registry_lock: ClassVar[threading.Lock] = threading.Lock()

    # Constant defining how many directories is this file below the project's modules root directory
    # The modules root directory is the one containing all importable modules from this project
    DEPTH_FROM_MODULES_ROOT_DIR: ClassVar[int] = 3

    # If all `subclasses_locations` start with the same module name, this variable is useful in
    # order to not type this prefix in all the `subclasses_locations`.
    # E.g. it should be "your_project" if all modules names start with "your_project":
    # `your_project.features`, `your_project.data`, `your_project.models`... and then we may
    # ommit it when defining subclasses_locations.
    # Otherwise, it should be an empty string
    SUBCLASSES_LOCATIONS_MODULE_PREFIX: ClassVar[str] = ""  # UPDATE THIS for your project

    def __init_subclass__(cls, **kwargs):
        """
        Initialize an implementation of BaseRegistry

        This method is executed when any child of BaseRegistry is imported for the first time
        by another Python module
        """
        super().__init_subclass__(**kwargs)
        parent_class: Type["BaseRegistry"] = cls.__bases__[0]

        cls._assert_subclasses_locations_property_in_subclass()

        # Avoid linting errors when the class is not a subclass of BaseRegistry
        parent_subclasses_locations = getattr(parent_class, "subclasses_locations", None)
        parent_registry = getattr(parent_class, "_registry", {})

        if (
            # Initialize the RegistryDict of the class implementing BaseRegistry
            parent_class.__name__ == "BaseRegistry"
            # Or if there is a sublevel of subclasses, initialize a RegistryDict for it too
            # A class defining a sublevel of subclasses defines again `subclasses_locations`,
            # to indicate where is the sublevel of subclasses. So it differs from the parent's
            or parent_subclasses_locations != cls.subclasses_locations
        ):
            cls._registry = RegistryDict(cls.__name__)
            cls._registry_is_populated = False

            # Add the RegistryDict corresponding to the sublevel of subclasses to the main registry
            if parent_class.__name__ != "BaseRegistry":
                parent_registry[cls.label] = cls._registry
            return

        cls._add_subclass_to_registry(parent_class)

    @classmethod
    def _add_subclass_to_registry(cls, parent_class: Type["BaseRegistry"]):
        """
        Adds the subclass being initialized to its parent's registry

        Parameters
        ----------
        parent_class: Type
            Parent of the subclass being initialized
        """
        try:
            # Add subclass to the registry of the parent implementing BaseRegistry
            parent_class._registry[cls.label] = cls

        except AttributeError as e:
            # If this class does not contain a `label` property, it should be a base class
            # If it is, we can skip it. If not, we should alert the user
            # Otherwise, it cannot be mapped inside the registry
            if not cls.__name__.lower().startswith("base"):
                raise SubclassLabelNotDefined(
                    f"Object `{cls.__name__}` has no attribute `label`: str. "
                    "Subclasses of a class implementing `BaseRegistry` need to "
                    "define a `label` property, which maps them in their parent's "
                    "registry to their class."
                ) from e

    @classmethod
    def _get_registry(cls) -> RegistryDict:
        """
        Gets the registry and initializes it if it is the first time consulting it.

        Returns
        -------
        RegistryDict
            The class registry mapping label strings to class types.
        """
        if cls._registry_is_populated is False:
            # Doble check for eficiency
            with cls._registry_lock:
                if not cls._registry_is_populated:
                    cls._populate_registry()
                    cls._registry_is_populated = True
        return cls._registry

    # Type hint for type checkers - registry is accessible as a subscriptable attribute
    # At runtime, this is replaced by the ClassProperty descriptor via __init_subclass__
    registry: ClassVar[RegistryDict] = ClassProperty("_get_registry")  # type: ignore[assignment]

    @classmethod
    def get_enum(cls) -> Type[Enum]:
        """
        Returns an Enum based on the keys of the registry.
        """
        registry = cls._get_registry()
        return Enum(
            f"{cls.__name__}Kind",
            {key.upper(): key for key in registry.keys()},
            type=str,
        )

    @classmethod
    def _populate_registry(cls):
        """
        Populates the registry with all of the modules' subclasses
        """
        modules_root_path = str(
            pathlib.Path(__file__).resolve().parents[cls.DEPTH_FROM_MODULES_ROOT_DIR]
        )

        # Traverse the subclasses directories and import classes found. When a subclass is imported,
        # it is added to the registry of the parent implementing BaseRegistry
        for subclasses_location in cls.subclasses_locations:
            subclasses_path = subclasses_location.replace(".", os.sep)
            subclasses_full_path = os.path.join(
                modules_root_path,
                cls.SUBCLASSES_LOCATIONS_MODULE_PREFIX,
                subclasses_path,
            )

            cls._import_subclass_modules(
                subclasses_full_path=subclasses_full_path,
                subclasses_location=subclasses_location,
                modules_root_path=modules_root_path,
            )

    @classmethod
    def _assert_subclasses_locations_property_in_subclass(cls):
        "Asserts subclasses_locations class property is assigned in class implementing BaseRegistry"
        try:
            cls.subclasses_locations

        except AttributeError as e:
            raise SubclassesLocationsNotDefined(
                f"Object `{cls.__name__}` has no attribute `subclasses_locations`: "
                "List[str]. Implementations of class `BaseRegistry` need to define a "
                "`subclasses_locations` property, which defines the directory modules "
                "to scan for subclasses."
            ) from e

    @classmethod
    def _import_subclass_modules(
        cls,
        subclasses_full_path: str,
        subclasses_location: str,
        modules_root_path: str,
    ):
        """
        Traverses through all the files found in the subclasses_location full path, importing
        the valid modules found, so the classes inside them are added to the registry

        Parameters
        ----------
        subclasses_full_path: str
            Full path to the subclasses location
        subclasses_location: str
            Subclass location as passed in the property of the class implementing BaseRegistry
        modules_root_path: str
            Full path to the modules root directory i.e. the directory containing every importable
            module from this project
        """
        directory_and_files = list(os.walk(subclasses_full_path))

        if len(directory_and_files) == 0:
            raise RegistryAutoPopulationError(
                "BaseRegistry: Could not automatically populate the `registry` "
                f"for class `{cls.__name__}` in location `{subclasses_location}`. "
                f"No files were found. Looked in path: {subclasses_full_path} using "
                f"{modules_root_path} as the modules root path. Check BaseRegistry's "
                "`DEPTH_FROM_MODULES_ROOT_DIR` constant, currently: "
                f"{cls.DEPTH_FROM_MODULES_ROOT_DIR}. Another constant to check is "
                f"`SUBCLASSES_LOCATIONS_MODULE_PREFIX`, currently: "
                f"{cls.SUBCLASSES_LOCATIONS_MODULE_PREFIX}."
            )

        for current_directory, _, files_in_directory in directory_and_files:
            if current_directory.endswith("__pycache__"):
                continue

            for file in files_in_directory:
                if not file.endswith(".py") or file.startswith("_"):
                    continue

                module_name = file[: -len(".py")]
                full_module_name = cls._get_full_module_name(
                    current_directory=current_directory,
                    modules_root_path=modules_root_path,
                    module_name=module_name,
                )
                importlib.import_module(full_module_name)

    @staticmethod
    def _get_full_module_name(
        current_directory: str,
        modules_root_path: str,
        module_name: str,
    ) -> str:
        """
        Gets the full module name, including the submodule location,
        which is passed throughthe current directory

        Parameters
        ----------
        current_directory: str
            Full path to the current directory being explored
        modules_root_path: str
            Full path to the modules root directory i.e. the directory containing every importable
            module from this project
        module_name: str,
            Name of the current module i.e. the current file

        Returns
        ----------
        str
            Full module name
        """
        module_location = current_directory[len(modules_root_path) + 1 :].replace(os.sep, ".")
        return f"{module_location}.{module_name}"
