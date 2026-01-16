# Generate Streamlit Rules

Quick-start for Streamlit MVP applications - supports both simple and complex MVPs.

## Interview

**CRITICAL:** Follow interview standards - ONE question at a time, show progress (X/TOTAL), use emojis, wait for answer before proceeding.

Ask ONE at a time:

### Core Questions (Required)

1. **Question 1/5:** 🎯 Project name? (e.g., "dashboard-app")

2. **Question 2/5:** 🏗️ Main pages/sections? (e.g., "dashboard, settings, reports")

3. **Question 3/5:** 📦 Data sources? (API, database, files, etc.)

### Optional Questions (Ask if relevant)

4. **Question 4/5:** 🔐 Authentication needed? (e.g., "Clerk", "Google Auth", "None")
   - If yes: Which provider? How should session tokens be handled for API calls?

5. **Question 5/5:** 🌐 Backend API integration? (e.g., "REST API at https://api.example.com", "None")
   - If yes: API base URL? Authentication method? (Bearer token, API key, etc.)

**Note:** For simple MVPs, questions 4-5 may be skipped. The interview can be re-run later to add features incrementally.

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
├── app.py                  # Main Streamlit entry
├── pages/                  # Multi-page app
│   ├── 1_dashboard.py
│   └── 2_settings.py
├── components/             # Reusable UI components
├── services/               # Business logic
│   ├── api/                # API clients (if backend integration)
│   └── state/              # State management (if complex state needed)
├── models/                 # Data models (Pydantic)
├── core/                   # Core utilities
│   └── exceptions.py       # Custom exceptions
└── utils/                  # Helpers
config/
├── config.yaml
└── .streamlit/
    └── config.toml
```

## Tech Stack

- **Python 3.11+** - Modern Python features
- **Streamlit** - Web framework
- **Pydantic** - Data validation and models
- **httpx** - Async HTTP client for API calls
- **pytest** - Testing framework (80% coverage minimum)

## Key Principles

### Type System
- **Type hints everywhere** - All functions, methods, and class attributes must have type annotations
- **Use `from __future__ import annotations`** - For forward references and cleaner type hints
- **Type check with mypy** - Ensure type hints are correct and consistent

### Code Style
- **Follow PEP 8** - Use Black or Ruff for formatting
- **Use descriptive names** - Variable and function names should clearly express intent
- **Keep functions focused** - Single responsibility principle
- **Use docstrings** - NumPy-style docstrings for complex functions/classes
- **English docstrings** - All docstrings in English

### Async/Await Patterns
- **Use async/await** - Prefer async functions for I/O operations (API calls, database)
- **Use httpx** - For async HTTP requests instead of requests
- **Handle async context properly** - Use async context managers and proper cleanup

### Error Handling
- **Use custom exceptions** - Create domain-specific exception hierarchies in `src/core/exceptions.py`
- **Raise exceptions early** - Fail fast with clear error messages
- **Handle exceptions explicitly** - Don't use bare `except:` clauses
- **Use exception chaining** - Use `raise ... from ...` when appropriate

### Dependency Injection
- **Initialize dependencies in constructors** - Stateless classes with injected dependencies
- **Use dependency injection** - For services, API clients, and other dependencies

### Testing
- **Use pytest** - Standard testing framework
- **Use pytest fixtures** - For test setup and teardown
- **Mock external dependencies** - Use unittest.mock or pytest-mock
- **Test structure mirrors source** - Keep test organization aligned with source code structure
- **80% coverage minimum** - Enforce with pytest-cov

### Session State Management
- **Use `st.session_state`** - For simple state management
- **Dedicated state module** - Use `src/services/state/` if state management becomes complex
- **Keep state logic in services** - Don't mix UI and state management

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

Note: `globs` and `alwaysApply` are mutually exclusive. Choose one based on skill type.

### Always-On Skills
- `.cursor/skills/000-project-core/SKILL.md` - Project overview, Streamlit patterns, state management, tech stack
  - Frontmatter: `name: "000-project-core"`, `description: "Project overview, Streamlit patterns, state management, tech stack"`, `alwaysApply: true`

### Auto-Attach Skills
- `.cursor/skills/100-pages/SKILL.md` (glob: `src/pages/**`) - Page structure, session state patterns, page config
  - Frontmatter: `name: "100-pages"`, `description: "Page structure, session state patterns, page config"`, `globs: ["src/pages/**"]`
- `.cursor/skills/110-components/SKILL.md` (glob: `src/components/**`) - Reusable component patterns, function-based components
  - Frontmatter: `name: "110-components"`, `description: "Reusable component patterns, function-based components"`, `globs: ["src/components/**"]`
- `.cursor/skills/120-services/SKILL.md` (glob: `src/services/**`) - Business logic separation, data fetching, API clients
  - Frontmatter: `name: "120-services"`, `description: "Business logic separation, data fetching, API clients"`, `globs: ["src/services/**"]`
- `.cursor/skills/130-models/SKILL.md` (glob: `src/models/**`) - Pydantic model patterns, validation
  - Frontmatter: `name: "130-models"`, `description: "Pydantic model patterns, validation"`, `globs: ["src/models/**"]`
- `.cursor/skills/140-core/SKILL.md` (glob: `src/core/**`) - Custom exceptions, core utilities
  - Frontmatter: `name: "140-core"`, `description: "Custom exceptions, core utilities"`, `globs: ["src/core/**"]`
- `.cursor/skills/200-testing/SKILL.md` (glob: `tests/**`) - Streamlit testing patterns, mocking streamlit functions
  - Frontmatter: `name: "200-testing"`, `description: "Streamlit testing patterns, mocking streamlit functions"`, `globs: ["tests/**"]`

## Skill Content

Include examples of:

### Core Skills
- Project overview with tech stack (Python 3.11+, Streamlit, Pydantic, httpx)
- Streamlit patterns and best practices
- Session state management (simple and complex)
- Type hints everywhere
- Async/await patterns for I/O

### Pages
- Page structure with proper imports
- Type hints for all functions
- Session state patterns
- Page config and metadata

### Components
- Component patterns (functions returning st components)
- Type hints for component functions
- Reusable component design

### Services
- Service layer for data operations
- Async API clients using httpx
- Dependency injection patterns
- Error handling with custom exceptions
- State management services (if needed)

### Models
- Pydantic model patterns
- Type validation
- Model serialization/deserialization

### Core
- Custom exception hierarchies
- Exception patterns and error handling

### Testing
- Streamlit testing patterns
- Mocking streamlit functions
- Testing async services
- Testing API clients
- Pytest fixtures and patterns

Use MY actual project name, pages, and configuration in examples.

Start with question #1.
