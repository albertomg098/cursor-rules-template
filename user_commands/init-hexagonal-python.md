# Generate Hexagonal Python Skills and Commands

Quick-start command for Python hexagonal architecture (FastAPI + optional Airflow). Generates both skills (rules) and commands.

## Interview - Ask Detailed Questions

Ask ONE question at a time. If answers are unclear, ask follow-up questions.

### Project Basics

1. **Question 1/15:** 📦 Project name? 
   - If unclear, ask: "What's the service name or repository name? (e.g., 'payment-service', 'user-auth-api')"

2. **Question 2/15:** 🎯 Project purpose?
   - Ask: "What does this service do? What's its main responsibility?"
   - If vague, ask: "What problem does it solve? Who uses it?"

3. **Question 3/15:** 🏗️ Main domain entities?
   - Ask: "What are the core business entities? (e.g., Payment, Transaction, Refund, User, Order)"
   - If unclear, ask: "What are the main things this system manages? List 3-5 core entities."
   - Follow-up: "Can you describe what each entity represents?"

### External Services - Be Specific

4. **Question 4/15:** 🛠️ Database?
   - Ask: "What database? (PostgreSQL, MySQL, MongoDB, Supabase, SQLite)"
   - Follow-up: "Are you using an ORM? (SQLAlchemy, Tortoise, Prisma, raw SQL)"
   - Ask: "How do you handle migrations? (Alembic, Django migrations, manual)"

5. **Question 5/15:** 🛠️ Authentication?
   - Ask: "How do you handle authentication? (Clerk, Auth0, custom JWT, OAuth, none)"
   - If custom, ask: "What authentication flow? (JWT tokens, session-based, API keys)"

6. **Question 6/15:** 📦 Other external services?
   - Ask: "What other external services do you integrate with?"
   - Break down:
     - **Storage:** "File storage? (S3, Cloud Storage, local filesystem, none)"
     - **APIs:** "Do you call external APIs? Which ones? (Stripe, SendGrid, etc.)"
     - **Message queues:** "Message queues? (RabbitMQ, Kafka, SQS, Redis pub/sub, none)"
     - **Cache:** "Caching? (Redis, Memcached, in-memory, none)"

7. **Question 7/15:** 🚀 Has Airflow/Orchestration?
   - Ask: "Do you use Airflow or other orchestration for scheduled tasks or workflows? (yes/no)"
   - If yes, ask: "Which orchestration framework? (Airflow, Prefect, etc.)"
   - Ask: "What do your workflows do? (data processing, ETL, scheduled jobs)"
   - Follow-up: "How often do they run? (daily, hourly, on-demand)"
   - Note: Orchestration goes in `orchestration/<framework>/` at root level, uses DockerOperator to pull image and trigger CLI app

### Development Practices

8. **Question 8/15:** 🧪 Testing?
   - Ask: "What testing framework? (pytest, unittest, none)"
   - Follow-up: "What's your test coverage target? (80%, 90%, not specified)"
   - Ask: "Do you use test fixtures? Mocking libraries? (pytest fixtures, unittest.mock)"
   - Note: Test structure mirrors src/ with e2e/, integration/, unit/ folders. Mocks live in conftest. Use fixtures and initialization pattern.

9. **Question 9/15:** ✅ Code quality?
   - Ask: "Do you use linters/formatters? (Black, Ruff, mypy, pylint)"
   - Follow-up: "Any pre-commit hooks?"
   - Note: Type hints always required, numpy-style and English docstrings

10. **Question 10/15:** ⚙️ CI/CD?
    - Ask: "Do you have CI/CD? (GitHub Actions, GitLab CI, Jenkins, none)"
    - If yes, ask: "What does your pipeline do? (run tests, lint, deploy)"

### Architectural Patterns (Confirm/Clarify)

11. **Question 11/15:** 🎨 Use case structure?
    - Confirm: "You'll use `use_cases/` OR `pipelines/` (not both), correct?"
    - Ask: "Should I create a `BaseUseCase` abstract class with common functionality (logging, error handling, validation, DI)?"
    - Follow-up: "What should BaseUseCase include? (abstract methods, common initialization, etc.)"

12. **Question 12/15:** 🎨 FastAPI structure?
    - Confirm: "FastAPI should be encapsulated in a class in `main.py`, with `self.app = FastAPI(...)` in `__init__`, correct?"
    - Ask: "How should routes be organized? (by domain/entity, by feature, flat structure?)"
    - Confirm: "Manual dependency injection - initialize stateless components in FastAPI class `__init__`, correct?"
    - Ask: "Where should response schemas live? (`infrastructure/inbound_adapters/api/schemas/`)"

13. **Question 13/15:** 🎨 CLI structure?
    - Confirm: "CLI should use Typer, encapsulated in a class, correct?"
    - Ask: "Should there be a router script that routes to use_cases, or should CLI commands directly call use cases?"
    - Confirm: "Manual dependency injection similar to FastAPI, correct?"

14. **Question 14/15:** ✅ Error handling and logging?
    - Ask: "How should domain exceptions be mapped to HTTP responses? (global exception handlers?)"
    - Ask: "Should logging be centralized in a class or file? Where?"
    - Confirm: "All exceptions registered in domain layer, correct?"

### Commands to Generate

15. **Question 15/15:** 🚀 What commands would be useful?
    - Ask: "What repetitive tasks do you do? (e.g., 'create use case', 'add new entity', 'generate migration', 'run tests')"
    - Ask: "What commands would speed up your workflow?"
    - Suggest: "Common commands might be: '/create-use-case', '/add-entity', '/create-adapter', '/generate-migration'"
    - For each command, ask: "What should `/command-name` do? What should it ask?"

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

**CRITICAL - Automatically Generate BaseRegistry:**
- Read `reference/base_registry/base_registry.py` from this template repo
- Read `reference/base_registry/exceptions.py` from this template repo
- Generate `src/domain/value_objects/base_registry.py` with:
  - All BaseRegistry implementation (preserve exactly)
  - Update import: Change `from .exceptions import` to `from {{project_name}}.domain.exceptions.registry import`
  - Adjust `SUBCLASSES_LOCATIONS_MODULE_PREFIX` constant to match project name (or empty string if no prefix)
  - Keep `DEPTH_FROM_MODULES_ROOT_DIR = 3` (or adjust based on project structure)
- Generate `src/domain/exceptions/registry.py` with all registry exceptions (preserve exactly)
- Do this automatically - user should not need to copy-paste anything

Create this structure:
```
orchestration/              # Orchestration frameworks (at root level, not in src/)
└── airflow/                # Airflow DAGs using DockerOperator

src/
├── domain/
│   ├── entities/           # Pydantic models with business logic
│   ├── value_objects/      # Immutable value objects (Pydantic or class methods)
│   │   └── base_registry.py  # BaseRegistry class - AUTO-GENERATED from template repo reference
│   ├── ports/              # Interfaces (ABC classes, not Protocol) - can extend BaseRegistry
│   ├── exceptions/       # Custom exception hierarchy (folder, not file)
│   │   └── registry.py     # Registry exceptions - AUTO-GENERATED from template repo reference
│   ├── dtos/               # Domain DTOs (optional, if needed)
│   └── services/           # Domain services (optional, if applicable)
├── application/
│   ├── use_cases/          # One class per use case OR pipelines/ (not both)
│   │   └── base_use_case.py  # BaseUseCase abstract class
│   ├── components/         # Main application logic classes (initialized and called from use_cases)
│   ├── resources/          # Common utility classes across application layer
│   └── schemas/            # Application Pydantic schemas
├── infrastructure/
│   ├── inbound_adapters/
│   │   ├── api/            # FastAPI application
│   │   │   ├── main.py     # FastAPI class (encapsulated, port in __init__)
│   │   │   ├── routes/     # Route definitions
│   │   │   ├── middleware/ # Auth and dependencies
│   │   │   └── schemas/    # Pydantic response models
│   │   └── cli/            # CLI application (Typer)
│   │       ├── main.py     # Typer app class (encapsulated)
│   │       └── router.py   # Script that routes to use_cases (optional)
│   ├── outbound_adapters/
│   │   ├── database/       # One file per provider (e.g., supabase_database.py)
│   │   ├── auth/           # One file per provider (e.g., clerk_auth.py)
│   │   └── ...             # Other service adapters
│   └── config/
│       ├── environment/    # Connection info for infra components
│       └── *.yaml          # Project-specific YAML configs
├── interfaces/             # Entrypoints (API main, CLI main) - NOT DTOs
└── config/                 # Alternative location for config (if not in infrastructure/config)
    ├── base.yaml
    └── environments/
        ├── dev.yaml
        ├── staging.yaml
        └── prod.yaml

tests/
├── e2e/                    # End-to-end tests (mirror src/ structure)
├── integration/            # Integration tests (mirror src/ structure)
└── unit/                   # Unit tests (mirror src/ structure)
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
- `name` is REQUIRED - use the skill folder name (e.g., "000-project-core")
- `description` is REQUIRED - brief description of what the skill enforces
- `globs` is OPTIONAL - only include if auto-attaching to file patterns (mutually exclusive with `alwaysApply`)
- `alwaysApply` is OPTIONAL - only include if this is an always-on skill (true). Mutually exclusive with `globs`. For manual skills, omit both `globs` and `alwaysApply`.

Skills should be context-dependent: decide whether to apply always, auto-attach based on file patterns, or make manual.

### Always-On Skills
- `.cursor/skills/000-project-core/SKILL.md` - Architecture overview, dependency direction (domain ← application ← infrastructure for outbound, inbound can use application), SOLID/DRY/KISS principles, class initialization patterns, BaseRegistry pattern for avoiding factory pattern
  - Frontmatter: `name: "000-project-core"`, `description: "Architecture overview, dependency direction, SOLID/DRY/KISS principles, class initialization patterns, BaseRegistry pattern"`, `alwaysApply: true`
- `.cursor/skills/010-python-standards/SKILL.md` - Type hints always required, numpy-style and English docstrings, pylint, async/await patterns
  - Frontmatter: `name: "010-python-standards"`, `description: "Type hints always required, numpy-style and English docstrings, pylint, async/await patterns"`, `alwaysApply: true`

### Auto-Attach Skills (based on file patterns)
- `.cursor/skills/100-domain-layer/SKILL.md` (glob: `src/domain/**`) - Pure business logic, NO external imports, ABC-based ports (not Protocol), Pydantic entities with business logic, immutable value objects (including BaseRegistry in value_objects/), custom exception hierarchy, BaseRegistry pattern for automatic subclass discovery and registry pattern
  - Frontmatter: `name: "100-domain-layer"`, `description: "Pure business logic, NO external imports, ABC-based ports, Pydantic entities, immutable value objects (including BaseRegistry), custom exception hierarchy, BaseRegistry pattern"`, `globs: ["src/domain/**"]`
- `.cursor/skills/110-application-layer/SKILL.md` (glob: `src/application/**`) - BaseUseCase abstract class pattern, use case classes (one per use case OR pipelines, not both), components (main app logic), resources (utils), schemas (Pydantic)
  - Frontmatter: `name: "110-application-layer"`, `description: "BaseUseCase abstract class pattern, use case classes, components, resources, schemas"`, `globs: ["src/application/**"]`
- `.cursor/skills/120-infrastructure/SKILL.md` (glob: `src/infrastructure/**`) - Adapter implementation patterns, manual dependency injection
  - Frontmatter: `name: "120-infrastructure"`, `description: "Adapter implementation patterns, manual dependency injection"`, `globs: ["src/infrastructure/**"]`
- `.cursor/skills/121-fastapi/SKILL.md` (glob: `src/infrastructure/inbound_adapters/api/**`) - FastAPI class encapsulation, route organization, middleware patterns, manual DI, error handling, response schemas
  - Frontmatter: `name: "121-fastapi"`, `description: "FastAPI class encapsulation, route organization, middleware patterns, manual DI, error handling, response schemas"`, `globs: ["src/infrastructure/inbound_adapters/api/**"]`
- `.cursor/skills/122-cli/SKILL.md` (glob: `src/infrastructure/inbound_adapters/cli/**`) - Typer app class encapsulation, CLI routing pattern, manual DI
  - Frontmatter: `name: "122-cli"`, `description: "Typer app class encapsulation, CLI routing pattern, manual DI"`, `globs: ["src/infrastructure/inbound_adapters/cli/**"]`
- `.cursor/skills/123-adapters/SKILL.md` (glob: `src/infrastructure/outbound_adapters/**`) - One file per provider pattern, adapter patterns for external services
  - Frontmatter: `name: "123-adapters"`, `description: "One file per provider pattern, adapter patterns for external services"`, `globs: ["src/infrastructure/outbound_adapters/**"]`
- `.cursor/skills/130-interfaces/SKILL.md` (glob: `src/interfaces/**`) - Entrypoint patterns (API/CLI main), NOT DTOs
  - Frontmatter: `name: "130-interfaces"`, `description: "Entrypoint patterns (API/CLI main), NOT DTOs"`, `globs: ["src/interfaces/**"]`
- `.cursor/skills/200-testing/SKILL.md` (glob: `tests/**`) - Test structure (e2e/integration/unit mirroring src/), hierarchical conftest, mocking patterns (fixtures, initialization pattern, mocks in conftest), BaseRegistry testing patterns, 80% coverage minimum
  - Frontmatter: `name: "200-testing"`, `description: "Test structure (e2e/integration/unit mirroring src/), hierarchical conftest, mocking patterns, BaseRegistry testing, 80% coverage minimum"`, `globs: ["tests/**"]`
- `.cursor/skills/300-orchestration/SKILL.md` (glob: `orchestration/**`) - Orchestration patterns (DockerOperator, CLI triggering)
  - Frontmatter: `name: "300-orchestration"`, `description: "Orchestration patterns (DockerOperator, CLI triggering)"`, `globs: ["orchestration/**"]`
- `.cursor/skills/400-config/SKILL.md` (glob: `**/config/**/*.yaml`) - YAML structure, environment-specific configs, environment folder for infra connections
  - Frontmatter: `name: "400-config"`, `description: "YAML structure, environment-specific configs, environment folder for infra connections"`, `globs: ["**/config/**/*.yaml"]`

### Manual Skills
- `.cursor/skills/900-new-feature/SKILL.md` - Workflow: create port (ABC) → implement use case (BaseUseCase) → create adapter → add tests → update docs
  - Frontmatter: `name: "900-new-feature"`, `description: "Workflow: create port (ABC) → implement use case (BaseUseCase) → create adapter → add tests → update docs"` (no globs, no alwaysApply)
- `.cursor/skills/901-update-docs/SKILL.md` - Checklist: README, API docs, tests, changelog
  - Frontmatter: `name: "901-update-docs"`, `description: "Checklist: README, API docs, tests, changelog"` (no globs, no alwaysApply)

## Generate Commands

Based on Q15, create commands in `.cursor/commands/<name>.md` format.

### Common Commands for Hexagonal Python:

If user wants them, generate:

1. **`.cursor/commands/create-use-case.md`**
   - Ask: Entity name, use case name, what it should do
   - Generate: Use case class, port interface, tests

2. **`.cursor/commands/add-entity.md`**
   - Ask: Entity name, attributes, relationships
   - Generate: Entity class, value objects, exceptions, tests

3. **`.cursor/commands/create-adapter.md`**
   - Ask: Adapter type (inbound/outbound), what it adapts, service name
   - Generate: Adapter class implementing port, tests

4. **`.cursor/commands/generate-migration.md`** (if using Alembic)
   - Ask: Migration name, what changes
   - Generate: Migration file with up/down methods

5. **`.cursor/commands/create-api-route.md`**
   - Ask: Route path, HTTP method, use case, request/response schemas
   - Generate: FastAPI route, Pydantic schemas, error handling

6. **`.cursor/commands/create-or-refine-tests.md`** (ALWAYS GENERATE - Essential command)
   - Read `user_commands/create-or-refine-tests-template.md` from this template repo
   - Customize for Hexagonal Python:
     - Replace placeholders with actual project name and entities from interview
     - Emphasize: test use cases in isolation (mock ports/ABC interfaces), test domain entities (immutable, business logic), test adapters separately (mock external services), test error handling and custom exceptions, test FastAPI routes (mock use cases), test CLI commands (mock use cases)
     - **BaseRegistry testing**: Test registry auto-population, label validation, subclasses_locations validation, nested registries, thread safety, error messages, get_enum() method, RegistryDict error messages, and mocking registry access in tests
     - Reference the project's 200-testing skill
   - Generate as `.cursor/commands/create-or-refine-tests.md` in the user's project
   - Ensure it follows: structure mirrors src/, hierarchical conftest.py, initialization strategy for mocking, 80% coverage minimum

7. **`.cursor/commands/create-github-workflow.md`** (OPTIONAL - Only if user wants CI/CD workflows)
   - If user answered "yes" to CI/CD in Q10, ask: "Would you like a command to create GitHub Actions workflows?"
   - If yes, read `user_commands/create-github-workflow-template.md` from this template repo
   - Customize for Hexagonal Python:
     - Update examples with actual project structure
     - Include common steps: pytest, ruff, mypy, docker build (if applicable)
   - Generate as `.cursor/commands/create-github-workflow.md` in the user's project

7. **`.cursor/commands/build-project.md`** (ALWAYS GENERATE - Essential for new projects)
   - Read `user_commands/build-project-template.md` from this template repo
   - Customize for Hexagonal Python:
     - Emphasize: create `src/domain/` with entities, value_objects (including BaseRegistry), exceptions, create `src/application/` with use_cases, create `src/infrastructure/` with inbound_adapters (FastAPI/Typer) and outbound_adapters, create test structure mirroring src/, create BaseRegistry files from reference/base_registry/, create initial domain entities, create configuration files (pyproject.toml, .pylintrc, etc.), create conftest.py files
     - Reference all project skills, especially structure from `000-project-core/SKILL.md`, domain patterns from `100-domain-layer/SKILL.md`, and testing patterns from `200-testing/SKILL.md`
     - Use actual project name and entities in generated files
     - **CRITICAL:** Automatically generate BaseRegistry by reading from `reference/base_registry/` and creating files with correct imports
   - Generate as `.cursor/commands/build-project.md` in the user's project
   - This command uses the project's skills as context to build the complete project structure

8. **`.cursor/commands/review-and-refactor.md`** (ALWAYS GENERATE - Essential for existing projects)
   - Read `user_commands/review-and-refactor-template.md` from this template repo
   - Customize for Hexagonal Python:
     - Emphasize: review dependency direction (domain ← application ← infrastructure), check for domain layer purity (no external imports), verify BaseUseCase pattern usage, check adapter implementations match ports, verify exception hierarchy, check test structure mirrors src/, ensure BaseRegistry pattern is used correctly
     - Reference all project skills, especially architecture patterns from `000-project-core/SKILL.md`, domain patterns from `100-domain-layer/SKILL.md`, and testing patterns from `200-testing/SKILL.md`
   - Generate as `.cursor/commands/review-and-refactor.md` in the user's project
   - This command uses the project's skills as context to review and refactor existing code

## Skill Content Requirements

### 000-project-core Skill MUST Include:

**CRITICAL - Project Context Section:**
- **Project Name:** {{project_name from Q1}}
- **Project Purpose:** {{project_purpose from Q2}} - What this service does, what problem it solves, who uses it
- **Domain:** {{domain entities from Q3}} - Main business entities and their relationships
- **Tech Stack:** {{from Q4-Q7}} - Database, authentication, external services, orchestration
- **Architecture:** Hexagonal architecture with dependency direction (domain ← application ← infrastructure)

This context helps the AI understand what the project is about and make appropriate suggestions.

### All Skills MUST:
- Use MY actual project name and entities in examples
- Include real code examples (not pseudo-code)
- Show DO/DON'T patterns
- Explain WHY (dependency direction, testability, maintainability, SOLID/DRY/KISS)
- Reference actual libraries I'm using (FastAPI, Pydantic, Typer, pytest, etc.)
- Emphasize key patterns:
  - ABC classes for ports (not Protocol)
  - Pydantic models for entities
  - BaseUseCase abstract class pattern
  - **BaseRegistry pattern** - `BaseRegistry` is a value object in `domain/value_objects/base_registry.py` that provides automatic subclass discovery and registry pattern. **CRITICAL: BaseRegistry is automatically generated when creating the project - read from template repo `reference/base_registry/` and generate files with correct imports and constants adjusted for the project. Preserve all implementation details exactly (RegistryDict, ClassProperty, threading, __init_subclass__, _populate_registry, etc.).** Ports, entities, and use cases/pipelines can extend `BaseRegistry` to automatically register subclasses. This avoids factory pattern and provides easy dependency resolution via `Class.registry[label]`. Subclasses must define `label: str` class variable, and parent classes must define `subclasses_locations: List[str]` class variable pointing to module paths where subclasses live. The AI should automatically use BaseRegistry when generating ports/entities that need multiple implementations - no manual setup required.
  - FastAPI/Typer class encapsulation
  - Manual dependency injection
  - Class initialization in constructor with optional params for mocking
  - Centralized logging (class or file)
  - Custom exception hierarchy in domain layer
  - Test structure: e2e/integration/unit mirroring src/
  - **BaseRegistry testing** - Test registry population, label validation, subclasses_locations validation, nested registries, thread safety, error messages, and mocking registry access in tests

### BaseRegistry Pattern Details (for domain layer skill)

When documenting BaseRegistry in the domain layer skill, include:

**CRITICAL - Auto-Generate BaseRegistry:**
- **Automatically generate BaseRegistry** by reading from this template repo (`reference/base_registry/`) and creating files in the project
- Generate `src/domain/value_objects/base_registry.py` with all implementation preserved exactly
- Generate `src/domain/exceptions/registry.py` with all registry exceptions
- Update import path in generated `base_registry.py`: `from {{project_name}}.domain.exceptions.registry import`
- Adjust `SUBCLASSES_LOCATIONS_MODULE_PREFIX` constant to project name (or empty string)
- Keep `DEPTH_FROM_MODULES_ROOT_DIR = 3` (adjust only if project structure differs)
- Includes: `BaseRegistry` class, `RegistryDict` helper class, `ClassProperty` descriptor
- Includes: Thread-safe lazy loading with `_registry_lock`, `_registry_is_populated` flag
- Includes: `get_enum()` method for generating Enums from registry keys
- Registry exceptions: `SubclassLabelNotDefined`, `SubclassesLocationsNotDefined`, `RegistryAutoPopulationError`, `UnexpectedError`
- User should never need to manually copy or modify BaseRegistry - it's auto-generated

**BaseRegistry is a value object** in `domain/value_objects/base_registry.py` that provides registry functionality. Other classes (ports, entities, use cases) can extend it to get automatic subclass registration.

**DO - Use BaseRegistry for ports with multiple implementations:**
```python
from abc import ABC, abstractmethod
from typing import ClassVar, List
from domain.value_objects.base_registry import BaseRegistry

class Database(BaseRegistry, ABC):
    """Abstract database port extending BaseRegistry for registry pattern."""
    subclasses_locations: ClassVar[List[str]] = ["infrastructure.outbound_adapters.database"]
    
    @abstractmethod
    def execute_query(self, query: str) -> pd.DataFrame:
        """Execute a query."""
        pass

# In infrastructure/outbound_adapters/database/supabase_database.py
class SupabaseDatabase(Database):
    label: ClassVar[str] = "supabase"
    
    def execute_query(self, query: str) -> pd.DataFrame:
        # Implementation
        pass

# Usage in infrastructure/router:
database_class = Database.registry["supabase"]  # Returns SupabaseDatabase class
database = database_class(params, connection_info, context)
```

**DO - Use BaseRegistry for entities with multiple types:**
```python
from pydantic import BaseModel
from typing import ClassVar, List
from domain.value_objects.base_registry import BaseRegistry

class BaseEntity(BaseModel, BaseRegistry):
    """Base entity extending BaseRegistry for registry pattern."""
    subclasses_locations: ClassVar[List[str]] = ["domain.entities"]
    object_id: str
    version: int

class Invoice(BaseEntity):
    label: ClassVar[str] = "invoice"
    amount: float

class Payment(BaseEntity):
    label: ClassVar[str] = "payment"
    invoice_id: str

# Usage:
entity_class = BaseEntity.registry["invoice"]  # Returns Invoice class
entity = entity_class(object_id="123", version=1, amount=100.0)
```

**DON'T - Use factory pattern when BaseRegistry is available:**
```python
# DON'T - Factory pattern
class DatabaseFactory:
    @staticmethod
    def create(provider: str) -> Database:
        if provider == "supabase":
            return SupabaseDatabase(...)
        elif provider == "postgresql":
            return PostgreSQLDatabase(...)
        # Hard to maintain, violates Open/Closed Principle

# DO - Use BaseRegistry instead
database_class = Database.registry[provider]  # Clean, extensible, automatic
```

**WHY BaseRegistry:**
- Avoids factory pattern boilerplate
- Automatic subclass discovery - no manual registration
- Type-safe access via `Class.registry[label]`
- Supports nested registries for complex hierarchies
- Easy to extend - just add new subclass with `label`
- Provides `get_enum()` method for generating Enums from registry keys
- Thread-safe lazy loading with automatic population
- Preserve implementation - it's battle-tested and handles edge cases

**Testing BaseRegistry:**
- Test registry auto-population from `subclasses_locations`
- Test `label` validation (raises `SubclassLabelNotDefined` if missing)
- Test `subclasses_locations` validation (raises `SubclassesLocationsNotDefined` if missing)
- Test nested registries (e.g., `BasePipeline.registry[pipeline][subpipeline]`)
- Test thread safety of registry population
- Test error messages show available labels when key not found
- Test `get_enum()` method generates correct Enum
- Mock registry access in tests: `with patch.object(BaseClass, 'registry', {'label': MockClass}):`
- Test `RegistryDict` shows helpful error messages with available keys

## Command Content Requirements

Each command MUST:
- Be self-contained (works when pasted or accessed via `/`)
- Ask specific questions (don't assume)
- Generate complete, runnable code
- Use MY actual project details (names, entities, structure)
- Include proper imports and error handling
- Follow architectural patterns:
  - ABC classes for ports (not Protocol)
  - Pydantic models for entities
  - BaseUseCase for use cases
  - Class encapsulation for FastAPI/Typer
  - Manual dependency injection
  - Type hints and numpy-style docstrings

## Key Architectural Patterns to Enforce

When generating code, ensure:

1. **Ports**: Use ABC (Abstract Base Classes), not Protocol. Naming: `UserRepository` or `UserRepositoryPort`
2. **Entities**: Pydantic models with business logic methods. Tend to be immutable.
3. **Use Cases**: Inherit from `BaseUseCase`, implement abstract methods. Manual DI via constructor.
4. **BaseRegistry Pattern**: `BaseRegistry` is a value object utility class in `domain/value_objects/base_registry.py` that provides automatic subclass discovery and registry pattern. **CRITICAL: Automatically generate BaseRegistry by reading from this template repo (`reference/base_registry/`) and creating the files with correct imports and constants adjusted for the project. Preserve all implementation details exactly (RegistryDict, ClassProperty, threading, __init_subclass__, _populate_registry, etc.).** This avoids factory pattern and provides easy dependency resolution. When a class needs to support multiple implementations (e.g., `Database` port with `SupabaseDatabase`, `PostgreSQLDatabase`), extend `BaseRegistry`:
   - `BaseRegistry` itself is a value object (lives in `domain/value_objects/`)
   - Parent class (e.g., `Database` port): Extend `BaseRegistry` alongside ABC, define `subclasses_locations: ClassVar[List[str]] = ["infrastructure.outbound_adapters.database"]`
   - Subclasses (e.g., `SupabaseDatabase`): Extend parent, define `label: ClassVar[str] = "supabase"`
   - Access implementations: `Database.registry["supabase"]` returns the `SupabaseDatabase` class
   - Use in adapters/infrastructure: `component_class = PortClass.registry[provider_label]` to get the right implementation
   - Supports nested registries (e.g., `BasePipeline.registry[pipeline_name][subpipeline_name]`)
   - Automatically populates registry on first access by scanning `subclasses_locations` modules
   - Provides `get_enum()` method to generate Enum from registry keys
   - Test BaseRegistry: registry population, label validation, nested registries, thread safety, error messages, get_enum(), mocking registry access
5. **FastAPI**: Encapsulated in class, `self.app = FastAPI(...)` in `__init__`. Manual DI for components.
6. **CLI**: Typer encapsulated in class. Manual DI. Optional router script to use_cases.
7. **Exceptions**: Custom hierarchy in `domain/exceptions/` (folder, not file).
8. **Logging**: Centralized in class or file.
9. **Testing**: Structure mirrors src/ with e2e/, integration/, unit/. Mocks in conftest. Test BaseRegistry: registry population, label validation, nested registries, thread safety, error messages, get_enum(), mocking registry access.
10. **Dependency Direction**: Domain ← Application ← Infrastructure (outbound). Inbound can use application.
11. **Class Initialization**: Initialize in constructor, optional params for mocking.
12. **BaseRegistry Auto-Generation**: When generating the project structure, automatically read `reference/base_registry/base_registry.py` and `reference/base_registry/exceptions.py` from this template repo, generate them in the project with correct imports (`from {{project_name}}.domain.exceptions.registry import`) and adjusted constants (`SUBCLASSES_LOCATIONS_MODULE_PREFIX`). User never needs to manually copy or modify - BaseRegistry is ready to use automatically.

Start with question #1.
