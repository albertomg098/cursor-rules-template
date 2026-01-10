# Setup Project: Generate Cursor Skills and Commands

Single entry point for generating Cursor skills (rules) AND commands for a project. This command will route to the appropriate project-specific command based on your project type.

## Step 1: Identify Project Type

Ask me ONE question:

**What type of project is this?**
- `hexagonal-python` - Python backend with hexagonal architecture (FastAPI + optional Airflow)
- `sdk-python` - Python SDK/Library/Component package
- `streamlit` - Streamlit MVP application
- `react-frontend` - React frontend application (Vite/Next.js)
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

### Skills (Rules)

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

Generate these skills:

- `.cursor/skills/000-project-core/SKILL.md` (always-on) - Project overview, architecture, domain
  - Frontmatter: `name: "000-project-core"`, `description: "Project overview, architecture, domain"`, `alwaysApply: true`
  - **CRITICAL:** Must include a "Project Context" section at the top with:
    - Project name (from Q1)
    - Project purpose/description (what it does, problem it solves, who uses it)
    - Domain/entities (from Q13)
    - Tech stack summary (from Q5-Q9)
    - Architecture pattern (from Q3)
  - This context helps the AI understand what the project is about and make appropriate suggestions
- `.cursor/skills/010-language-standards/SKILL.md` (always-on) - Language conventions, formatting
  - Frontmatter: `name: "010-language-standards"`, `description: "Language conventions, formatting"`, `alwaysApply: true`
- Layer-specific skills with appropriate globs based on structure
  - Each should have: `name`, `description`, `globs: ["pattern/**"]`
- `.cursor/skills/200-testing/SKILL.md` (glob: `tests/**` or test patterns)
  - Frontmatter: `name: "200-testing"`, `description: "Testing patterns and standards"`, `globs: ["tests/**"]` (or appropriate test pattern)
- `.cursor/skills/900-new-feature/SKILL.md` (manual) - Workflow for adding features
  - Frontmatter: `name: "900-new-feature"`, `description: "Workflow for adding features"` (no globs, no alwaysApply)
- `.cursor/skills/901-update-docs/SKILL.md` (manual) - Documentation checklist
  - Frontmatter: `name: "901-update-docs"`, `description: "Documentation checklist"` (no globs, no alwaysApply)

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
