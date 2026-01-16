# User Commands Index

## Main Command (Use This)

| Command | Description | Use When |
|---------|-------------|----------|
| `setup-project.md` | **Single entry point** - Routes to appropriate command based on project type. Generates both skills (rules) AND commands. | Starting any new project or setting up existing one |

This command will ask what type of project you have and automatically route to the appropriate specific command. The interview is detailed - be specific in your answers!

## Internal Commands (Used Automatically)

These commands are called internally by `setup-project.md`. You don't need to use them directly:

| Command | Project Type |
|---------|--------------|
| `init-hexagonal-python.md` | Python backend with hexagonal architecture (FastAPI + Airflow) |
| `init-sdk-python.md` | Python SDK/Library/Component package |
| `init-streamlit.md` | Streamlit MVP application |
| `init-react-frontend.md` | React SPA (Vite/CRA) with **Vercel Engineering Best Practices** |
| `init-nextjs-frontend.md` | Next.js App Router frontend with **Vercel Engineering Best Practices** |
| `init-nextjs-fullstack.md` | Next.js fullstack (DB, auth, API) with **Vercel Engineering Best Practices** |

### Vercel Best Practices Integration

The frontend project types include 45+ performance optimization rules from Vercel Engineering:
- **Eliminating Waterfalls** (CRITICAL) - Promise.all, defer await, Suspense
- **Bundle Size Optimization** (CRITICAL) - Direct imports, dynamic imports, preloading
- **Server-Side Performance** (HIGH) - React.cache, LRU cache, parallel fetching
- **Client-Side Data Fetching** (MEDIUM-HIGH) - SWR deduplication, optimistic updates
- **Re-render Optimization** (MEDIUM) - Functional setState, derived state
- **Rendering Performance** (MEDIUM) - content-visibility, static hoisting

## Command Templates

These templates are used by init commands to generate project-specific commands:

| Template | Purpose | When Generated |
|----------|---------|----------------|
| `build-project-template.md` | Template for generating project structure building commands. Uses project's skills as context to build complete project structure and initial files. | Always generated for all project types (essential for new projects) |
| `create-or-refine-tests-template.md` | Template for generating test creation commands. Follows TDD workflow (RED-GREEN-VALIDATE). | Always generated for Python projects (SDK, Hexagonal) |
| `review-and-refactor-template.md` | Template for generating code review and refactoring commands. Uses project's skills as context to review and refactor existing code. | Always generated for all project types (essential for existing projects) |
| `code-review-template.md` | **NEW** - Template for generating code review commands with severity classification. Checks security, performance, architecture, code quality, testing. | Always generated (part of quality workflow) |
| `check-commit-size-template.md` | **NEW** - Template for generating commit size checking commands. Enforces atomic commits and small PRs. | Always generated (part of quality workflow) |
| `create-github-workflow-template.md` | Template for generating GitHub Actions workflow creation commands. | Optional - only if user wants CI/CD workflows |
| `add-web-design-guidelines.md` | **NEW** - Add Vercel's Web Interface Guidelines skill. Enables UI auditing for 100+ accessibility, performance, and UX best practices. | Optional - for frontend projects needing UI quality checks |
| `browser-test-template.md` | **NEW** - Template for browser testing command. Phase 4 of TDD workflow - deploy and test in browser with checklist. | Always generated for frontend projects |

## Template Repo Commands (Use `/` in Cursor)

These are **actual Cursor commands** accessible via `/` when working on the template repo:

| Command | Description | Use When |
|---------|-------------|----------|
| `/add-project-type` | Create new quick-start command | Want to add support for new project type (e.g., Next.js, Vue, JavaScript, etc.) |
| `/modify-project-type` | Adjust existing project type to match your standards | Want to customize an existing project type (e.g., modify `sdk-python` to match your architecture) |
| `/explore-project-type` | Understand a project type's structure and rules | Want to learn about a project type's standards and patterns |
| `/add-framework-rules` | Create framework/language-specific global rules | Want to add global rules for a new framework/language (e.g., React, TypeScript, Go) |
| `/add-skill` | Add single skill to other projects | Need to add a skill to a project (not template repo) |

**Note:** These commands automatically update index files - no manual steps needed!

**How to use:** Type `/` in Cursor chat and you'll see available commands. Or type `/add-project-type` directly.

## Usage

1. Open `setup-project.md`
2. Copy entire contents
3. Paste into Cursor chat
4. Answer detailed questions - the command will route automatically
5. Skills (rules) AND commands are generated automatically
