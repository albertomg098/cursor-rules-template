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

Create skills in `.cursor/skills/<name>/SKILL.md` format. **CRITICAL:** Each skill file MUST start with frontmatter in this exact format:

```yaml
---
name: "skill-name"
description: "Description of what this skill enforces"
globs: ["pattern/**"]  # Only for auto-attach skills (omit for always-on or manual)
alwaysApply: true      # Only for always-on skills (omit if using globs)
---
```

**Important:** 
- `name` is REQUIRED - use the skill folder name
- `description` is REQUIRED - brief description of what the skill enforces
- `globs` is OPTIONAL - only include if auto-attaching to file patterns
- `alwaysApply` is OPTIONAL - only include if this is an always-on skill (true). If using `globs`, omit `alwaysApply`.

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

## Tech Assumptions

- React 18+ with TypeScript
- Zustand for client state (or specified alternative)
- React Query for server state (or specified alternative)
- Tailwind CSS (or specified alternative)
- Vitest + React Testing Library

Use MY actual project name, framework, and tech choices in all examples.

Start with question #1.
