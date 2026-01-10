# Generate Python SDK Rules

Quick-start for Python SDK/Library projects with components architecture.

## Interview

**CRITICAL:** Follow interview standards - ONE question at a time, show progress (X/TOTAL), use emojis, wait for answer before proceeding.

Ask ONE at a time:

### Project Basics

1. **Question 1/8:** 🎯 Package name? (e.g., "myclient", will be used as `src/myclient/`)

2. **Question 2/8:** 🏗️ Main components? (e.g., "client, server, evaluation" - these become top-level folders)

3. **Question 3/8:** 🔌 Optional extensions/plugins? (e.g., "webhooks, middleware" - these go in `extensions/` folder, or "none")

4. **Question 4/8:** 📦 External dependencies? (list main libraries: requests, httpx, pydantic, etc.)

### Development Practices

5. **Question 5/8:** 🧪 Testing framework? (Confirm: pytest, or specify other)
   - Follow-up: "What's your test coverage target?" (Default: 80% minimum)

6. **Question 6/8:** 🔍 Code quality tools? (Confirm: pylint, or specify: Black, Ruff, mypy, etc.)
   - Follow-up: "Any pre-commit hooks?"

7. **Question 7/8:** 📝 Versioning strategy? (Confirm: Semantic versioning via CI/CD or GitHub workflows, or specify other)

8. **Question 8/8:** 📚 Documentation approach? (Confirm: numpy-style docstrings with examples in docstrings, or specify other)

## Check for Existing Files

**CRITICAL:** Before generating any files, you MUST check for existing skills and commands.

1. **Check for existing skills:**
   - List all existing files in `.cursor/skills/` directory (if it exists)
   - For each skill that would be generated, check if it already exists
   - Show user: "I found these existing skills: [list]"

2. **Check for existing commands:**
   - List all existing files in `.cursor/commands/` directory (if it exists)
   - For each command that would be generated, check if it already exists
   - Show user: "I found these existing commands: [list]"

3. **Ask how to handle existing files:**
   - If any existing files are found, ask ONE question:
   
   **"How should I handle existing files?"**
   - `overwrite` - Replace all existing files with new ones
   - `refine` - Update existing files with new information, preserve custom content
   - `skip` - Keep existing files as-is, only create new ones
   - `selective` - Let me choose for each file individually
   
   Wait for answer before proceeding.

4. **If user chose `refine`:**
   - For each existing file:
     - Read the existing file content completely
     - Identify what's custom vs. what's template-generated:
       - Custom content: Examples using actual project names/entities, project-specific patterns, custom rules added by user
       - Template content: Generic examples, standard patterns, boilerplate that should be updated
     - Merge strategy:
       - **Frontmatter:** Update if missing or incorrect, preserve if custom
       - **Project-specific examples:** Always preserve user's actual project details (names, entities, services)
       - **Patterns/rules:** Update with latest best practices, but preserve any custom rules user added
       - **Structure:** Preserve custom sections, add missing standard sections
     - If content conflicts (e.g., different patterns), ask: "I see [conflict]. Should I [option1] or [option2]?"
     - Show diff before writing: "I'll update [filename] with these changes: [summary]"
   - For new files: Generate normally

5. **If user chose `selective`:**
   - For each existing file, ask: "Refine [filename]? (yes/no/skip)"
   - Wait for answer before proceeding to next file
   - Apply chosen action (refine/overwrite/skip) per file

## Generate Structure

```
src/
├── {{package_name}}/
│   ├── __init__.py         # Public API exports only
│   ├── core/               # Domain-like core (always present)
│   │   ├── exceptions/     # Exception hierarchy (folder)
│   │   ├── models/         # Data models (folder)
│   │   ├── config/         # Configuration (folder, or top-level if complex)
│   │   └── base/           # Base classes and ABC interfaces for extensibility
│   ├── {{component_1}}/    # Main component (e.g., client/, server/, evaluation/)
│   │   ├── __init__.py     # Export main classes
│   │   └── ...             # All component-related scripts
│   ├── {{component_2}}/    # Another main component
│   │   ├── __init__.py
│   │   └── ...
│   ├── extensions/         # Optional extensions/plugins (if Q3 answered)
│   │   ├── __init__.py
│   │   └── ...             # Extension modules
│   └── _internal/          # Private implementation (optional)
├── tests/
│   ├── unit/               # Unit tests (mirror src/ structure)
│   ├── integration/        # Integration tests (mirror src/ structure)
│   ├── e2e/                # End-to-end tests (if needed)
│   └── conftest.py         # Root-level conftest (hierarchical conftest.py in subfolders)
└── docs/                   # Documentation
```

## Generate Skills

Create skills in `.cursor/skills/<name>/SKILL.md` format. **CRITICAL:** Each skill file MUST start with frontmatter. Use the appropriate format based on skill type:

**Always-on skill:**
```yaml
---
name: "skill-name"
description: "Description of what this skill enforces"
alwaysApply: true
---
```

**Auto-attach skill:**
```yaml
---
name: "skill-name"
description: "Description of what this skill enforces"
globs: ["pattern/**"]
---
```

**Manual skill:**
```yaml
---
name: "skill-name"
description: "Description of what this skill enforces"
---
```

**Important:** 
- `name` is REQUIRED - use the skill folder name
- `description` is REQUIRED - brief description of what the skill enforces
- `globs` is OPTIONAL - only include if auto-attaching to file patterns (mutually exclusive with `alwaysApply`)
- `alwaysApply` is OPTIONAL - only include if this is an always-on skill (true). Mutually exclusive with `globs`. For manual skills, omit both `globs` and `alwaysApply`.

Skills should be context-dependent: decide whether to apply always, auto-attach based on file patterns, or make manual.

### Always-On Skills
- `.cursor/skills/000-package-core/SKILL.md` - SDK design principles: public API = `__init__.py` exports, component folders with `__init__.py`, `_internal/` is private, deprecate before removing (min 1 minor version), SOLID/DRY/KISS principles, manual dependency injection via constructors
  - Frontmatter: `name: "000-package-core"`, `description: "SDK design principles: public API exports, component structure, deprecation, SOLID/DRY/KISS, manual DI"`, `alwaysApply: true`
- `.cursor/skills/010-python-standards/SKILL.md` - Python conventions, type hints always required, numpy-style docstrings with examples, pylint compliance
  - Frontmatter: `name: "010-python-standards"`, `description: "Python conventions, type hints always required, numpy-style docstrings with examples, pylint compliance"`, `alwaysApply: true`

### Auto-Attach Skills (based on file patterns)
- `.cursor/skills/100-public-api/SKILL.md` (glob: `src/{{package}}/__init__.py`) - Export rules, API stability, versioning, only export from component `__init__.py` files
  - Frontmatter: `name: "100-public-api"`, `description: "Export rules, API stability, versioning, only export from component __init__.py files"`, `globs: ["src/{{package}}/__init__.py"]`
- `.cursor/skills/110-core/SKILL.md` (glob: `src/{{package}}/core/**`) - Core patterns, ABC-based interfaces (not Protocol), domain-like structure, exceptions in `core/exceptions/`, models in `core/models/`, config in `core/config/`, base classes and ABCs in `core/base/`
  - Frontmatter: `name: "110-core"`, `description: "Core patterns, ABC-based interfaces, domain-like structure, exceptions/models/config/base organization"`, `globs: ["src/{{package}}/core/**"]`
- `.cursor/skills/120-{{component}}/SKILL.md` (glob: `src/{{package}}/{{component}}/**`) - Generate ONE skill per component: component structure (folder with `__init__.py` and related scripts), manual DI via constructors, optional params for testing/mocking, stateless classes
  - Frontmatter: `name: "120-{{component}}"`, `description: "Component structure, manual DI via constructors, optional params for testing/mocking, stateless classes"`, `globs: ["src/{{package}}/{{component}}/**"]`
- `.cursor/skills/130-extensions/SKILL.md` (glob: `src/{{package}}/extensions/**`) - Extension/plugin patterns, ABC-based interfaces for extensibility
  - Frontmatter: `name: "130-extensions"`, `description: "Extension/plugin patterns, ABC-based interfaces for extensibility"`, `globs: ["src/{{package}}/extensions/**"]`
- `.cursor/skills/200-testing/SKILL.md` (glob: `tests/**`) - Testing patterns: structure mirrors src/ with unit/, integration/, e2e/, hierarchical conftest.py files, initialization strategy for mocking, mocks in conftest, pytest, 80% coverage minimum
  - Frontmatter: `name: "200-testing"`, `description: "Testing patterns: structure mirrors src/, hierarchical conftest.py, initialization strategy for mocking, pytest, 80% coverage minimum"`, `globs: ["tests/**"]`
- `.cursor/skills/300-documentation/SKILL.md` (glob: `docs/**`, `README.md`) - Documentation standards: numpy-style docstrings with examples, attractive README with setup, main entrypoints, functionalities
  - Frontmatter: `name: "300-documentation"`, `description: "Documentation standards: numpy-style docstrings with examples, attractive README"`, `globs: ["docs/**", "README.md"]`

### Manual Skills
- `.cursor/skills/900-api-changes/SKILL.md` - Breaking change workflow: deprecation → new version → removal
  - Frontmatter: `name: "900-api-changes"`, `description: "Breaking change workflow: deprecation → new version → removal"` (no globs, no alwaysApply)
- `.cursor/skills/901-release/SKILL.md` - Publishing workflow: semantic versioning via CI/CD or GitHub workflows, version bump → changelog → tests → publish
  - Frontmatter: `name: "901-release"`, `description: "Publishing workflow: semantic versioning via CI/CD, version bump → changelog → tests → publish"` (no globs, no alwaysApply)

## Key Principles in Skills

- **Public API** = what's exported from package `__init__.py` and component `__init__.py` files
- **Component structure** = each component is a folder with `__init__.py` and related scripts (no standalone files)
- **Core folder** = domain-like structure with `exceptions/`, `models/`, `config/`, `base/` subfolders
- **Extensibility** = always via ABC (Abstract Base Classes), not Protocol
- **Dependency injection** = manual DI via constructors, optional params for testing/mocking
- **Testing** = structure mirrors src/ with unit/, integration/, e2e/, hierarchical conftest.py, initialization strategy for mocking
- **Documentation** = numpy-style docstrings with examples, attractive README with setup, entrypoints, functionalities
- **Code quality** = type hints always required, pylint, SOLID/DRY/KISS principles
- **Testing coverage** = 80% minimum
- **Versioning** = semantic versioning via CI/CD or GitHub workflows
- `_internal/` can change without notice
- Deprecation warnings before breaking changes (min 1 minor version)

## Skill Content Requirements

### 000-package-core Skill MUST Include:

**CRITICAL - Project Context Section:**
- **Package Name:** {{package_name from Q1}}
- **Package Purpose:** {{from Q2-Q3}} - What this SDK/library does, main components, extensions/plugins
- **Components:** {{components from Q2}} - Main components and their purposes
- **Tech Stack:** {{from Q4}} - External dependencies and libraries
- **Architecture:** SDK/Library structure with public API, components, core, and extensions

This context helps the AI understand what the package is about and make appropriate suggestions.

### All Skills MUST:
- Use MY actual package name and components in examples
- Include real code examples (not pseudo-code)
- Show DO/DON'T patterns
- Explain WHY (testability, maintainability, SOLID/DRY/KISS)
- Reference actual libraries I'm using
- Emphasize key patterns:
  - ABC classes for interfaces (not Protocol)
  - Component folders with `__init__.py`
  - Manual dependency injection
  - Constructor-based initialization with optional params for mocking
  - Hierarchical conftest.py files
  - Numpy-style docstrings with examples
  - Testing structure mirroring src/

Use MY actual package name and components in all examples.

## Generate Commands

**ALWAYS generate this command** (it's essential for maintaining test standards):

**`.cursor/commands/create-or-refine-tests.md`** - Create, extend, or refine tests following project standards.

**To generate:**
1. Read `user_commands/create-or-refine-tests-template.md` from this template repo
2. Customize it for SDK Python:
   - Replace `{{package}}` with actual package name from Q1
   - Update examples to use actual components from Q2
   - Emphasize: test components separately, mock external APIs (requests, httpx), test public API exports from `__init__.py`, test component interactions, test exception hierarchy
   - Reference the project's 200-testing skill
3. Generate as `.cursor/commands/create-or-refine-tests.md` in the user's project
4. Ensure it follows: structure mirrors src/, hierarchical conftest.py, initialization strategy for mocking, 80% coverage minimum

**OPTIONAL command** (only if user wants CI/CD):

**`.cursor/commands/create-github-workflow.md`** - Create GitHub Actions workflows.

**To generate (if user wants it):**
- If user mentioned CI/CD or versioning via GitHub workflows in Q7, ask: "Would you like a command to create GitHub Actions workflows?"
- If yes, read `user_commands/create-github-workflow-template.md` from this template repo
- Customize for SDK Python:
  - Update with actual package name and structure
  - Include common steps: pytest, ruff, mypy, build, publish to PyPI (if applicable)
- Generate as `.cursor/commands/create-github-workflow.md` in the user's project

**ALWAYS generate this command** (essential for new projects):

**`.cursor/commands/build-project.md`** - Build complete project structure and initial files following project rules.

**To generate:**
1. Read `user_commands/build-project-template.md` from this template repo
2. Customize it for SDK Python:
   - Emphasize: create `src/{{package}}/` structure with components, create `core/` with exceptions/models/config/base subfolders, create `extensions/` if applicable, create test structure mirroring src/, create `__init__.py` files with proper exports, create initial domain models, create configuration files (pyproject.toml, .pylintrc, etc.), create conftest.py files
   - Reference all project skills, especially structure from `000-package-core/SKILL.md`, component patterns from component-specific skills, and testing patterns from `200-testing/SKILL.md`
   - Use actual package name and components in generated files
3. Generate as `.cursor/commands/build-project.md` in the user's project
4. This command uses the project's skills as context to build the complete project structure

**ALWAYS generate this command** (essential for existing projects):

**`.cursor/commands/review-and-refactor.md`** - Review and refactor codebase using project rules.

**To generate:**
1. Read `user_commands/review-and-refactor-template.md` from this template repo
2. Customize it for SDK Python:
   - Emphasize: review public API exports (only from `__init__.py`), check component structure (folders with `__init__.py`), verify ABC interfaces (not Protocol), check core organization (exceptions/models/config/base), ensure manual DI via constructors, verify test structure mirrors src/, check documentation standards
   - Reference all project skills, especially SDK design principles from `000-package-core/SKILL.md`, component patterns from component-specific skills, and testing patterns from `200-testing/SKILL.md`
3. Generate as `.cursor/commands/review-and-refactor.md` in the user's project
4. This command uses the project's skills as context to review and refactor existing code

Start with question #1.
