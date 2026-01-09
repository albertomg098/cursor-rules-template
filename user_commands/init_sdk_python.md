# Generate Python SDK Rules

Quick-start for Python SDK/Library projects with components architecture.

## Interview

Ask ONE at a time:

1. **Package name?** (e.g., "myclient", will be used as `src/myclient/`)

2. **Main components?** (e.g., "auth, api_client, webhooks")

3. **External dependencies?** (list main libraries: requests, httpx, etc.)

## Generate Structure

```
src/
├── {{package_name}}/
│   ├── __init__.py         # Public API exports only
│   ├── client.py           # Main client class
│   ├── config.py           # Configuration
│   ├── exceptions.py       # Exception hierarchy
│   ├── core/               # Core functionality
│   │   ├── base.py         # Base classes
│   │   └── protocols.py    # Interfaces for extensibility
│   ├── components/         # Pluggable components
│   │   ├── __init__.py
│   │   ├── component_a/
│   │   └── component_b/
│   ├── models/             # Data models
│   └── _internal/          # Private implementation
├── tests/
└── docs/
```

## Generate Skills

Create skills in `.cursor/skills/<name>/SKILL.md` format:

### Always-On Skills
- `.cursor/skills/000-package-core/SKILL.md` - SDK design principles: public API = `__init__.py` exports, `_internal/` is private, deprecate before removing (min 1 minor version)
- `.cursor/skills/010-python-standards/SKILL.md` - Python conventions, type hints, annotations

### Auto-Attach Skills
- `.cursor/skills/100-public-api/SKILL.md` (glob: `src/{{package}}/__init__.py`, `src/{{package}}/client.py`) - Export rules, API stability, versioning
- `.cursor/skills/110-core/SKILL.md` (glob: `src/{{package}}/core/**`) - Core patterns, Protocol-based interfaces
- `.cursor/skills/120-components/SKILL.md` (glob: `src/{{package}}/components/**`) - Component structure, ports/adapters for extensibility
- `.cursor/skills/130-models/SKILL.md` (glob: `src/{{package}}/models/**`) - Data models, Pydantic schemas
- `.cursor/skills/140-exceptions/SKILL.md` (glob: `src/{{package}}/exceptions.py`) - Exception hierarchy, custom exceptions
- `.cursor/skills/200-testing/SKILL.md` (glob: `tests/**`) - Testing patterns, mocking external APIs
- `.cursor/skills/300-documentation/SKILL.md` (glob: `docs/**`, `README.md`) - Doc standards, examples in docstrings

### Manual Skills
- `.cursor/skills/900-api-changes/SKILL.md` - Breaking change workflow: deprecation → new version → removal
- `.cursor/skills/901-release/SKILL.md` - Publishing workflow: version bump → changelog → tests → publish

## Key Principles in Skills

- Public API = what's exported from `__init__.py`
- `_internal/` can change without notice
- Components follow ports/adapters for extensibility
- Every public function has docstrings with examples
- Deprecation warnings before breaking changes

Use MY actual package name and components in all examples.

Start with question #1.
