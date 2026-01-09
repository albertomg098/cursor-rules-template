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

7. **Has Airflow?**
   - Ask: "Do you use Airflow for scheduled tasks or workflows? (yes/no)"
   - If yes, ask: "What do your DAGs do? (data processing, ETL, scheduled jobs)"
   - Follow-up: "How often do they run? (daily, hourly, on-demand)"

### Development Practices

8. **Testing?**
   - Ask: "What testing framework? (pytest, unittest, none)"
   - Follow-up: "What's your test coverage target? (80%, 90%, not specified)"
   - Ask: "Do you use test fixtures? Mocking libraries? (pytest fixtures, unittest.mock)"

9. **Code quality?**
   - Ask: "Do you use linters/formatters? (Black, Ruff, mypy, pylint)"
   - Follow-up: "Any pre-commit hooks?"

10. **CI/CD?**
    - Ask: "Do you have CI/CD? (GitHub Actions, GitLab CI, Jenkins, none)"
    - If yes, ask: "What does your pipeline do? (run tests, lint, deploy)"

### Commands to Generate

11. **What commands would be useful?**
    - Ask: "What repetitive tasks do you do? (e.g., 'create use case', 'add new entity', 'generate migration', 'run tests')"
    - Ask: "What commands would speed up your workflow?"
    - Suggest: "Common commands might be: '/create-use-case', '/add-entity', '/create-adapter', '/generate-migration'"
    - For each command, ask: "What should `/command-name` do? What should it ask?"

## Generate Structure

Create this structure:
```
src/
├── domain/
│   ├── entities/
│   ├── value_objects/
│   ├── ports/              # Interfaces (Protocol classes)
│   ├── services/           # Domain services
│   └── exceptions.py
├── application/
│   ├── use_cases/          # One class per use case
│   ├── pipelines/          # Multi-step workflows (if Airflow)
│   ├── components/         # Reusable building blocks
│   └── resources/          # Shared resources
├── infrastructure/
│   ├── inbound_adapters/
│   │   ├── api/            # FastAPI routes
│   │   └── cli/            # Airflow DAGs, CLI commands (if Airflow)
│   ├── outbound_adapters/
│   │   ├── database/       # Supabase, Postgres implementations
│   │   ├── auth/           # Clerk, Auth0 implementations
│   │   └── ...
│   └── config/             # Config loading, secrets
├── interfaces/             # DTOs, Pydantic schemas
└── config/
    ├── base.yaml
    └── environments/
        ├── dev.yaml
        ├── staging.yaml
        └── prod.yaml
```

## Generate Skills

Create skills in `.cursor/skills/<name>/SKILL.md` format:

### Always-On Skills
- `.cursor/skills/000-project-core/SKILL.md` - Architecture overview, dependency direction (domain ← application ← infrastructure), principles
- `.cursor/skills/010-python-standards/SKILL.md` - Python 3.11+, type hints, `from __future__ import annotations`, import order, async/await

### Auto-Attach Skills
- `.cursor/skills/100-domain-layer/SKILL.md` (glob: `src/domain/**`) - Pure business logic, NO external imports, Protocol-based ports, immutable entities
- `.cursor/skills/110-application-layer/SKILL.md` (glob: `src/application/**`) - Use case classes (one per use case), pipeline patterns
- `.cursor/skills/120-infrastructure/SKILL.md` (glob: `src/infrastructure/**`) - Adapter implementation patterns
- `.cursor/skills/121-fastapi/SKILL.md` (glob: `src/infrastructure/inbound_adapters/api/**`) - Route patterns, dependency injection, error handling
- `.cursor/skills/122-airflow/SKILL.md` (glob: `src/infrastructure/inbound_adapters/cli/**`) - DAG patterns, task wrappers (ONLY if Airflow=yes)
- `.cursor/skills/123-adapters/SKILL.md` (glob: `src/infrastructure/outbound_adapters/**`) - Adapter patterns for external services
- `.cursor/skills/130-interfaces/SKILL.md` (glob: `src/interfaces/**`) - Pydantic schemas, `from_entity` patterns
- `.cursor/skills/200-testing/SKILL.md` (glob: `tests/**`) - Hierarchical conftest, mocking patterns, 80% coverage
- `.cursor/skills/300-terraform/SKILL.md` (glob: `terraform/**`) - IaC patterns (if applicable)
- `.cursor/skills/400-config/SKILL.md` (glob: `config/**/*.yaml`) - YAML structure, environment-specific configs

### Manual Skills
- `.cursor/skills/900-new-feature/SKILL.md` - Workflow: create port → implement use case → create adapter → add tests → update docs
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
- Explain WHY (dependency direction, testability, maintainability)
- Reference actual libraries I'm using (FastAPI, Pydantic, etc.)

## Command Content Requirements

Each command MUST:
- Be self-contained (works when pasted or accessed via `/`)
- Ask specific questions (don't assume)
- Generate complete, runnable code
- Use MY actual project details (names, entities, structure)
- Include proper imports and error handling

Start with question #1.
