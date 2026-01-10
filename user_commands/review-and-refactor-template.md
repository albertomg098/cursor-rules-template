# Review and Refactor Codebase

Review the existing codebase and suggest/apply refactorings based on the project's rules and patterns defined in `.cursor/skills/`.

**CRITICAL:** This command uses the project's skills (rules) as context. Make sure to read and understand all relevant skills before reviewing code.

## Step 1: Load Project Context

**MUST DO FIRST:** Read all skills in `.cursor/skills/` to understand:
- Project architecture and patterns
- Coding standards and conventions
- Domain entities and business logic
- Layer-specific patterns
- Testing requirements
- Error handling patterns

**How to load context:**
1. List all directories in `.cursor/skills/`
2. For each skill directory, read the `SKILL.md` file
3. Extract key patterns, constraints, and examples from each skill
4. Build a comprehensive understanding of:
   - **Project Context** (from `000-project-core/SKILL.md` - look for "Project Context" section):
     - Project name
     - Project purpose/description (what the repo is about, what problem it solves)
     - Domain/entities
     - Tech stack
     - Architecture pattern
   - Domain entities (from domain layer skills)
   - Architecture patterns (from layer-specific skills)
   - Coding standards (from language standards skills)
   - Testing patterns (from testing skills)

## Step 2: Analyze Codebase Structure

**Understand the current state:**

1. **List main directories** in the project root
2. **Identify source code locations** (e.g., `src/`, `app/`, `lib/`)
3. **Identify test locations** (e.g., `tests/`, `__tests__/`, `spec/`)
4. **Check for configuration files** (e.g., `pyproject.toml`, `package.json`, `tsconfig.json`)
5. **Review project structure** against expected patterns from skills

## Step 3: Review Code Against Rules

**For each major component/module:**

1. **Read the code** in the component
2. **Check against relevant skills:**
   - Which skills apply to this file? (check globs in skill frontmatter)
   - What patterns should this code follow?
   - What are the DO/DON'T examples from the skills?
3. **Identify violations:**
   - Missing type hints (if required by language standards)
   - Incorrect architecture patterns (e.g., domain importing infrastructure)
   - Missing error handling (if required)
   - Incorrect naming conventions
   - Missing docstrings (if required)
   - Not following layer-specific patterns
   - Missing tests (if test coverage is required)

## Step 4: Prioritize Refactorings

**Categorize issues:**

1. **Critical violations** - Architecture violations, dependency direction issues
2. **Pattern violations** - Not following project patterns, incorrect structure
3. **Code quality** - Missing type hints, docstrings, error handling
4. **Testing gaps** - Missing tests, incorrect test structure
5. **Naming/conventions** - Incorrect naming, formatting issues

**Ask user:**
- "I found [X] issues. How would you like to proceed?"
  - `review-only` - Show all issues with explanations, don't make changes
  - `refactor-critical` - Fix critical architecture violations only
  - `refactor-all` - Fix all issues systematically
  - `interactive` - Let me choose which issues to fix

Wait for answer before proceeding.

## Step 5: Apply Refactorings

**If user chose to refactor:**

**For each file to refactor:**

1. **Read the current file** completely
2. **Identify specific violations** against project rules
3. **Show what will change:**
   - "I'll refactor `path/to/file.py` to:"
   - List specific changes (e.g., "Add type hints to all functions", "Move domain logic out of infrastructure layer")
4. **Apply changes** following project patterns:
   - Use actual project entities/names from skills
   - Follow patterns from relevant skills
   - Maintain existing functionality
   - Add proper error handling if missing
   - Add type hints if missing
   - Fix architecture violations
   - Update imports if structure changes
5. **Verify changes** don't break functionality

**Important:**
- Preserve existing functionality
- Use project-specific names/entities from skills
- Follow exact patterns from skills (don't invent new patterns)
- Maintain test compatibility
- Update related files if structure changes

## Step 6: Update Tests

**If tests exist:**

1. **Review test structure** against testing skill requirements
2. **Update tests** if code structure changed
3. **Add missing tests** if test coverage is required
4. **Ensure tests follow** testing patterns from `200-testing/SKILL.md`

## Step 7: Summary

**After refactoring:**

1. **List all files changed**
2. **Summarize improvements:**
   - Architecture fixes
   - Pattern compliance
   - Code quality improvements
   - Test coverage updates
3. **Note any remaining issues** that couldn't be auto-fixed
4. **Suggest next steps** if needed

## Important Notes

- **Always read skills first** - Don't assume patterns, read them from `.cursor/skills/`
- **Use project context** - Use actual project names, entities, and patterns from skills
- **Preserve functionality** - Refactoring should not change behavior
- **Incremental changes** - If many files need changes, work incrementally
- **Ask before major changes** - If a refactoring affects many files, confirm with user first

## Example Workflow

```
1. Load skills → Understand project uses hexagonal architecture, Python 3.11+, type hints required
2. Analyze structure → Found src/domain/, src/application/, src/infrastructure/
3. Review code → Found domain entities importing from infrastructure (violation!)
4. Prioritize → Critical: Fix dependency direction violations
5. Refactor → Move infrastructure imports out of domain, use ports instead
6. Update tests → Update tests to use ports/mocks
7. Summary → Fixed 5 files, domain layer now pure, added missing type hints
```

Start by loading project context from `.cursor/skills/`.
