# Generate React Frontend Rules

Quick-start for production React applications.

## Interview

**CRITICAL:** Follow interview standards - ONE question at a time, show progress (X/TOTAL), use emojis, wait for answer before proceeding.

Ask ONE at a time:

1. **Question 1/5:** 📦 Project name? (e.g., "admin-dashboard")

2. **Question 2/5:** 🛠️ Framework? (Vite, Next.js, Create React App)

3. **Question 3/5:** ⚙️ State management? (Zustand, Redux, Context API)

4. **Question 4/5:** 📦 API layer? (React Query, SWR, custom)

5. **Question 5/5:** 🎨 Styling? (Tailwind CSS, CSS Modules, styled-components)

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
├── components/
│   ├── ui/                 # Primitive components (Button, Input)
│   └── features/           # Feature components
├── pages/ (or app/)        # Route components
├── hooks/                  # Custom hooks
├── store/                  # State management (Zustand)
├── api/                    # API layer
├── types/                  # TypeScript types
├── utils/                  # Helpers
└── styles/                 # Global styles
```

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

**Important:** 
- `name` is REQUIRED - use the skill folder name
- `description` is REQUIRED - brief description of what the skill enforces
- `globs` is OPTIONAL - only include if auto-attaching to file patterns (mutually exclusive with `alwaysApply`)
- `alwaysApply` is OPTIONAL - only include if this is an always-on skill (true). Mutually exclusive with `globs`. For manual skills, omit both `globs` and `alwaysApply`.

### Always-On Skills
- `.cursor/skills/000-project-core/SKILL.md` - Architecture, component organization, conventions
  - Frontmatter: `name: "000-project-core"`, `description: "Architecture, component organization, conventions"`, `alwaysApply: true`
- `.cursor/skills/010-typescript/SKILL.md` - TypeScript standards, strict mode, type definitions
  - Frontmatter: `name: "010-typescript"`, `description: "TypeScript standards, strict mode, type definitions"`, `alwaysApply: true`

### Auto-Attach Skills
- `.cursor/skills/100-components/SKILL.md` (glob: `src/components/**`) - Component patterns, props interfaces, composition
  - Frontmatter: `name: "100-components"`, `description: "Component patterns, props interfaces, composition"`, `globs: ["src/components/**"]`
- `.cursor/skills/110-pages/SKILL.md` (glob: `src/pages/**` or `src/app/**`) - Page/route patterns, data fetching
  - Frontmatter: `name: "110-pages"`, `description: "Page/route patterns, data fetching"`, `globs: ["src/pages/**", "src/app/**"]`
- `.cursor/skills/120-hooks/SKILL.md` (glob: `src/hooks/**`) - Custom hook patterns, naming conventions
  - Frontmatter: `name: "120-hooks"`, `description: "Custom hook patterns, naming conventions"`, `globs: ["src/hooks/**"]`
- `.cursor/skills/130-state/SKILL.md` (glob: `src/store/**`) - Zustand patterns, React Query usage
  - Frontmatter: `name: "130-state"`, `description: "Zustand patterns, React Query usage"`, `globs: ["src/store/**"]`
- `.cursor/skills/140-api/SKILL.md` (glob: `src/api/**`) - API layer patterns, error handling
  - Frontmatter: `name: "140-api"`, `description: "API layer patterns, error handling"`, `globs: ["src/api/**"]`
- `.cursor/skills/200-testing/SKILL.md` (glob: `**/*.test.tsx`) - Vitest + React Testing Library patterns
  - Frontmatter: `name: "200-testing"`, `description: "Vitest + React Testing Library patterns"`, `globs: ["**/*.test.tsx"]`
- `.cursor/skills/300-styling/SKILL.md` (glob: `*.css`, tailwind) - Styling conventions, Tailwind patterns
  - Frontmatter: `name: "300-styling"`, `description: "Styling conventions, Tailwind patterns"`, `globs: ["**/*.css", "**/*.tsx"]` (adjust based on actual patterns)

## Skill Content Requirements

### 000-project-core Skill MUST Include:

**CRITICAL - Project Context Section:**
- **Project Name:** {{project_name from Q1}}
- **Project Purpose:** {{from Q2-Q5}} - What this application does, framework, state management, API layer, styling
- **Tech Stack:** {{from Q2-Q5}} - Framework (Vite/Next.js), state management (Zustand/Redux), API layer (React Query/SWR), styling (Tailwind/CSS Modules)
- **Architecture:** React frontend application structure

This context helps the AI understand what the project is about and make appropriate suggestions.

## Tech Assumptions

- React 18+ with TypeScript
- Zustand for client state (or specified alternative)
- React Query for server state (or specified alternative)
- Tailwind CSS (or specified alternative)
- Vitest + React Testing Library

Use MY actual project name, framework, and tech choices in all examples.

## Generate Commands

**ALWAYS generate this command** (essential for new projects):

**`.cursor/commands/build-project.md`** - Build complete project structure and initial files following project rules.

**To generate:**
1. Read `user_commands/build-project-template.md` from this template repo
2. Customize it for React Frontend:
   - Emphasize: create `src/` structure with components/, hooks/, services/, types/, create pages/ or app/ structure (depending on framework), create test structure mirroring src/, create configuration files (package.json, tsconfig.json, vite.config.ts or next.config.js, .eslintrc.json, etc.), create initial components and types, create API service layer, create state management setup (Zustand/Redux)
   - Reference all project skills, especially structure from `000-project-core/SKILL.md`, TypeScript standards from `010-typescript/SKILL.md`, component patterns from `100-components/SKILL.md`, and testing patterns from `200-testing/SKILL.md`
   - Use actual project name and structure in generated files
3. Generate as `.cursor/commands/build-project.md` in the user's project
4. This command uses the project's skills as context to build the complete project structure

**ALWAYS generate this command** (essential for existing projects):

**`.cursor/commands/review-and-refactor.md`** - Review and refactor codebase using project rules.

**To generate:**
1. Read `user_commands/review-and-refactor-template.md` from this template repo
2. Customize it for React Frontend:
   - Emphasize: review component structure and composition, check TypeScript type definitions, verify hooks patterns, check state management (Zustand/Redux), verify API layer patterns, check styling conventions (Tailwind/CSS Modules), verify test structure and React Testing Library patterns
   - Reference all project skills, especially architecture from `000-project-core/SKILL.md`, TypeScript standards from `010-typescript/SKILL.md`, component patterns from `100-components/SKILL.md`, and testing patterns from `200-testing/SKILL.md`
3. Generate as `.cursor/commands/review-and-refactor.md` in the user's project
4. This command uses the project's skills as context to review and refactor existing code

Start with question #1.
