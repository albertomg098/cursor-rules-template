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

Create skills in `.cursor/skills/<name>/SKILL.md` format:

### Always-On Skills
- `.cursor/skills/000-project-core/SKILL.md` - Project overview, Streamlit patterns, state management, tech stack

### Auto-Attach Skills
- `.cursor/skills/100-pages/SKILL.md` (glob: `src/pages/**`) - Page structure, session state patterns, page config
- `.cursor/skills/110-components/SKILL.md` (glob: `src/components/**`) - Reusable component patterns, function-based components
- `.cursor/skills/120-services/SKILL.md` (glob: `src/services/**`) - Business logic separation, data fetching, API clients
- `.cursor/skills/130-models/SKILL.md` (glob: `src/models/**`) - Pydantic model patterns, validation
- `.cursor/skills/140-core/SKILL.md` (glob: `src/core/**`) - Custom exceptions, core utilities
- `.cursor/skills/200-testing/SKILL.md` (glob: `tests/**`) - Streamlit testing patterns, mocking streamlit functions

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
