# Build Project Structure

Build the complete project structure and initial files following all project rules defined in `.cursor/skills/`.

**CRITICAL:** This command uses the project's skills (rules) as context. Make sure skills exist before building. If skills don't exist, suggest running `setup-project.md` first.

## Step 1: Load Project Context

**MUST DO FIRST:** Read all skills in `.cursor/skills/` to understand:
- Project architecture and patterns
- Project structure and organization
- Coding standards and conventions
- Domain entities and business logic
- Layer-specific patterns
- Testing requirements
- Error handling patterns
- Configuration requirements

**How to load context:**
1. List all directories in `.cursor/skills/`
2. For each skill directory, read the `SKILL.md` file
3. Extract key information:
   - **Project Context** (from core skill, e.g., `000-project-core/SKILL.md` or `000-package-core/SKILL.md`):
     - Project/package name
     - Project purpose/description
     - Domain/entities
     - Tech stack
     - Architecture pattern
     - Components/modules
   - **Project Structure** (from structure-related skills):
     - Directory layout
     - File organization patterns
     - Layer organization
   - **Coding Standards** (from language standards skills):
     - Type hints requirements
     - Docstring style
     - Code style (Black, Ruff, etc.)
   - **Testing Patterns** (from testing skills):
     - Test structure
     - Testing framework
     - Coverage requirements
   - **Configuration** (from config-related skills):
     - Required config files
     - Environment setup
     - Dependency management

**If skills don't exist:**
- Show: "I don't see any skills in `.cursor/skills/`. To build a project, I need to understand the project structure and rules."
- Ask: "Would you like me to run `setup-project.md` first to generate skills, or do you have an existing project structure I should follow?"
- Wait for answer before proceeding.

## Step 2: Check Current Project State

**Understand what already exists:**

1. **List main directories** in the project root
2. **Check for existing source code:**
   - Does `src/` or main source directory exist?
   - What files/folders are already there?
3. **Check for existing tests:**
   - Does `tests/` or test directory exist?
   - What test files exist?
4. **Check for configuration files:**
   - `pyproject.toml`, `package.json`, `tsconfig.json`, etc.
   - `.gitignore`, `.env.example`, etc.
   - CI/CD configs (`.github/workflows/`, etc.)
5. **Check for documentation:**
   - `README.md`
   - `docs/` directory

**Show user:**
- "Current project state:"
  - Existing directories: [list]
  - Existing source files: [count]
  - Existing test files: [count]
  - Configuration files: [list]

## Step 3: Determine What to Build

**Based on project context from skills, determine:**

1. **What structure needs to be created?**
   - Main source directories (e.g., `src/`, `app/`, `lib/`)
   - Layer directories (e.g., `domain/`, `application/`, `infrastructure/`)
   - Component directories (from project context)
   - Test directories (mirroring source structure)

2. **What initial files are needed?**
   - `__init__.py` files (for Python packages)
   - Entry point files (e.g., `main.py`, `app.py`, `index.ts`)
   - Core domain entities/models
   - Configuration files
   - Test setup files (e.g., `conftest.py`)

3. **What configuration needs to be set up?**
   - Dependency management files (`pyproject.toml`, `requirements.txt`, `package.json`)
   - Code quality configs (`.pylintrc`, `.ruff.toml`, `.eslintrc.json`)
   - Type checking configs (`mypy.ini`, `tsconfig.json`)
   - Environment files (`.env.example`)

**Ask user (if needed):**
- "I'll build the project structure based on your skills. Should I:"
  - `build-all` - Create complete structure with initial files
  - `structure-only` - Create directories only, no initial files
  - `incremental` - Let me choose what to build step by step
  - `custom` - Specify what to build

Wait for answer if asked.

## Step 4: Generate Project Structure

**Create directories following patterns from skills:**

1. **Main source structure:**
   - Create directories as specified in project context
   - Follow layer organization (if applicable)
   - Create component directories (if applicable)
   - Add `__init__.py` files for Python packages

2. **Test structure:**
   - Mirror source structure
   - Create `unit/`, `integration/`, `e2e/` if specified
   - Add `conftest.py` files (hierarchical if needed)

3. **Configuration directories:**
   - Create `docs/` if documentation is required
   - Create `.github/workflows/` if CI/CD is mentioned
   - Create any other required directories

**Important:**
- Follow exact structure from skills (don't invent new patterns)
- Use actual project/package names from context
- Create `__init__.py` files for all Python packages
- Maintain proper directory hierarchy

## Step 5: Generate Initial Files

**Create initial files following project patterns:**

### Core Files

1. **Entry points:**
   - Main entry file (e.g., `main.py`, `app.py`, `index.ts`)
   - Follow patterns from skills
   - Include proper imports
   - Add type hints if required
   - Add docstrings if required

2. **Core domain/entities:**
   - Create initial domain entities/models (if specified in context)
   - Use actual entity names from project context
   - Follow patterns from domain/core skills
   - Include proper type hints
   - Add docstrings with examples (if numpy-style required)

3. **Configuration files:**
   - Create `__init__.py` files with proper exports (if public API)
   - Create config modules following config patterns
   - Add environment variable handling if needed

4. **Exception hierarchy:**
   - Create base exception classes (if specified in skills)
   - Follow exception patterns from skills
   - Create domain-specific exceptions (if entities are known)

### Configuration Files

1. **Dependency management:**
   - `pyproject.toml` (Python) - Include dependencies from tech stack
   - `package.json` (Node.js) - Include dependencies from tech stack
   - `requirements.txt` (if needed) - Pin versions

2. **Code quality:**
   - `.pylintrc` or `.ruff.toml` (Python)
   - `.eslintrc.json` (JavaScript/TypeScript)
   - `mypy.ini` (Python type checking)
   - `tsconfig.json` (TypeScript)

3. **Environment:**
   - `.env.example` - Template with required variables
   - `.gitignore` - Standard ignores + project-specific

4. **Documentation:**
   - `README.md` - Project overview, setup instructions, main entrypoints
   - Follow documentation patterns from skills

### Test Files

1. **Test setup:**
   - `conftest.py` (pytest) - Root-level fixtures
   - Hierarchical `conftest.py` files if needed
   - Test utilities/helpers

2. **Initial tests:**
   - Example test files following test structure
   - Tests for initial entities/models
   - Follow testing patterns from skills

**Important:**
- Use actual project names/entities from context (not placeholders)
- Follow exact patterns from skills (DO/DON'T examples)
- Include proper type hints if required
- Add docstrings if required (with examples if numpy-style)
- Use actual libraries from tech stack
- Follow dependency injection patterns if specified
- Create complete files, never use placeholders like `# ... rest of code`

## Step 6: Verify Structure Against Rules

**Check generated structure against skills:**

1. **Architecture compliance:**
   - Does structure follow architecture pattern? (hexagonal, clean, MVC, etc.)
   - Are dependencies pointing in correct direction?
   - Are layers properly separated?

2. **Pattern compliance:**
   - Do files follow naming conventions?
   - Are `__init__.py` files exporting correctly? (if public API)
   - Are components structured correctly?
   - Is dependency injection implemented correctly?

3. **Code quality:**
   - Are type hints present? (if required)
   - Are docstrings present? (if required)
   - Do examples use actual project names?

4. **Testing:**
   - Does test structure mirror source structure?
   - Are conftest files in correct locations?
   - Do tests follow testing patterns?

**If issues found:**
- List them: "I found these issues: [list]"
- Ask: "Should I fix these now? (yes/no)"
- Fix if yes

## Step 7: Generate Summary

**After building:**

1. **List all created directories:**
   - Show directory tree structure

2. **List all created files:**
   - Group by category (source, tests, config, docs)

3. **Show next steps:**
   - "Next steps:"
     - Install dependencies: `pip install -e .` or `npm install`
     - Run tests: `pytest` or `npm test`
     - Review generated files and customize as needed
     - Add more domain entities/models as needed
     - Follow patterns from `.cursor/skills/` when adding new code

4. **Remind about rules:**
   - "Remember: All code should follow patterns in `.cursor/skills/`"
   - "Use `/review-and-refactor` to check code against rules"
   - "Use `/create-or-refine-tests` to add tests"

## Important Notes

- **Always read skills first** - Don't assume patterns, read them from `.cursor/skills/`
- **Use project context** - Use actual project names, entities, and patterns from skills
- **Follow patterns exactly** - Use DO/DON'T examples from skills
- **Create complete files** - Never use placeholders, create working code
- **Test structure mirrors source** - Follow testing patterns from skills
- **Ask before overwriting** - If files exist, ask before overwriting

## Example Workflow

```
1. Load skills → Understand: hexagonal architecture, Python 3.11+, FastAPI, domain entities: User, Order
2. Check state → Found empty project, only README.md exists
3. Determine → Need to build: src/domain/, src/application/, src/infrastructure/, tests/
4. Generate structure → Created all directories with __init__.py files
5. Generate files → Created User entity, Order entity, main.py, conftest.py, pyproject.toml
6. Verify → Checked against skills, all compliant
7. Summary → Listed 15 directories, 25 files created, next steps provided
```

Start by loading project context from `.cursor/skills/`.
