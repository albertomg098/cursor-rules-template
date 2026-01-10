class SubclassLabelNotDefined(Exception):
    """Raised when a subclass does not define its label property."""


class SubclassesLocationsNotDefined(Exception):
    """Raised when a registry class does not define its subclasses_locations property."""


class UnexpectedError(Exception):
    """Raised when an unexpected error occurs during registry operations."""


class RegistryAutoPopulationError(Exception):
    """Raised when the BaseRegistry fails to automatically populate the registry."""
