# Generate Hexagonal Python Skills and Commands

Quick-start command for Python hexagonal architecture (FastAPI + optional Airflow). Generates both skills (rules) and commands.

## Interview - Ask Detailed Questions

Ask ONE question at a time. If answers are unclear, ask follow-up questions.

### Project Basics

1. **Project name?** 
   - If unclear, ask: "What's the service name or repository name? (e.g., 'payment-service', 'user-auth-api')"

2. **Project purpose?**
   - Ask: "What does this service do? What's its main responsibility?"
   - If vague, ask: "What problem does it solve? Who uses it?"

3. **Main domain entities?**
   - Ask: "What are the core business entities? (e.g., Payment, Transaction, Refund, User, Order)"
   - If unclear, ask: "What are the main things this system manages? List 3-5 core entities."
   - Follow-up: "Can you describe what each entity represents?"

### External Services - Be Specific

4. **Database?**
   - Ask: "What database? (PostgreSQL, MySQL, MongoDB, Supabase, SQLite)"
   - Follow-up: "Are you using an ORM? (SQLAlchemy, Tortoise, Prisma, raw SQL)"
   - Ask: "How do you handle migrations? (Alembic, Django migrations, manual)"

5. **Authentication?**
   - Ask: "How do you handle authentication? (Clerk, Auth0, custom JWT, OAuth, none)"
   - If custom, ask: "What authentication flow? (JWT tokens, session-based, API keys)"

6. **Other external services?**
   - Ask: "What other external services do you integrate with?"
   - Break down:
     - **Storage:** "File storage? (S3, Cloud Storage, local filesystem, none)"
     - **APIs:** "Do you call external APIs? Which ones? (Stripe, SendGrid, etc.)"
     - **Message queues:** "Message queues? (RabbitMQ, Kafka, SQS, Redis pub/sub, none)"
     - **Cache:** "Caching? (Redis, Memcached, in-memory, none)"

7. **Has Airflow/Orchestration?**
   - Ask: "Do you use Airflow or other orchestration for scheduled tasks or workflows? (yes/no)"
   - If yes, ask: "Which orchestration framework? (Airflow, Prefect, etc.)"
   - Ask: "What do your workflows do? (data processing, ETL, scheduled jobs)"
   - Follow-up: "How often do they run? (daily, hourly, on-demand)"
   - Note: Orchestration goes in `orchestration/<framework>/` at root level, uses DockerOperator to pull image and trigger CLI app

### Development Practices

8. **Testing?**
   - Ask: "What testing framework? (pytest, unittest, none)"
   - Follow-up: "What's your test coverage target? (80%, 90%, not specified)"
   - Ask: "Do you use test fixtures? Mocking libraries? (pytest fixtures, unittest.mock)"
   - Note: Test structure mirrors src/ with e2e/, integration/, unit/ folders. Mocks live in conftest. Use fixtures and initialization pattern.

9. **Code quality?**
   - Ask: "Do you use linters/formatters? (Black, Ruff, mypy, pylint)"
   - Follow-up: "Any pre-commit hooks?"
   - Note: Type hints always required, numpy-style and English docstrings

10. **CI/CD?**
    - Ask: "Do you have CI/CD? (GitHub Actions, GitLab CI, Jenkins, none)"
    - If yes, ask: "What does your pipeline do? (run tests, lint, deploy)"

### Architectural Patterns (Confirm/Clarify)

12. **Use case structure?**
    - Confirm: "You'll use `use_cases/` OR `pipelines/` (not both), correct?"
    - Ask: "Should I create a `BaseUseCase` abstract class with common functionality (logging, error handling, validation, DI)?"
    - Follow-up: "What should BaseUseCase include? (abstract methods, common initialization, etc.)"

13. **FastAPI structure?**
    - Confirm: "FastAPI should be encapsulated in a class in `main.py`, with `self.app = FastAPI(...)` in `__init__`, correct?"
    - Ask: "How should routes be organized? (by domain/entity, by feature, flat structure?)"
    - Confirm: "Manual dependency injection - initialize stateless components in FastAPI class `__init__`, correct?"
    - Ask: "Where should response schemas live? (`infrastructure/inbound_adapters/api/schemas/`)"

14. **CLI structure?**
    - Confirm: "CLI should use Typer, encapsulated in a class, correct?"
    - Ask: "Should there be a router script that routes to use_cases, or should CLI commands directly call use cases?"
    - Confirm: "Manual dependency injection similar to FastAPI, correct?"

15. **Error handling and logging?**
    - Ask: "How should domain exceptions be mapped to HTTP responses? (global exception handlers?)"
    - Ask: "Should logging be centralized in a class or file? Where?"
    - Confirm: "All exceptions registered in domain layer, correct?"

### Commands to Generate

16. **What commands would be useful?**
    - Ask: "What repetitive tasks do you do? (e.g., 'create use case', 'add new entity', 'generate migration', 'run tests')"
    - Ask: "What commands would speed up your workflow?"
    - Suggest: "Common commands might be: '/create-use-case', '/add-entity', '/create-adapter', '/generate-migration'"
    - For each command, ask: "What should `/command-name` do? What should it ask?"

## Generate Structure

Create this structure:
```
orchestration/              # Orchestration frameworks (at root level, not in src/)
└── airflow/                # Airflow DAGs using DockerOperator

src/
├── domain/
│   ├── entities/           # Pydantic models with business logic
│   ├── value_objects/      # Immutable value objects (Pydantic or class methods)
│   ├── ports/              # Interfaces (ABC classes, not Protocol)
│   ├── exceptions/       # Custom exception hierarchy (folder, not file)
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

Create skills in `.cursor/skills/<name>/SKILL.md` format. Skills should be context-dependent: decide whether to apply always, auto-attach based on file patterns, or make manual.

### Always-On Skills
- `.cursor/skills/000-project-core/SKILL.md` - Architecture overview, dependency direction (domain ← application ← infrastructure for outbound, inbound can use application), SOLID/DRY/KISS principles, class initialization patterns
- `.cursor/skills/010-python-standards/SKILL.md` - Type hints always required, numpy-style and English docstrings, pylint, async/await patterns

### Auto-Attach Skills (based on file patterns)
- `.cursor/skills/100-domain-layer/SKILL.md` (glob: `src/domain/**`) - Pure business logic, NO external imports, ABC-based ports (not Protocol), Pydantic entities with business logic, immutable value objects, custom exception hierarchy
- `.cursor/skills/110-application-layer/SKILL.md` (glob: `src/application/**`) - BaseUseCase abstract class pattern, use case classes (one per use case OR pipelines, not both), components (main app logic), resources (utils), schemas (Pydantic)
- `.cursor/skills/120-infrastructure/SKILL.md` (glob: `src/infrastructure/**`) - Adapter implementation patterns, manual dependency injection
- `.cursor/skills/121-fastapi/SKILL.md` (glob: `src/infrastructure/inbound_adapters/api/**`) - FastAPI class encapsulation, route organization, middleware patterns, manual DI, error handling, response schemas
- `.cursor/skills/122-cli/SKILL.md` (glob: `src/infrastructure/inbound_adapters/cli/**`) - Typer app class encapsulation, CLI routing pattern, manual DI
- `.cursor/skills/123-adapters/SKILL.md` (glob: `src/infrastructure/outbound_adapters/**`) - One file per provider pattern, adapter patterns for external services
- `.cursor/skills/130-interfaces/SKILL.md` (glob: `src/interfaces/**`) - Entrypoint patterns (API/CLI main), NOT DTOs
- `.cursor/skills/200-testing/SKILL.md` (glob: `tests/**`) - Test structure (e2e/integration/unit mirroring src/), hierarchical conftest, mocking patterns (fixtures, initialization pattern, mocks in conftest), 80% coverage minimum
- `.cursor/skills/300-orchestration/SKILL.md` (glob: `orchestration/**`) - Orchestration patterns (DockerOperator, CLI triggering)
- `.cursor/skills/400-config/SKILL.md` (glob: `**/config/**/*.yaml`) - YAML structure, environment-specific configs, environment folder for infra connections

### Manual Skills
- `.cursor/skills/900-new-feature/SKILL.md` - Workflow: create port (ABC) → implement use case (BaseUseCase) → create adapter → add tests → update docs
- `.cursor/skills/901-update-docs/SKILL.md` - Checklist: README, API docs, tests, changelog

## Generate Commands

Based on Q11, create commands in `.cursor/commands/<name>.md` format.

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

## Skill Content Requirements

Each skill MUST:
- Use MY actual project name and entities in examples
- Include real code examples (not pseudo-code)
- Show DO/DON'T patterns
- Explain WHY (dependency direction, testability, maintainability, SOLID/DRY/KISS)
- Reference actual libraries I'm using (FastAPI, Pydantic, Typer, pytest, etc.)
- Emphasize key patterns:
  - ABC classes for ports (not Protocol)
  - Pydantic models for entities
  - BaseUseCase abstract class pattern
  - FastAPI/Typer class encapsulation
  - Manual dependency injection
  - Class initialization in constructor with optional params for mocking
  - Centralized logging (class or file)
  - Custom exception hierarchy in domain layer
  - Test structure: e2e/integration/unit mirroring src/

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
4. **FastAPI**: Encapsulated in class, `self.app = FastAPI(...)` in `__init__`. Manual DI for components.
5. **CLI**: Typer encapsulated in class. Manual DI. Optional router script to use_cases.
6. **Exceptions**: Custom hierarchy in `domain/exceptions/` (folder, not file).
7. **Logging**: Centralized in class or file.
8. **Testing**: Structure mirrors src/ with e2e/, integration/, unit/. Mocks in conftest.
9. **Dependency Direction**: Domain ← Application ← Infrastructure (outbound). Inbound can use application.
10. **Class Initialization**: Initialize in constructor, optional params for mocking.

Start with question #1.
