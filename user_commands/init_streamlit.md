# Generate Streamlit Rules

Quick-start for Streamlit MVP applications.

## Interview

Ask ONE at a time:

1. **Project name?** (e.g., "dashboard-app")

2. **Main pages/sections?** (e.g., "dashboard, settings, reports")

3. **Data sources?** (API, database, files, etc.)

## Generate Structure

```
src/
├── app.py                  # Main Streamlit entry
├── pages/                  # Multi-page app
│   ├── 1_dashboard.py
│   └── 2_settings.py
├── components/             # Reusable UI components
├── services/               # Business logic
├── models/                 # Data models
└── utils/                  # Helpers
config/
├── config.yaml
└── .streamlit/
    └── config.toml
```

## Generate Skills

Create skills in `.cursor/skills/<name>/SKILL.md` format:

### Always-On Skills
- `.cursor/skills/000-project-core/SKILL.md` - Project overview, Streamlit patterns, state management

### Auto-Attach Skills
- `.cursor/skills/100-pages/SKILL.md` (glob: `src/pages/**`) - Page structure, session state patterns, page config
- `.cursor/skills/110-components/SKILL.md` (glob: `src/components/**`) - Reusable component patterns, function-based components
- `.cursor/skills/120-services/SKILL.md` (glob: `src/services/**`) - Business logic separation, data fetching
- `.cursor/skills/200-testing/SKILL.md` (glob: `tests/**`) - Streamlit testing patterns, mocking streamlit functions

## Skill Content

Include examples of:
- Page structure with proper imports
- Session state management
- Component patterns (functions returning st components)
- Service layer for data operations
- Config management with YAML

Use MY actual project name and pages in examples.

Start with question #1.
