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
   - `hexagonal-python` → Access User Command `init-hexagonal-python` (or read `user_commands/init_hexagonal_python.md` if available)
   - `sdk-python` → Access User Command `init-sdk-python` (or read `user_commands/init_sdk_python.md` if available)
   - `streamlit` → Access User Command `init-streamlit` (or read `user_commands/init_streamlit.md` if available)
   - `react-frontend` → Access User Command `init-react-frontend` (or read `user_commands/init_react_frontend.md` if available)
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

## Generate Skills and Commands

After collecting all answers, generate:

### Skills (Rules)

- `.cursor/skills/000-project-core/SKILL.md` (always-on) - Project overview, architecture, domain
- `.cursor/skills/010-language-standards/SKILL.md` (always-on) - Language conventions, formatting
- Layer-specific skills with appropriate globs based on structure
- `.cursor/skills/200-testing/SKILL.md` (glob: `tests/**` or test patterns)
- `.cursor/skills/900-new-feature/SKILL.md` (manual) - Workflow for adding features
- `.cursor/skills/901-update-docs/SKILL.md` (manual) - Documentation checklist

### Commands

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
