# Generate Streamlit Rules

Quick-start for Streamlit MVP applications - supports both simple and complex MVPs.

## Interview

**CRITICAL:** Follow interview standards - ONE question at a time, show progress (X/TOTAL), use emojis, wait for answer before proceeding.

Ask ONE at a time:

### Core Questions (Required)

1. **Question 1/4:** 🎯 Project name? (e.g., "dashboard-app")

2. **Question 2/4:** 🏗️ Main pages/sections? (e.g., "dashboard, settings, reports")

3. **Question 3/4:** 📦 Data sources? (API, database, files, etc.)

4. **Question 4/4:** 🎨 UI Style preferences? (optional - can use defaults)
   - Ask: "Do you have specific UI style preferences? (colors, theme, minimalist/modern, etc.)"
   - If yes, ask: "What colors do you want? (primary, secondary, accent colors)"
   - Ask: "What style? (minimalist, modern, corporate, colorful, dark mode, etc.)"
   - Ask: "Any specific design requirements? (spacing, typography, rounded corners, etc.)"
   - If no preferences or "use defaults", note: "Will use default minimalist style with neutral colors"
   - **Note:** A default styling rule will be created that can be customized later

### Optional Questions (Ask if relevant)

5. **Optional Question 1/2:** 🔐 Authentication needed? (e.g., "Clerk", "Google Auth", "None")
   - If yes: Which provider? How should session tokens be handled for API calls?

6. **Optional Question 2/2:** 🌐 Backend API integration? (e.g., "REST API at https://api.example.com", "None")
   - If yes: API base URL? Authentication method? (Bearer token, API key, etc.)

**Note:** For simple MVPs, only the 4 core questions are required. The optional questions (5-6) may be skipped. The interview can be re-run later to add features incrementally.

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
- `.cursor/skills/300-styling/SKILL.md` (glob: `src/pages/**`, `src/components/**`, `src/app.py`, `config/.streamlit/**`) - UI styling, colors, theme, design system
  - Frontmatter: `name: "300-styling"`, `description: "UI styling, colors, theme, design system"`, `globs: ["src/pages/**", "src/components/**", "src/app.py", "config/.streamlit/**"]`

## Skill Content

Include examples of:

### Core Skills (000-project-core)

**CRITICAL - Project Context Section:**
- **Project Name:** {{project_name from Q1}}
- **Project Purpose:** {{from Q2-Q3}} - What this application does, main pages/sections, data sources
- **UI Style:** {{from Q4}} - Style preferences (colors, theme) or "default minimalist style"
- **Tech Stack:** Python 3.11+, Streamlit, Pydantic, httpx
- **Architecture:** Streamlit MVP application structure

This context helps the AI understand what the project is about and make appropriate suggestions.

**Additional Content:**
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

### Styling
- **CRITICAL:** Include a "Default Style Specification" section with:
  - **Color Palette:** (use user preferences from Q4, or defaults below)
    - Primary color: `#1f77b4` (blue) - for main actions, links
    - Secondary color: `#ff7f0e` (orange) - for secondary actions
    - Background: `#ffffff` (white) - main background
    - Surface: `#f8f9fa` (light gray) - for cards, containers
    - Text primary: `#212529` (dark gray) - main text
    - Text secondary: `#6c757d` (medium gray) - secondary text
    - Success: `#28a745` (green) - for success messages
    - Warning: `#ffc107` (yellow) - for warnings
    - Error: `#dc3545` (red) - for errors
  - **Style Theme:** Minimalist, clean, modern
  - **Spacing:** Consistent padding/margins (use Streamlit's built-in spacing)
  - **Typography:** Streamlit default fonts, clear hierarchy
  - **Components:** Rounded corners for containers, subtle shadows
  - **Layout:** Clean, spacious, well-organized
  - **Customization:** User can override these defaults in `config/.streamlit/config.toml`
- Streamlit theme configuration (config.toml)
- CSS customization patterns (if needed)
- Component styling consistency
- Color usage guidelines
- Responsive design considerations

**If user provided custom style preferences in Q4:**
- Replace default colors with user's specified colors
- Update style theme to match user preferences
- Include any specific design requirements mentioned

**If user said "use defaults" or didn't specify:**
- Use the default minimalist style specification above
- Note that defaults can be customized later in `config/.streamlit/config.toml`

Use MY actual project name, pages, and configuration in examples.

## Generate Commands

**ALWAYS generate this command** (essential for existing projects):

**`.cursor/commands/review-and-refactor.md`** - Review and refactor codebase using project rules.

**To generate:**
1. Read `user_commands/review-and-refactor-template.md` from this template repo
2. Customize it for Streamlit:
   - Emphasize: review page structure and session state usage, check component patterns (functions returning st components), verify service layer separation, check async/await patterns for I/O, verify Pydantic model usage, check error handling with custom exceptions, verify test structure and Streamlit mocking
   - Reference all project skills, especially Streamlit patterns from `000-project-core/SKILL.md`, page patterns from `100-pages/SKILL.md`, component patterns from `110-components/SKILL.md`, styling patterns from `300-styling/SKILL.md`, and testing patterns from `200-testing/SKILL.md`
3. Generate as `.cursor/commands/review-and-refactor.md` in the user's project
4. This command uses the project's skills as context to review and refactor existing code

## Styling Skill Content Requirements

The `300-styling/SKILL.md` skill MUST include:

### Default Style Specification

**Color Palette:**
- Primary: `#1f77b4` (blue) - main actions, buttons, links
- Secondary: `#ff7f0e` (orange) - secondary actions
- Background: `#ffffff` (white) - main background
- Surface: `#f8f9fa` (light gray) - cards, containers, sidebars
- Text Primary: `#212529` (dark gray) - main text
- Text Secondary: `#6c757d` (medium gray) - secondary text, labels
- Success: `#28a745` (green) - success messages, positive indicators
- Warning: `#ffc107` (yellow) - warnings, caution indicators
- Error: `#dc3545` (red) - errors, negative indicators
- Border: `#dee2e6` (light gray) - borders, dividers

**Style Theme:**
- **Design Philosophy:** Minimalist, clean, modern
- **Layout:** Spacious, well-organized, clear visual hierarchy
- **Components:** Rounded corners (border-radius: 8px), subtle shadows
- **Spacing:** Consistent padding (16px standard, 8px for tight spaces, 24px for sections)
- **Typography:** Streamlit default fonts, clear size hierarchy
- **Interactivity:** Smooth transitions, clear hover states

**Streamlit Configuration:**
- Configure in `config/.streamlit/config.toml`
- Use Streamlit's theme configuration options
- Custom CSS can be added via `config/.streamlit/style.css` if needed

**If user provided custom preferences in Q4:**
- Replace the color palette above with user's specified colors
- Update style theme to match user's preferences (e.g., "corporate", "colorful", "dark mode")
- Include any specific design requirements (spacing, typography, etc.)

**If user said "use defaults":**
- Use the default specification above
- Note: "These defaults can be customized later by editing `config/.streamlit/config.toml`"

### Styling Patterns

**DO - Use consistent styling:**
```python
# Use Streamlit's built-in components with consistent styling
st.button("Primary Action", type="primary")  # Uses primary color
st.button("Secondary Action", type="secondary")  # Uses secondary color

# Use containers for grouped content
with st.container():
    st.markdown("### Section Title")
    # Content with consistent spacing
```

**DO - Apply theme colors:**
```python
# Use success/error colors for status indicators
st.success("Operation completed")  # Uses success color
st.error("Operation failed")  # Uses error color
```

**DON'T - Mix styles:**
```python
# DON'T use random colors or inconsistent styling
st.markdown('<div style="color: #ff00ff;">Text</div>', unsafe_allow_html=True)  # Avoid random colors
```

**DON'T - Overcomplicate styling:**
```python
# DON'T add unnecessary CSS unless needed
# Prefer Streamlit's built-in styling options
```

Start with question #1.
