# BaseRegistry Reference Implementation

This folder contains the reference implementation of `BaseRegistry` - a value object that provides automatic subclass discovery and registry pattern.

**NOTE: This is a reference for AI commands/skills to read and auto-generate. Users should never need to manually copy these files.**

## Files

- `base_registry.py` - The main BaseRegistry implementation with RegistryDict and ClassProperty
- `exceptions.py` - Registry-specific exceptions

## For AI Commands/Skills

When generating a hexagonal Python project, the AI should:

1. **Read `base_registry.py`** from this reference folder
2. **Read `exceptions.py`** from this reference folder
3. **Generate `src/domain/value_objects/base_registry.py`** with:
   - All implementation preserved exactly
   - Import updated: `from {{project_name}}.domain.exceptions.registry import`
   - `SUBCLASSES_LOCATIONS_MODULE_PREFIX` adjusted to project name (or empty string)
   - `DEPTH_FROM_MODULES_ROOT_DIR` kept as 3 (or adjusted based on project structure)
4. **Generate `src/domain/exceptions/registry.py`** with all exceptions preserved exactly

## Important Notes

- **Preserve all implementation details** - Do not modify core logic
- Only adjust the constants and import paths for the project structure
- This implementation is battle-tested and handles edge cases
- Includes thread-safe lazy loading, nested registries, and helpful error messages
- Users should never need to know about or manually copy BaseRegistry - it's auto-generated
