# Cursor Rules Toolkit - Implementation Plan

## Overview

This repository serves as a personal, version-controlled system for generating Cursor IDE rules across all projects. It provides:
1. **User Rules** - Global instructions for Cursor Settings → Rules
2. **User Commands** - Prompts that trigger rule generation workflows

## Repository Structure

```
cursor-rules-toolkit/
├── README.md                           # Usage guide and setup instructions
├── PLAN.md                             # This file - implementation plan
├── user_rules/
│   └── global_rules.md                 # Copy to Cursor Settings → Rules
└── user_commands/
    ├── README.md                       # Index of available commands
    ├── init_project_rules.md           # Main command: interview + generate all rules
    ├── init_hexagonal_python.md        # Quick start for hexagonal FastAPI/Airflow
    ├── init_sdk_python.md              # Quick start for Python SDK/components
    ├── init_streamlit.md               # Quick start for Streamlit MVP
    ├── init_react_frontend.md          # Quick start for React production
    └── add_rule.md                     # Add a single rule to existing project
```

## File Specifications

### 1. README.md

**Purpose:** Main entry point explaining the repository

**Content Structure:**
- What this repo is for (personal rule generation system)
- Quick start guide:
  1. Clone/update this repo
  2. Copy `user_rules/global_rules.md` to Cursor Settings → Rules
  3. When starting a project, paste a command from `user_commands/` into Cursor chat
- How to extend (add your own commands, update rules over time)
- Workflow diagram showing the process
- Links to command documentation

**Key Sections:**
- Introduction
- Setup (one-time)
- Usage (per-project)
- Maintenance (updating rules)
- Contributing (to your own repo)

### 2. user_rules/global_rules.md

**Purpose:** Global preferences that apply to ALL coding projects

**Content Requirements:**
- Keep under 100 lines (loaded on every prompt)
- Personal coding standards (type hints, OOP patterns, SOLID, DRY, KISS)
- Python specifics (3.11+, annotations, import order, async/await)
- General behavior (concise, ask questions, practical examples, no placeholders)
- Testing requirements (80% coverage minimum)
- Documentation requirements (update README/tests with changes)

**Structure:**
```markdown
# My Development Standards

## When I say "setup cursor rules" or "init project rules":
[Interview questions and generation workflow]

## My default preferences (apply to all code):
[Standards list]
```

### 3. user_commands/README.md

**Purpose:** Index of all available commands

**Content:**
- Table listing each command with:
  - Command name
  - One-line description
  - When to use it
  - Quick example
- Usage instructions (how to paste commands)
- Command categories (full setup vs quick-start vs utilities)

### 4. user_commands/init_project_rules.md

**Purpose:** Main command for comprehensive rule generation

**Workflow:**
1. Interview user (one question at a time):
   - Project name and description
   - Architecture type (hexagonal-python, sdk-python, streamlit, react, other)
   - Main entities/components
   - External services (database, auth, others)
   - Orchestration (Airflow, Prefect, none)
   - Testing framework
   - CI/CD
   - Infrastructure as Code
   - Docker needed

2. Generate `.cursor/rules/` structure based on answers
3. Create `AGENTS.md` at project root
4. Provide summary

**Command Format:**
- Self-contained prompt that can be pasted directly
- Clear instructions for the AI to follow
- Interview script with conditional logic
- Rule generation templates based on architecture type

**Key Features:**
- Conditional rule generation (only generate relevant rules)
- Project-specific customization (use actual names, entities, services)
- Complete file generation (no placeholders)

### 5. user_commands/init_hexagonal_python.md

**Purpose:** Quick-start for Python hexagonal architecture

**Interview Questions (minimal):**
- Project name
- Main domain entities
- External services (database: supabase/postgres, auth: clerk/auth0, others)
- Has Airflow? (yes/no)

**Structure to Generate:**
```
src/
├── domain/
│   ├── entities/
│   ├── value_objects/
│   ├── ports/
│   ├── services/
│   └── exceptions.py
├── application/
│   ├── use_cases/
│   ├── pipelines/
│   ├── components/
│   └── resources/
├── infrastructure/
│   ├── inbound_adapters/
│   │   ├── api/
│   │   └── cli/
│   ├── outbound_adapters/
│   │   ├── database/
│   │   ├── auth/
│   │   └── ...
│   └── config/
├── interfaces/
└── config/
    ├── base.yaml
    └── environments/
```

**Rules to Generate:**
- `000-project-core.mdc` (Always) - Architecture overview, dependency direction
- `010-python-standards.mdc` (Always) - Python conventions
- `100-domain-layer.mdc` (Auto: src/domain/**) - Pure business logic
- `110-application-layer.mdc` (Auto: src/application/**) - Use case patterns
- `120-infrastructure.mdc` (Auto: src/infrastructure/**) - Adapter patterns
- `121-fastapi.mdc` (Auto: src/infrastructure/inbound_adapters/api/**) - Route patterns
- `122-airflow.mdc` (Auto: src/infrastructure/inbound_adapters/cli/**) - DAG patterns (if Airflow)
- `123-adapters.mdc` (Auto: src/infrastructure/outbound_adapters/**) - External service adapters
- `130-interfaces.mdc` (Auto: src/interfaces/**) - Pydantic schemas
- `200-testing.mdc` (Auto: tests/**) - Testing patterns
- `300-terraform.mdc` (Auto: terraform/**) - IaC patterns (if terraform)
- `400-config.mdc` (Auto: config/**/*.yaml) - YAML structure
- `900-new-feature.mdc` (Manual) - Feature workflow
- `901-update-docs.mdc` (Manual) - Documentation checklist

**Rule Content Requirements:**
- Correct frontmatter (description, globs, alwaysApply)
- Real code examples specific to stack
- Clear constraints (DO/DON'T)
- WHY explanations

### 6. user_commands/init_sdk_python.md

**Purpose:** Quick-start for Python SDK/Library projects

**Structure to Generate:**
```
src/
├── {{package_name}}/
│   ├── __init__.py
│   ├── client.py
│   ├── config.py
│   ├── exceptions.py
│   ├── core/
│   ├── components/
│   ├── models/
│   └── _internal/
├── tests/
└── docs/
```

**Key Principles:**
- Public API = exports from `__init__.py`
- `_internal/` is private
- Components follow ports/adapters
- Deprecation before removal
- Docstrings with examples

**Rules to Generate:**
- `000-package-core.mdc` (Always) - SDK design principles
- `010-python-standards.mdc` (Always) - Python conventions
- `100-public-api.mdc` (Auto: src/{{package}}/__init__.py, client.py)
- `110-core.mdc` (Auto: src/{{package}}/core/**)
- `120-components.mdc` (Auto: src/{{package}}/components/**)
- `130-models.mdc` (Auto: src/{{package}}/models/**)
- `140-exceptions.mdc` (Auto: src/{{package}}/exceptions.py)
- `200-testing.mdc` (Auto: tests/**)
- `300-documentation.mdc` (Auto: docs/**, README.md)
- `900-api-changes.mdc` (Manual) - Breaking change workflow
- `901-release.mdc` (Manual) - Publishing workflow

### 7. user_commands/init_streamlit.md

**Purpose:** Quick-start for Streamlit MVP applications

**Structure to Generate:**
```
src/
├── app.py
├── pages/
├── components/
├── services/
├── models/
└── utils/
config/
├── config.yaml
└── .streamlit/
```

**Rules to Generate:**
- `000-project-core.mdc` (Always) - Project overview
- `100-pages.mdc` (Auto: src/pages/**) - Page structure
- `110-components.mdc` (Auto: src/components/**) - Component patterns
- `120-services.mdc` (Auto: src/services/**) - Business logic
- `200-testing.mdc` (Auto: tests/**) - Testing patterns

### 8. user_commands/init_react_frontend.md

**Purpose:** Quick-start for production React applications

**Tech Assumptions:**
- React 18+ with TypeScript
- Vite or Next.js
- Zustand for client state
- React Query for server state
- Tailwind CSS
- Vitest + React Testing Library

**Structure to Generate:**
```
src/
├── components/
│   ├── ui/
│   └── features/
├── pages/ (or app/)
├── hooks/
├── store/
├── api/
├── types/
├── utils/
└── styles/
```

**Rules to Generate:**
- `000-project-core.mdc` (Always) - Architecture
- `010-typescript.mdc` (Always) - TS standards
- `100-components.mdc` (Auto: src/components/**)
- `110-pages.mdc` (Auto: src/pages/** or src/app/**)
- `120-hooks.mdc` (Auto: src/hooks/**)
- `130-state.mdc` (Auto: src/store/**)
- `140-api.mdc` (Auto: src/api/**)
- `200-testing.mdc` (Auto: **/*.test.tsx)
- `300-styling.mdc` (Auto: *.css, tailwind)

### 9. user_commands/add_rule.md

**Purpose:** Add a single rule to existing project

**Workflow:**
1. Ask: What should this rule cover? (description)
2. Ask: When should it activate? (always, auto-attach to glob, manual)
3. Ask: Any specific patterns or examples?
4. Generate single `.mdc` file with appropriate naming

**Command Format:**
- Simple interview script
- Rule template generator
- File naming convention helper

## Rule File Specifications

### Frontmatter Format

Every `.mdc` rule file must have:

```markdown
---
description: "Clear description of what this rule covers"
globs: ["pattern1/**", "pattern2/**"]  # For auto-attach rules
alwaysApply: true/false                 # For always-on rules
---

# Rule Title

[Rule content]
```

### Rule Content Standards

1. **Real Code Examples:** Use actual, runnable code, not pseudo-code
2. **Stack-Specific:** Reference actual libraries/frameworks from the project
3. **DO/DON'T Examples:** Show both correct and incorrect patterns
4. **WHY Explanations:** Explain reasoning behind patterns
5. **Concise:** Under 200 lines per rule
6. **Actionable:** Clear constraints and guidelines

### Rule Naming Convention

- `000-` prefix: Always-on core rules
- `010-` prefix: Always-on language/framework standards
- `100-` prefix: Auto-attach layer rules
- `200-` prefix: Auto-attach testing rules
- `300-` prefix: Auto-attach infrastructure/tooling rules
- `400-` prefix: Auto-attach config rules
- `900-` prefix: Manual workflow rules

## Command Implementation Strategy

### Interview Pattern

All commands should follow this pattern:

1. **Greeting:** Explain what will happen
2. **Question Loop:** Ask one question at a time, wait for answer
3. **Confirmation:** Summarize answers before generating
4. **Generation:** Create all files
5. **Summary:** Show what was created and how to use it

### Code Generation Approach

Commands should:
- Use actual project details (names, entities, services) in examples
- Generate complete files (no TODOs or placeholders)
- Include proper imports and dependencies
- Follow the project's actual structure
- Reference real libraries from the tech stack

### Conditional Logic

Commands should:
- Only generate relevant rules (e.g., skip Airflow rules if not using Airflow)
- Adapt structure based on answers (e.g., different folder structures)
- Include/exclude sections based on services used
- Customize examples with actual entity names

## Quality Checklist

For each command file:
- [ ] Self-contained (works when pasted directly)
- [ ] Clear interview script
- [ ] Conditional rule generation
- [ ] Project-specific customization
- [ ] Complete file generation
- [ ] Proper frontmatter in all rules
- [ ] Real code examples
- [ ] DO/DON'T patterns
- [ ] WHY explanations

For each rule template:
- [ ] Correct frontmatter
- [ ] Appropriate globs or alwaysApply
- [ ] Real, stack-specific examples
- [ ] Clear constraints
- [ ] Under 200 lines
- [ ] Actionable guidelines

## Implementation Phases

### Phase 1: Foundation
1. Create repository structure
2. Write README.md
3. Create user_rules/global_rules.md
4. Create user_commands/README.md

### Phase 2: Main Command
1. Implement init_project_rules.md with full interview
2. Create rule templates for all architecture types
3. Test command with sample projects

### Phase 3: Quick-Start Commands
1. Implement init_hexagonal_python.md
2. Implement init_sdk_python.md
3. Implement init_streamlit.md
4. Implement init_react_frontend.md

### Phase 4: Utilities
1. Implement add_rule.md
2. Add any additional utility commands

### Phase 5: Refinement
1. Test all commands with real projects
2. Refine rule templates based on usage
3. Update documentation
4. Add examples and use cases

## Testing Strategy

For each command:
1. Create a test project
2. Paste the command into Cursor chat
3. Complete the interview
4. Verify all expected files are generated
5. Check rule frontmatter is correct
6. Verify examples are project-specific
7. Test that rules activate correctly in Cursor

## Maintenance Plan

- **Version Control:** Track changes to rules over time
- **Feedback Loop:** Note which rules are most/least useful
- **Evolution:** Update rules as coding practices evolve
- **Documentation:** Keep README updated with new commands
- **Examples:** Add real-world examples of generated rules

## Success Criteria

The repository is successful when:
1. User can copy global_rules.md to Cursor settings in < 2 minutes
2. User can generate project rules in < 5 minutes using a command
3. Generated rules are immediately useful (no manual editing needed)
4. Rules activate correctly based on globs/alwaysApply
5. Examples in rules match the actual project structure
6. Rules help enforce consistent patterns across projects
