# Generate React Frontend Rules

Quick-start for production React applications.

## Interview

Ask ONE at a time:

1. **Project name?** (e.g., "admin-dashboard")

2. **Framework?** (Vite, Next.js, Create React App)

3. **State management?** (Zustand, Redux, Context API)

4. **API layer?** (React Query, SWR, custom)

5. **Styling?** (Tailwind CSS, CSS Modules, styled-components)

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

Create skills in `.cursor/skills/<name>/SKILL.md` format:

### Always-On Skills
- `.cursor/skills/000-project-core/SKILL.md` - Architecture, component organization, conventions
- `.cursor/skills/010-typescript/SKILL.md` - TypeScript standards, strict mode, type definitions

### Auto-Attach Skills
- `.cursor/skills/100-components/SKILL.md` (glob: `src/components/**`) - Component patterns, props interfaces, composition
- `.cursor/skills/110-pages/SKILL.md` (glob: `src/pages/**` or `src/app/**`) - Page/route patterns, data fetching
- `.cursor/skills/120-hooks/SKILL.md` (glob: `src/hooks/**`) - Custom hook patterns, naming conventions
- `.cursor/skills/130-state/SKILL.md` (glob: `src/store/**`) - Zustand patterns, React Query usage
- `.cursor/skills/140-api/SKILL.md` (glob: `src/api/**`) - API layer patterns, error handling
- `.cursor/skills/200-testing/SKILL.md` (glob: `**/*.test.tsx`) - Vitest + React Testing Library patterns
- `.cursor/skills/300-styling/SKILL.md` (glob: `*.css`, tailwind) - Styling conventions, Tailwind patterns

## Tech Assumptions

- React 18+ with TypeScript
- Zustand for client state (or specified alternative)
- React Query for server state (or specified alternative)
- Tailwind CSS (or specified alternative)
- Vitest + React Testing Library

Use MY actual project name, framework, and tech choices in all examples.

Start with question #1.
