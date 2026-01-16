# Setup Project: Generate Cursor Skills and Commands

Single entry point for generating Cursor skills (rules) AND commands for a project. This command will route to the appropriate project-specific command based on your project type.

## Step 1: Identify Project Type

Ask me ONE question:

**What type of project is this?**
- `hexagonal-python` - Python backend with hexagonal architecture (FastAPI + optional Airflow)
- `sdk-python` - Python SDK/Library/Component package
- `streamlit` - Streamlit MVP application
- `react-frontend` - React SPA (Vite/CRA) with Vercel best practices
- `nextjs-frontend` - Next.js App Router frontend with Vercel best practices
- `nextjs-fullstack` - Next.js fullstack (database, auth, API routes) with Vercel best practices
- `custom` - Other architecture (will ask for details)

**Note:** To understand what a project type includes before choosing, use `/explore-project-type` command (type `/explore-project-type` in Cursor chat when in the template repo).

Wait for my answer, then proceed to Step 2.

## Step 2: Route to Specific Command

Based on my answer, you must:

1. **Access the corresponding command** from User Commands:
   - `hexagonal-python` → Access User Command `init-hexagonal-python` (or read `user_commands/init-hexagonal-python.md` if available)
   - `sdk-python` → Access User Command `init-sdk-python` (or read `user_commands/init-sdk-python.md` if available)
   - `streamlit` → Access User Command `init-streamlit` (or read `user_commands/init-streamlit.md` if available)
   - `react-frontend` → Access User Command `init-react-frontend` (or read `user_commands/init-react-frontend.md` if available)
   - `nextjs-frontend` → Access User Command `init-nextjs-frontend` (or read `user_commands/init-nextjs-frontend.md` if available)
   - `nextjs-fullstack` → Access User Command `init-nextjs-fullstack` (or read `user_commands/init-nextjs-fullstack.md` if available)
   - `custom` → Use detailed interview (see below)

   **Note:** These commands should be set up as User Commands in Cursor Settings. If they're not available, try reading the files from `user_commands/` directory in the workspace, or prompt the user to set them up.

2. **Execute that command's interview and generation process** exactly as written - as if I had pasted that command directly into chat.

3. **Follow that command's instructions completely** - ask its questions in order, generate skills AND commands as specified.

## For Custom Projects - Detailed Interview

If I answered `custom`, conduct a thorough interview. Ask ONE question at a time and wait for answers. If answers are unclear or incomplete, ask follow-up questions.

### Project Basics

1. **Project name?** 
   - If unclear, ask: "What do you call this project? What's the repository name or service name?"

2. **Project purpose and domain?**
   - Ask: "What does this project do? What problem does it solve?"
   - If vague, ask: "Can you describe the main functionality? Who are the users?"
   - Follow-up: "What's the business domain? (e.g., e-commerce, finance, healthcare, social media)"

### Architecture and Structure

3. **Architecture pattern?**
   - Ask: "What architecture pattern are you using? (MVC, Clean Architecture, Hexagonal, Microservices, Monolith, Serverless, etc.)"
   - If unsure, ask: "How is your code organized? Do you have layers like controllers, services, repositories?"

4. **Project structure?**
   - Ask: "What's your folder structure? Can you describe the main directories?"
   - If unclear, ask: "Where do you put your business logic? Where are your API routes? Where are your models/entities?"
   - Follow-up: "Are there any special directories? (e.g., migrations, scripts, config)"

### Tech Stack - Be Specific

5. **Programming language and version?**
   - Ask: "What programming language? What version? (e.g., Python 3.11, Node.js 18, TypeScript 5.0)"
   - If not specified, ask: "Do you have a specific version requirement?"

6. **Main framework/library?**
   - Ask: "What's your main framework? (e.g., FastAPI, Express, Django, Next.js, React)"
   - Follow-up: "Any other major libraries? (e.g., Prisma, SQLAlchemy, Pydantic)"

7. **Database?**
   - Ask: "What database are you using? (PostgreSQL, MySQL, MongoDB, SQLite, none)"
   - If yes, ask: "Are you using an ORM? Which one? (e.g., SQLAlchemy, Prisma, TypeORM)"
   - Follow-up: "How do you handle migrations?"

8. **External services?**
   - Ask: "What external services do you integrate with?"
   - Break down:
     - **Authentication:** "How do you handle auth? (Clerk, Auth0, custom JWT, OAuth, none)"
     - **Storage:** "File storage? (S3, Cloud Storage, local, none)"
     - **APIs:** "Do you call external APIs? Which ones?"
     - **Message queues:** "Message queues? (RabbitMQ, Kafka, SQS, none)"
     - **Cache:** "Caching? (Redis, Memcached, none)"

9. **Orchestration/workflows?**
   - Ask: "Do you have scheduled tasks or workflows? (Airflow, Prefect, Cron, GitHub Actions, none)"
   - If yes, ask: "What do these workflows do? How often do they run?"

### Development Practices

10. **Testing framework and approach?**
    - Ask: "What testing framework? (pytest, Jest, Vitest, unittest, none)"
    - Follow-up: "What's your testing strategy? (unit tests, integration tests, e2e tests)"
    - Ask: "What's your target test coverage? (percentage or 'not specified')"

11. **Code quality tools?**
    - Ask: "Do you use linters/formatters? (ESLint, Prettier, Black, Ruff, none)"
    - Follow-up: "Any other code quality tools? (mypy, SonarQube, etc.)"

12. **CI/CD?**
    - Ask: "Do you have CI/CD? (GitHub Actions, GitLab CI, Jenkins, none)"
    - If yes, ask: "What does your pipeline do? (tests, linting, deployment)"

### Patterns and Conventions

13. **Main entities/domain objects?**
    - Ask: "What are the main entities in your domain? (e.g., User, Order, Product, Payment)"
    - If unclear, ask: "What are the core business objects this system manages?"
    - Follow-up: "Can you list 3-5 main entities?"

14. **Key patterns/conventions?**
    - Ask: "Are there specific patterns you follow? (e.g., Repository pattern, Factory pattern, Dependency Injection)"
    - Ask: "Any naming conventions? (e.g., snake_case, camelCase, PascalCase)"
    - Ask: "How do you handle errors? (custom exceptions, error codes, Result types)"

15. **API style?**
    - If applicable, ask: "What API style? (REST, GraphQL, gRPC, RPC)"
    - Follow-up: "How do you structure your API routes/endpoints?"

### Commands to Generate

16. **What commands would be useful?**
    - Ask: "What repetitive tasks do you do in this project? (e.g., 'create migration', 'run tests', 'deploy', 'seed database')"
    - Ask: "What commands would speed up your workflow? (e.g., '/generate-model', '/create-test', '/deploy-staging')"
    - Follow-up: "List 3-5 commands that would be most helpful"
    - For each command, ask: "What should `/command-name` do? What questions should it ask?"

## Step 3: Check for Existing Files

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

## Step 3.5: Determine Repository Type

**CRITICAL:** Before generating commands, determine if this is a new or existing repository.

Ask me ONE question:

**Is this a new repository or an existing one?**
- `new` - New repository, no existing codebase (or minimal setup)
- `existing` - Existing repository with code already present

Wait for my answer, then proceed to command generation.

## Generate Skills and Commands

After handling existing files (or if none exist), generate:

### Skills and Rules

**CRITICAL:** Generate both formats for maximum compatibility:
1. **Skills** in `.cursor/skills/<name>/SKILL.md` format (existing format)
2. **Rules** in `.cursor/rules/<rule_name>.mdc` format (alternative format)

For each skill/rule, create BOTH files with the same content. The rule name should match the skill name (e.g., `000-project-core` → `.cursor/rules/000-project-core.mdc`).

**CRITICAL:** Each skill file MUST start with frontmatter. Use the appropriate format based on skill type:

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

Generate these skills and rules (create BOTH formats for each):

### Core Project Skills (Always-On)

- `.cursor/skills/000-project-core/SKILL.md` AND `.cursor/rules/000-project-core.mdc` (always-on) - Project overview, architecture, domain
  - Frontmatter: `name: "000-project-core"`, `description: "Project overview, architecture, domain"`, `alwaysApply: true`
  - **CRITICAL:** Must include a "Project Context" section at the top with:
    - Project name (from Q1)
    - Project purpose/description (what it does, problem it solves, who uses it)
    - Domain/entities (from Q13)
    - Tech stack summary (from Q5-Q9)
    - Architecture pattern (from Q3)
  - This context helps the AI understand what the project is about and make appropriate suggestions
  - **Generate both:** Create the skill file AND the rule file with identical content

- `.cursor/skills/010-language-standards/SKILL.md` AND `.cursor/rules/010-language-standards.mdc` (always-on) - Language conventions, formatting
  - Frontmatter: `name: "010-language-standards"`, `description: "Language conventions, formatting"`, `alwaysApply: true`
  - **Generate both:** Create the skill file AND the rule file with identical content

### Quality & Process Skills (Always-On) - NEW

- `.cursor/skills/050-tdd-workflow/SKILL.md` AND `.cursor/rules/050-tdd-workflow.mdc` (always-on) - TDD workflow with RED-GREEN-VALIDATE
  - Frontmatter: `name: "050-tdd-workflow"`, `description: "TDD workflow with RED-GREEN-VALIDATE phases"`, `alwaysApply: true`
  - **Content must include:**
    - Language-specific test commands (based on tech stack: pytest for Python, jest/vitest for JS/TS)
    - RED phase: Commands to run tests expecting failures
    - GREEN phase: Commands to run tests expecting pass
    - VALIDATE phase: Full validation command (lint + typecheck + coverage)
    - TDD Execution Log template for todos/PRs
    - Blocking conditions (when NOT to mark complete)
    - Bug fix workflow with test gap analysis
  - **Generate both:** Create the skill file AND the rule file with identical content

- `.cursor/skills/060-simplicity-constraints/SKILL.md` AND `.cursor/rules/060-simplicity-constraints.mdc` (always-on) - Code simplicity constraints
  - Frontmatter: `name: "060-simplicity-constraints"`, `description: "Code simplicity constraints and limits"`, `alwaysApply: true`
  - **Content must include:**
    - Hard limits table: 20 lines/function, 200 lines/file, 3 params max, 2 levels nesting
    - Enforcement protocol (check before completing any file)
    - Language-specific examples for reducing complexity
    - "Never defer refactoring" principle
  - **Generate both:** Create the skill file AND the rule file with identical content

- `.cursor/skills/070-session-management/SKILL.md` AND `.cursor/rules/070-session-management.mdc` (always-on) - Session state and context preservation
  - Frontmatter: `name: "070-session-management"`, `description: "Session state and context preservation"`, `alwaysApply: true`
  - **Content must include:**
    - Checkpoint triggers table (when to update state)
    - Session file structure (`_project_specs/session/`)
    - Templates for: current-state.md, decisions.md, code-landmarks.md
    - Decision logging format
    - Resume instructions format
  - **Generate both:** Create the skill file AND the rule file with identical content

- `.cursor/skills/080-code-review/SKILL.md` AND `.cursor/rules/080-code-review.mdc` (always-on) - Code review requirements
  - Frontmatter: `name: "080-code-review"`, `description: "Code review requirements and workflow"`, `alwaysApply: true`
  - **Content must include:**
    - Severity levels (🔴 Critical, 🟠 High, 🟡 Medium, 🟢 Low)
    - Review categories (Security, Performance, Architecture, Code Quality, Testing)
    - Framework/language-specific review points
    - Workflow: Code → Test → Review → Fix → Commit
  - **Generate both:** Create the skill file AND the rule file with identical content

- `.cursor/skills/090-commit-hygiene/SKILL.md` AND `.cursor/rules/090-commit-hygiene.mdc` (always-on) - Commit and PR size management
  - Frontmatter: `name: "090-commit-hygiene"`, `description: "Commit and PR size management"`, `alwaysApply: true`
  - **Content must include:**
    - Size thresholds table (files, lines, time)
    - Atomic commit rule ("if you need 'and', split it")
    - Commit triggers (when to commit)
    - PR size impact research
    - Splitting strategies
  - **Generate both:** Create the skill file AND the rule file with identical content

### Layer-Specific Skills (Auto-Attach)

- Layer-specific skills and rules with appropriate globs based on structure
  - Each should have: `name`, `description`, `globs: ["pattern/**"]`
  - **Generate both:** For each layer skill, create BOTH `.cursor/skills/<name>/SKILL.md` AND `.cursor/rules/<name>.mdc` with identical content

### Testing Skills (Auto-Attach)

- `.cursor/skills/200-testing/SKILL.md` AND `.cursor/rules/200-testing.mdc` (glob: `tests/**` or test patterns)
  - Frontmatter: `name: "200-testing"`, `description: "Testing patterns and standards"`, `globs: ["tests/**"]` (or appropriate test pattern)
  - **Content must include:**
    - TDD workflow integration (reference 050-tdd-workflow)
    - Test structure mirroring source
    - Fixture patterns and conftest organization
    - Mocking strategies
    - Coverage requirements (80% minimum)
  - **Generate both:** Create the skill file AND the rule file with identical content

### Workflow Skills (Manual)

- `.cursor/skills/900-new-feature/SKILL.md` AND `.cursor/rules/900-new-feature.mdc` (manual) - Workflow for adding features
  - Frontmatter: `name: "900-new-feature"`, `description: "Workflow for adding features"` (no globs, no alwaysApply)
  - **Content must include:**
    - TDD workflow steps (RED-GREEN-VALIDATE)
    - Layer-by-layer implementation order
    - Checklist before marking complete
  - **Generate both:** Create the skill file AND the rule file with identical content

- `.cursor/skills/901-update-docs/SKILL.md` AND `.cursor/rules/901-update-docs.mdc` (manual) - Documentation checklist
  - Frontmatter: `name: "901-update-docs"`, `description: "Documentation checklist"` (no globs, no alwaysApply)
  - **Generate both:** Create the skill file AND the rule file with identical content

### Session Management Structure

**CRITICAL:** Also create the session management directory structure:

```bash
mkdir -p _project_specs/session/archive
```

Create these session files:

- `_project_specs/session/current-state.md` - Template for live session state
- `_project_specs/session/decisions.md` - Template for decision logging
- `_project_specs/session/code-landmarks.md` - Template for code navigation

**CRITICAL - Dual Format Generation:**
- For EACH skill listed above, you MUST create BOTH files:
  1. `.cursor/skills/<name>/SKILL.md` (skill format with frontmatter)
  2. `.cursor/rules/<name>.mdc` (rule format, same content, no folder structure)
- The content of both files should be IDENTICAL (same markdown content, same frontmatter)
- The rule file name matches the skill name (e.g., `000-project-core` → `000-project-core.mdc`)
- This ensures compatibility with both skill-based and rule-based Cursor configurations

### Commands

**Generate commands based on repository type:**

#### For New Repositories (if user answered `new` in Step 3.5):

**`.cursor/commands/build-project.md`** - Build complete project structure and initial files following project rules.

**To generate:**
1. Access User Command `build-project-template` (or try reading from `user_commands/build-project-template.md` if available in workspace)
   - **Note:** This command should be set up as a User Command in Cursor Settings. If it's not available, prompt the user to set it up or provide the template content.
2. Customize it based on project type:
   - Use project-specific structure patterns from the generated skills
   - Reference architecture patterns from `000-project-core/SKILL.md`
   - Reference language standards from language-specific skills
   - Reference layer-specific patterns from auto-attach skills
   - Reference testing patterns from `200-testing/SKILL.md`
   - Use actual project names, entities, and components in generated files
3. Generate as `.cursor/commands/build-project.md` in the user's project
4. This command uses the project's skills as context to build the complete project structure

#### For Existing Repositories (if user answered `existing` in Step 3.5):

**Do NOT generate `build-project.md`** unless the user specifically requests it.

**If user wants build-project for existing repo:**
- Ask: "Would you like me to generate the `/build-project` command? (yes/no)"
- If yes, generate it using the same process as for new repositories above
- If no, skip it

#### Always Generate (for both new and existing repositories):

**`.cursor/commands/review-and-refactor.md`** - Review and refactor codebase using project rules.

**To generate:**
1. Access User Command `review-and-refactor-template` (or try reading from `user_commands/review-and-refactor-template.md` if available in workspace)
   - **Note:** This command should be set up as a User Command in Cursor Settings. If it's not available, prompt the user to set it up or provide the template content.
2. Customize it based on project type:
   - Use project-specific patterns from the generated skills
   - Reference architecture patterns from `000-project-core/SKILL.md`
   - Reference language standards from language-specific skills
   - Reference layer-specific patterns from auto-attach skills
   - Reference testing patterns from `200-testing/SKILL.md`
3. Generate as `.cursor/commands/review-and-refactor.md` in the user's project
4. This command uses the project's skills as context to review and refactor existing code

**`.cursor/commands/create-or-refine-tests.md`** - Create or refine tests following TDD workflow.

**To generate:**
1. Access User Command `create-or-refine-tests-template` (or try reading from `user_commands/create-or-refine-tests-template.md` if available in workspace)
2. Customize it based on project type:
   - Use language-specific test commands (pytest for Python, jest/vitest for JS/TS)
   - Reference TDD workflow from `050-tdd-workflow/SKILL.md`
   - Reference testing patterns from `200-testing/SKILL.md`
3. Generate as `.cursor/commands/create-or-refine-tests.md` in the user's project

**`.cursor/commands/code-review.md`** - Run code review with severity classification.

**Content:**
```markdown
# Code Review

Run a code review on the current changes or specified files.

## Usage

Analyze the code for:
- 🔴 **Critical** issues (must fix, blocks commit)
- 🟠 **High** issues (should fix, blocks commit)
- 🟡 **Medium** issues (fix soon, can commit)
- 🟢 **Low** issues (nice to have)

## Review Categories

1. **Security** - Vulnerabilities, injection risks, secrets exposure
2. **Performance** - N+1 queries, memory leaks, inefficient algorithms
3. **Architecture** - SOLID violations, coupling issues, layer breaches
4. **Code Quality** - Complexity, duplication, readability
5. **Testing** - Coverage gaps, missing edge cases

## Output Format

For each issue found:
- Severity level (emoji)
- File and line number
- Issue description
- Suggested fix

## Blocking Rules

- 🔴 Critical + 🟠 High = **BLOCKED** - Fix before commit
- 🟡 Medium + 🟢 Low = **ADVISORY** - Can commit, fix soon
```

**`.cursor/commands/check-commit-size.md`** - Check if changes are ready to commit.

**Content:**
```markdown
# Check Commit Size

Check current changes against commit size thresholds.

## Thresholds

| Metric | 🟢 OK | 🟡 WARN | 🔴 STOP |
|--------|-------|---------|---------|
| Files | ≤ 5 | 6-10 | > 10 |
| Lines | ≤ 200 | 201-400 | > 400 |

## Commands to Run

```bash
# Check files changed
git diff --stat HEAD

# Check line counts
git diff --shortstat HEAD
```

## Output

Based on thresholds:
- 🟢 **OK** - Good to commit
- 🟡 **WARN** - Consider committing soon
- 🔴 **STOP** - Commit NOW, changes too large

## If Too Large

Suggest how to split:
1. By layer (database → API → frontend)
2. By feature (CRUD operations separately)
3. Refactor first, then feature
```

**Additional commands** (based on Q16):

For each command identified in Q16, create:
- `.cursor/commands/{{command-name}}.md` - With interview questions and generation logic

## Important Notes

- You must READ the specific command file to know what questions to ask and what to generate
- Use MY actual project details in all examples (project name, entities, services)
- Generate complete, runnable code examples
- Keep each skill under 200 lines
- Commands should be self-contained and useful
- If answers are vague, ask clarifying questions before proceeding

Start by asking: **"What type of project is this?"** (with the options listed above)
