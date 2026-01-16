# Generate React Frontend Rules (Vercel Best Practices)

Quick-start for production React SPA applications (Vite, Create React App) following **Vercel Engineering's React Best Practices**.

This command generates skills and commands incorporating applicable Vercel performance optimization rules:
- Bundle size optimization (CRITICAL)
- Client-side data fetching (HIGH)
- Re-render optimization (MEDIUM)
- Rendering performance (MEDIUM)
- JavaScript micro-optimizations (LOW-MEDIUM)
- Advanced patterns (LOW)

**Note:** Server-side patterns (RSC, Server Actions) don't apply to SPAs. This template focuses on client-side optimization.

## Interview

**CRITICAL:** Follow interview standards - ONE question at a time, show progress (X/TOTAL), use emojis, wait for answer before proceeding.

Ask ONE at a time:

1. **Question 1/7:** 📦 Project name? (e.g., "admin-dashboard", "customer-portal")

2. **Question 2/7:** 🛠️ Build tool and framework?
   - Vite + React (recommended)
   - Create React App
   - Vite + React with SSR (Remix, TanStack Start)

3. **Question 3/7:** ⚙️ State management approach?
   - Zustand (recommended for simplicity)
   - Jotai (atomic state)
   - Redux Toolkit
   - Context API only

4. **Question 4/7:** 📦 Data fetching strategy?
   - SWR (recommended - built by Vercel)
   - React Query / TanStack Query
   - RTK Query
   - Custom fetch hooks

5. **Question 5/7:** 🎨 Styling solution?
   - Tailwind CSS (recommended)
   - CSS Modules
   - styled-components / Emotion
   - Vanilla CSS

6. **Question 6/7:** 🌐 API architecture?
   - REST API
   - GraphQL (Apollo, urql)
   - tRPC (if using separate backend)

7. **Question 7/7:** 📊 Key features to implement?
   - Dashboard with data tables
   - Forms with validation (React Hook Form, Formik)
   - Real-time updates (WebSockets)
   - File uploads
   - Authentication
   - Multiple languages (i18n)
   - Other (specify)

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
     - Identify what's custom vs. what's template-generated
     - Merge strategy: Update patterns, preserve project-specific examples
     - Show diff before writing
   - For new files: Generate normally

## Generate Structure

```
src/
├── components/
│   ├── ui/                 # Primitive UI components (Button, Input, Modal)
│   ├── features/           # Feature-specific components
│   │   └── [feature]/      # Grouped by feature
│   └── layouts/            # Layout components
├── pages/                  # Page/route components
│   ├── Dashboard/
│   ├── Settings/
│   └── index.ts            # Route exports
├── hooks/                  # Custom hooks
│   ├── useAuth.ts
│   ├── useLocalStorage.ts
│   └── index.ts
├── stores/                 # State management (Zustand)
│   ├── useUserStore.ts
│   └── index.ts
├── api/                    # API layer
│   ├── client.ts           # API client (axios/fetch)
│   ├── endpoints/          # API endpoint functions
│   └── hooks/              # SWR/React Query hooks
├── types/                  # TypeScript types
│   ├── models/             # Domain model types
│   └── api/                # API request/response types
├── utils/                  # Utility functions
├── styles/                 # Global styles
├── constants/              # App constants
└── App.tsx
```

## Generate Skills and Rules

**CRITICAL:** Generate both formats for maximum compatibility:
1. **Skills** in `.cursor/skills/<name>/SKILL.md` format
2. **Rules** in `.cursor/rules/<rule_name>.mdc` format

For each skill/rule, create BOTH files with the same content.

### Always-On Skills and Rules

#### 000-project-core (Always-On)
`.cursor/skills/000-project-core/SKILL.md` AND `.cursor/rules/000-project-core.mdc`

**Frontmatter:**
```yaml
---
name: "000-project-core"
description: "React SPA architecture, component organization, conventions"
alwaysApply: true
---
```

**Content MUST include:**

```markdown
# React SPA Project Core

## Project Context

- **Project Name:** {{project_name from Q1}}
- **Purpose:** {{from features}}
- **Tech Stack:** {{build tool}} + React, {{state management}}, {{data fetching}}, {{styling}}
- **API Architecture:** {{api architecture}}

## Architecture Principles

### Component Organization
- **UI Components:** Reusable, presentational, no business logic
- **Feature Components:** Business logic, composed of UI components
- **Page Components:** Route entry points, data orchestration
- **Layout Components:** Shared page structure

### State Management Strategy
- **Server State:** SWR/React Query (API data, caching, revalidation)
- **Client State:** Zustand/Jotai (UI state, user preferences)
- **Form State:** React Hook Form (form inputs, validation)
- **URL State:** React Router (navigation, params)

### Data Flow
```
API Response → SWR/React Query Cache → Component Props → UI
User Action → Event Handler → Store/Mutation → API → Revalidation
```

## Folder Conventions

### Component Files
```
components/features/UserProfile/
├── UserProfile.tsx       # Main component
├── UserProfile.test.tsx  # Tests
├── UserAvatar.tsx        # Sub-component
├── useUserProfile.ts     # Custom hook (if needed)
└── index.ts              # Re-exports
```

### Naming Conventions
- Components: `PascalCase.tsx`
- Hooks: `useCamelCase.ts`
- Utilities: `camelCase.ts`
- Types: `PascalCase` (interfaces/types)
- Constants: `UPPER_SNAKE_CASE`
```

#### 010-typescript (Always-On)
`.cursor/skills/010-typescript/SKILL.md` AND `.cursor/rules/010-typescript.mdc`

**Frontmatter:**
```yaml
---
name: "010-typescript"
description: "TypeScript strict mode standards for React"
alwaysApply: true
---
```

**Content:**
```markdown
# TypeScript Standards for React SPA

## Strict Configuration

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitReturns": true,
    "exactOptionalPropertyTypes": true,
    "useDefineForClassFields": true
  }
}
```

## Type Patterns

### Component Props
```tsx
// DO: Interface with explicit types
interface UserCardProps {
  user: User
  isSelected?: boolean
  onSelect: (user: User) => void
  children?: React.ReactNode
}

export function UserCard({ 
  user, 
  isSelected = false, 
  onSelect,
  children 
}: UserCardProps) {
  return (
    <div onClick={() => onSelect(user)}>
      {user.name}
      {children}
    </div>
  )
}

// DON'T: Inline types or any
function UserCard({ user }: { user: any }) { ... }
```

### Event Handlers
```tsx
// DO: Explicit event types
const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
  setValue(e.target.value)
}

const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
  e.preventDefault()
  // ...
}

// DON'T: any or missing types
const handleChange = (e: any) => { ... }
```

### API Response Types
```tsx
// types/api/user.ts
interface ApiResponse<T> {
  data: T
  meta?: {
    total: number
    page: number
  }
}

interface User {
  id: string
  name: string
  email: string
  createdAt: string
}

type GetUsersResponse = ApiResponse<User[]>
type GetUserResponse = ApiResponse<User>
```

### Generic Components
```tsx
interface SelectProps<T> {
  options: T[]
  value: T | null
  onChange: (value: T) => void
  getLabel: (option: T) => string
  getValue: (option: T) => string | number
}

function Select<T>({ 
  options, 
  value, 
  onChange, 
  getLabel, 
  getValue 
}: SelectProps<T>) {
  return (
    <select
      value={value ? getValue(value) : ''}
      onChange={(e) => {
        const selected = options.find(
          opt => getValue(opt) === e.target.value
        )
        if (selected) onChange(selected)
      }}
    >
      {options.map(opt => (
        <option key={getValue(opt)} value={getValue(opt)}>
          {getLabel(opt)}
        </option>
      ))}
    </select>
  )
}
```
```

#### 020-vercel-performance-critical (Always-On) - **CRITICAL RULES**
`.cursor/skills/020-vercel-performance-critical/SKILL.md` AND `.cursor/rules/020-vercel-performance-critical.mdc`

**Frontmatter:**
```yaml
---
name: "020-vercel-performance-critical"
description: "Vercel Engineering's CRITICAL performance patterns - bundle optimization"
alwaysApply: true
---
```

**Content:**
```markdown
# Vercel Performance: CRITICAL Patterns (SPA)

These patterns from Vercel Engineering have the highest impact on SPA performance.

## 1. Bundle Size Optimization (CRITICAL)

### 1.1 Avoid Barrel File Imports (CRITICAL - 200-800ms impact)

Barrel files can add 200-800ms to app startup. Import directly from source.

**DON'T: Import from barrel (loads entire library)**
```tsx
// Loads ALL 1,583+ icons
import { Check, X, Menu } from 'lucide-react'

// Loads ALL MUI components
import { Button, TextField } from '@mui/material'

// Loads ALL of lodash
import { debounce, throttle } from 'lodash'
```

**DO: Import directly (loads only what you use)**
```tsx
// Only loads 3 icons
import Check from 'lucide-react/dist/esm/icons/check'
import X from 'lucide-react/dist/esm/icons/x'
import Menu from 'lucide-react/dist/esm/icons/menu'

// Only loads 2 components
import Button from '@mui/material/Button'
import TextField from '@mui/material/TextField'

// Only loads 2 functions
import debounce from 'lodash/debounce'
import throttle from 'lodash/throttle'
```

**Commonly affected libraries:**
- `lucide-react`, `react-icons`, `@tabler/icons-react`
- `@mui/material`, `@mui/icons-material`
- `@headlessui/react`, `@radix-ui/react-*`
- `lodash`, `date-fns`, `rxjs`, `ramda`
- `react-use`

### 1.2 Lazy Loading with React.lazy()

**DON'T: Bundle Monaco with main chunk (~300KB)**
```tsx
import MonacoEditor from './MonacoEditor'
import ChartDashboard from './ChartDashboard'
```

**DO: Lazy load heavy components**
```tsx
import { lazy, Suspense } from 'react'

const MonacoEditor = lazy(() => import('./MonacoEditor'))
const ChartDashboard = lazy(() => import('./ChartDashboard'))

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <MonacoEditor />
    </Suspense>
  )
}
```

### 1.3 Route-Based Code Splitting

```tsx
import { lazy, Suspense } from 'react'
import { Routes, Route } from 'react-router-dom'

// Lazy load all page components
const Dashboard = lazy(() => import('./pages/Dashboard'))
const Settings = lazy(() => import('./pages/Settings'))
const Analytics = lazy(() => import('./pages/Analytics'))

function App() {
  return (
    <Suspense fallback={<PageLoader />}>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/analytics" element={<Analytics />} />
      </Routes>
    </Suspense>
  )
}
```

### 1.4 Conditional Module Loading

**DO: Load heavy data only when feature is activated**
```tsx
function AnimationPlayer({ enabled }: { enabled: boolean }) {
  const [frames, setFrames] = useState<Frame[] | null>(null)

  useEffect(() => {
    if (enabled && !frames) {
      import('./animation-frames.js')
        .then(mod => setFrames(mod.frames))
        .catch(() => setEnabled(false))
    }
  }, [enabled, frames])

  if (!frames) return <Skeleton />
  return <Canvas frames={frames} />
}
```

### 1.5 Preload on User Intent

**DO: Preload before user needs it**
```tsx
function EditorButton({ onClick }: { onClick: () => void }) {
  const preload = () => {
    void import('./MonacoEditor')
  }

  return (
    <button
      onMouseEnter={preload}
      onFocus={preload}
      onClick={onClick}
    >
      Open Editor
    </button>
  )
}
```

## 2. Parallel Data Fetching (CRITICAL for SPA)

### 2.1 Promise.all() for Independent Requests

**DON'T: Sequential requests (3 round trips)**
```tsx
useEffect(() => {
  async function load() {
    const user = await fetchUser()
    const posts = await fetchPosts()
    const comments = await fetchComments()
    setData({ user, posts, comments })
  }
  load()
}, [])
```

**DO: Parallel requests (1 round trip)**
```tsx
useEffect(() => {
  async function load() {
    const [user, posts, comments] = await Promise.all([
      fetchUser(),
      fetchPosts(),
      fetchComments()
    ])
    setData({ user, posts, comments })
  }
  load()
}, [])
```

### 2.2 SWR Parallel Fetching

```tsx
function Dashboard() {
  // These run in parallel automatically
  const { data: user } = useSWR('/api/user', fetcher)
  const { data: projects } = useSWR('/api/projects', fetcher)
  const { data: notifications } = useSWR('/api/notifications', fetcher)

  if (!user || !projects || !notifications) return <Loading />

  return <DashboardContent user={user} projects={projects} />
}
```

## Impact Reference

| Pattern | Impact | Improvement |
|---------|--------|-------------|
| Direct imports | CRITICAL | 200-800ms startup |
| Route splitting | CRITICAL | 50-80% smaller initial bundle |
| Lazy loading | HIGH | Load on demand |
| Parallel fetching | HIGH | 2-3× faster data loading |
| Preload on intent | MEDIUM | Better perceived speed |
```

#### 030-vercel-performance-high (Always-On)
`.cursor/skills/030-vercel-performance-high/SKILL.md` AND `.cursor/rules/030-vercel-performance-high.mdc`

**Frontmatter:**
```yaml
---
name: "030-vercel-performance-high"
description: "Vercel Engineering's HIGH impact patterns - data fetching optimization"
alwaysApply: true
---
```

**Content:**
```markdown
# Vercel Performance: HIGH Impact Patterns (SPA)

## 3. Client-Side Data Fetching (HIGH)

### 3.1 Use SWR for Automatic Deduplication

SWR (by Vercel) provides automatic request deduplication, caching, and revalidation.

**DON'T: Manual fetching (no deduplication)**
```tsx
function UserList() {
  const [users, setUsers] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/api/users')
      .then(r => r.json())
      .then(data => {
        setUsers(data)
        setLoading(false)
      })
  }, [])

  if (loading) return <Loading />
  return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>
}
```

**DO: SWR (automatic deduplication, caching, revalidation)**
```tsx
import useSWR from 'swr'

const fetcher = (url: string) => fetch(url).then(r => r.json())

function UserList() {
  const { data: users, error, isLoading } = useSWR('/api/users', fetcher)

  if (isLoading) return <Loading />
  if (error) return <Error />
  return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>
}

// If another component uses useSWR('/api/users', fetcher),
// it will reuse the same cached data - no duplicate request!
```

### 3.2 SWR Configuration Patterns

```tsx
// lib/swr.ts
import { SWRConfig } from 'swr'

// Global config wrapper
export function SWRProvider({ children }: { children: React.ReactNode }) {
  return (
    <SWRConfig
      value={{
        fetcher: (url: string) => fetch(url).then(r => r.json()),
        revalidateOnFocus: false, // Disable for less network usage
        dedupingInterval: 2000,   // 2s dedup window
      }}
    >
      {children}
    </SWRConfig>
  )
}

// For immutable data (never changes)
export function useImmutableSWR<T>(key: string) {
  return useSWR<T>(key, {
    revalidateIfStale: false,
    revalidateOnFocus: false,
    revalidateOnReconnect: false
  })
}
```

### 3.3 Mutations with SWR

```tsx
import useSWRMutation from 'swr/mutation'

async function createUser(url: string, { arg }: { arg: CreateUserInput }) {
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(arg)
  })
  return res.json()
}

function CreateUserForm() {
  const { trigger, isMutating } = useSWRMutation('/api/users', createUser)

  const handleSubmit = async (data: CreateUserInput) => {
    await trigger(data)
    // Cache is automatically revalidated
  }

  return (
    <form onSubmit={handleSubmit}>
      {/* ... */}
      <button disabled={isMutating}>
        {isMutating ? 'Creating...' : 'Create User'}
      </button>
    </form>
  )
}
```

### 3.4 Optimistic Updates

```tsx
import useSWR, { mutate } from 'swr'

function TodoItem({ todo }: { todo: Todo }) {
  const toggleComplete = async () => {
    // Optimistically update the local data
    mutate(
      '/api/todos',
      (current: Todo[]) =>
        current.map(t =>
          t.id === todo.id ? { ...t, completed: !t.completed } : t
        ),
      false // Don't revalidate yet
    )

    // Send request to server
    await fetch(`/api/todos/${todo.id}`, {
      method: 'PATCH',
      body: JSON.stringify({ completed: !todo.completed })
    })

    // Revalidate to ensure consistency
    mutate('/api/todos')
  }

  return (
    <li onClick={toggleComplete}>
      {todo.completed ? '✅' : '⬜'} {todo.title}
    </li>
  )
}
```

### 3.5 Deduplicate Global Event Listeners

**DON'T: N instances = N listeners**
```tsx
function useKeyboardShortcut(key: string, callback: () => void) {
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if (e.metaKey && e.key === key) callback()
    }
    window.addEventListener('keydown', handler)
    return () => window.removeEventListener('keydown', handler)
  }, [key, callback])
}
```

**DO: N instances = 1 listener (with SWR subscription)**
```tsx
import useSWRSubscription from 'swr/subscription'

const keyCallbacks = new Map<string, Set<() => void>>()

function useKeyboardShortcut(key: string, callback: () => void) {
  useEffect(() => {
    if (!keyCallbacks.has(key)) keyCallbacks.set(key, new Set())
    keyCallbacks.get(key)!.add(callback)
    return () => { keyCallbacks.get(key)?.delete(callback) }
  }, [key, callback])

  useSWRSubscription('global-keydown', () => {
    const handler = (e: KeyboardEvent) => {
      if (e.metaKey && keyCallbacks.has(e.key)) {
        keyCallbacks.get(e.key)!.forEach(cb => cb())
      }
    }
    window.addEventListener('keydown', handler)
    return () => window.removeEventListener('keydown', handler)
  })
}
```
```

#### 040-vercel-performance-medium (Always-On)
`.cursor/skills/040-vercel-performance-medium/SKILL.md` AND `.cursor/rules/040-vercel-performance-medium.mdc`

**Frontmatter:**
```yaml
---
name: "040-vercel-performance-medium"
description: "Vercel Engineering's MEDIUM impact patterns - re-render and rendering optimization"
alwaysApply: true
---
```

**Content:**
```markdown
# Vercel Performance: MEDIUM Impact Patterns

## 4. Re-render Optimization (MEDIUM)

### 4.1 Use Functional setState Updates

**DON'T: Requires state dependency (unstable callback)**
```tsx
function TodoList() {
  const [items, setItems] = useState(initialItems)
  
  // Callback recreated on every items change
  const addItem = useCallback((newItem: Item) => {
    setItems([...items, newItem])
  }, [items]) // Dependency on items
  
  return <ItemsEditor items={items} onAdd={addItem} />
}
```

**DO: Stable callback with functional update**
```tsx
function TodoList() {
  const [items, setItems] = useState(initialItems)
  
  // Callback never recreated
  const addItem = useCallback((newItem: Item) => {
    setItems(curr => [...curr, newItem])
  }, []) // No dependencies!
  
  return <ItemsEditor items={items} onAdd={addItem} />
}
```

### 4.2 Lazy State Initialization

**DON'T: Runs on every render**
```tsx
// buildSearchIndex() runs on EVERY render
const [searchIndex] = useState(buildSearchIndex(items))

// JSON.parse runs on every render
const [settings] = useState(
  JSON.parse(localStorage.getItem('settings') || '{}')
)
```

**DO: Runs only once**
```tsx
// buildSearchIndex() runs ONLY on initial render
const [searchIndex] = useState(() => buildSearchIndex(items))

// JSON.parse runs only once
const [settings] = useState(() => {
  const stored = localStorage.getItem('settings')
  return stored ? JSON.parse(stored) : {}
})
```

### 4.3 Subscribe to Derived State

**DON'T: Re-renders on every pixel of resize**
```tsx
function Sidebar() {
  const width = useWindowWidth() // Updates on every pixel
  const isMobile = width < 768
  return <nav className={isMobile ? 'mobile' : 'desktop'} />
}
```

**DO: Re-renders only on boolean change**
```tsx
function Sidebar() {
  const isMobile = useMediaQuery('(max-width: 767px)')
  return <nav className={isMobile ? 'mobile' : 'desktop'} />
}
```

### 4.4 Narrow Effect Dependencies

**DON'T: Re-runs on any user field change**
```tsx
useEffect(() => {
  console.log('User ID:', user.id)
}, [user]) // Runs when any user field changes
```

**DO: Re-runs only when id changes**
```tsx
useEffect(() => {
  console.log('User ID:', user.id)
}, [user.id]) // Only when id changes
```

### 4.5 Use Transitions for Non-Urgent Updates

```tsx
import { startTransition, useState } from 'react'

function FilteredList({ items }: { items: Item[] }) {
  const [filter, setFilter] = useState('')
  const [filteredItems, setFilteredItems] = useState(items)

  const handleFilterChange = (value: string) => {
    setFilter(value) // Urgent: update input immediately
    
    startTransition(() => {
      // Non-urgent: can be interrupted
      setFilteredItems(items.filter(item => 
        item.name.includes(value)
      ))
    })
  }

  return (
    <>
      <input value={filter} onChange={e => handleFilterChange(e.target.value)} />
      <List items={filteredItems} />
    </>
  )
}
```

### 4.6 Extract to Memoized Components

**DON'T: Computes avatar even when loading**
```tsx
function Profile({ user, loading }: Props) {
  const avatar = useMemo(() => {
    const id = computeAvatarId(user)
    return <Avatar id={id} />
  }, [user])

  if (loading) return <Skeleton />
  return <div>{avatar}</div>
}
```

**DO: Skip computation when loading**
```tsx
const UserAvatar = memo(function UserAvatar({ user }: { user: User }) {
  const id = useMemo(() => computeAvatarId(user), [user])
  return <Avatar id={id} />
})

function Profile({ user, loading }: Props) {
  if (loading) return <Skeleton />
  return <div><UserAvatar user={user} /></div>
}
```

## 5. Rendering Performance (MEDIUM)

### 5.1 CSS content-visibility for Long Lists

```css
.list-item {
  content-visibility: auto;
  contain-intrinsic-size: 0 80px;
}
```

For 1000 items, browser skips layout/paint for ~990 off-screen items.

### 5.2 Animate SVG Wrapper, Not SVG

**DON'T: No hardware acceleration**
```tsx
<svg className="animate-spin">...</svg>
```

**DO: Hardware accelerated**
```tsx
<div className="animate-spin">
  <svg>...</svg>
</div>
```

### 5.3 Hoist Static JSX Elements

**DON'T: Recreates element every render**
```tsx
function Container({ loading }: { loading: boolean }) {
  return <div>{loading && <Skeleton />}</div>
}
```

**DO: Reuses same element**
```tsx
const skeleton = <Skeleton />

function Container({ loading }: { loading: boolean }) {
  return <div>{loading && skeleton}</div>
}
```

### 5.4 Use Explicit Conditional Rendering

**DON'T: Renders "0" when count is 0**
```tsx
{count && <Badge>{count}</Badge>}
```

**DO: Renders nothing when count is 0**
```tsx
{count > 0 ? <Badge>{count}</Badge> : null}
```
```

### Quality & Process Skills (050-090)

#### 050-tdd-workflow (Always-On) - **INCLUDES BROWSER TESTING**
`.cursor/skills/050-tdd-workflow/SKILL.md` AND `.cursor/rules/050-tdd-workflow.mdc`

**Frontmatter:**
```yaml
---
name: "050-tdd-workflow"
description: "TDD workflow with RED-GREEN-VALIDATE-DEPLOY phases for React SPA"
alwaysApply: true
---
```

**Content:**
```markdown
# TDD Workflow for React SPA

## The Four Phases: RED → GREEN → VALIDATE → DEPLOY

### Phase 1: RED (Write Failing Test)
```bash
npm test -- --testPathPattern="ComponentName" --watch
# Or with Vitest
npx vitest --watch ComponentName
```
- Write test first
- Verify it fails for the right reason

### Phase 2: GREEN (Make It Pass)
```bash
npm test -- --testPathPattern="ComponentName"
# Or with Vitest
npx vitest run ComponentName
```
- Write minimal code to pass
- No refactoring yet

### Phase 3: VALIDATE (Full Suite)
```bash
npm run lint && npm run typecheck && npm test -- --coverage --watchAll=false
# Or with Vitest
npm run lint && npm run typecheck && npx vitest run --coverage
```
- Run full test suite
- Check coverage meets 80% minimum
- Fix any lint/type errors

### Phase 4: DEPLOY & BROWSER TEST (CRITICAL)
```bash
# Start dev server
npm run dev

# Or build and preview production
npm run build && npm run preview
```

**Browser Testing Checklist:**
- [ ] Navigate to changed pages/components
- [ ] Test on desktop AND mobile viewport (use DevTools)
- [ ] Check console for errors/warnings
- [ ] Verify network requests in DevTools (no failed requests)
- [ ] Test user interactions (clicks, forms, navigation)
- [ ] Check loading states and error states
- [ ] Verify responsive layout at breakpoints (640px, 768px, 1024px, 1280px)
- [ ] Test with slow network (DevTools → Network → Slow 3G)
- [ ] Verify SWR/React Query caching works (check Network tab for deduplication)

**When to Skip Browser Testing:**
- Pure utility function changes (no UI impact)
- Type-only changes
- Test file changes only

**When Browser Testing is MANDATORY:**
- Any component changes
- Any styling changes
- Any API/data fetching changes
- Any routing changes
- Any state management changes
- Any SWR/React Query hook changes

## TDD Execution Log Template

For PRs and todos, include:
```markdown
## TDD Log
- [ ] RED: Test written and failing
- [ ] GREEN: Test passing
- [ ] VALIDATE: `npm run lint && npm run typecheck && npm test`
- [ ] DEPLOY: `npm run dev` → Browser tested
  - Tested pages: [list pages]
  - Viewports: desktop, mobile
  - Console errors: none
  - Network: API calls working
```

## Blocking Conditions

**DO NOT mark complete if:**
- Tests are failing
- Lint errors exist
- TypeScript errors exist
- Coverage dropped below 80%
- **Browser shows errors/warnings in console**
- **UI is broken on mobile viewport**
- **API/Network requests are failing**
- **SWR shows stale data unexpectedly**
```

Generate other standard quality skills:
- `.cursor/skills/060-simplicity-constraints/SKILL.md` - Code limits
- `.cursor/skills/070-session-management/SKILL.md` - Checkpoints
- `.cursor/skills/080-code-review/SKILL.md` - React-specific checks
- `.cursor/skills/090-commit-hygiene/SKILL.md` - Atomic commits

### Auto-Attach Skills

#### 100-components (Auto-Attach)
`.cursor/skills/100-components/SKILL.md` AND `.cursor/rules/100-components.mdc`

**Frontmatter:**
```yaml
---
name: "100-components"
description: "React component patterns and composition"
globs: ["src/components/**"]
---
```

**Content includes:**
- Props interface patterns
- Composition patterns
- Forward ref
- Compound components
- Controlled vs uncontrolled

#### 110-pages (Auto-Attach)
`.cursor/skills/110-pages/SKILL.md` AND `.cursor/rules/110-pages.mdc`

**Frontmatter:**
```yaml
---
name: "110-pages"
description: "Page component patterns and data loading"
globs: ["src/pages/**"]
---
```

#### 120-hooks (Auto-Attach)
`.cursor/skills/120-hooks/SKILL.md` AND `.cursor/rules/120-hooks.mdc`

**Frontmatter:**
```yaml
---
name: "120-hooks"
description: "Custom hook patterns following best practices"
globs: ["src/hooks/**"]
---
```

**Content includes:**
- Hook naming conventions
- Composition over configuration
- Return value patterns
- Testing hooks

#### 130-state (Auto-Attach)
`.cursor/skills/130-state/SKILL.md` AND `.cursor/rules/130-state.mdc`

**Frontmatter:**
```yaml
---
name: "130-state"
description: "Zustand/state management patterns"
globs: ["src/stores/**", "src/store/**"]
---
```

**Content includes:**
- Zustand store patterns
- Slices and selectors
- Persisted state
- Devtools integration

#### 140-api (Auto-Attach)
`.cursor/skills/140-api/SKILL.md` AND `.cursor/rules/140-api.mdc`

**Frontmatter:**
```yaml
---
name: "140-api"
description: "API layer patterns with SWR"
globs: ["src/api/**"]
---
```

**Content includes:**
- API client patterns
- SWR hooks per endpoint
- Error handling
- Request/response types

#### 200-testing (Auto-Attach)
`.cursor/skills/200-testing/SKILL.md` AND `.cursor/rules/200-testing.mdc`

**Frontmatter:**
```yaml
---
name: "200-testing"
description: "Vitest + React Testing Library patterns"
globs: ["**/*.test.tsx", "**/*.test.ts", "src/__tests__/**"]
---
```

**Content includes:**
- Component testing patterns
- Hook testing with renderHook
- User event testing
- Mock patterns for SWR/API

#### 300-styling (Auto-Attach)
`.cursor/skills/300-styling/SKILL.md` AND `.cursor/rules/300-styling.mdc`

Based on styling choice (Tailwind, CSS Modules, etc.)

### Session Management Structure

Create:
```bash
mkdir -p _project_specs/session/archive
```

Files:
- `_project_specs/session/current-state.md`
- `_project_specs/session/decisions.md`
- `_project_specs/session/code-landmarks.md`

## Generate Commands

**ALWAYS generate these commands:**

1. **`.cursor/commands/build-project.md`** - Build complete project structure
   - Read `user_commands/build-project-template.md`
   - Customize for React SPA structure

2. **`.cursor/commands/review-and-refactor.md`** - Review using Vercel patterns
   - Read `user_commands/review-and-refactor-template.md`
   - Focus on bundle size, SWR patterns, re-render optimization

3. **`.cursor/commands/create-or-refine-tests.md`** - TDD with Vitest
   - Read `user_commands/create-or-refine-tests-template.md`
   - Customize for Vitest + RTL

4. **`.cursor/commands/code-review.md`** - React-specific checks
5. **`.cursor/commands/check-commit-size.md`** - Commit thresholds
6. **`.cursor/commands/check-performance.md`** - Validate Vercel patterns
7. **`.cursor/commands/browser-test.md`** - Browser testing checklist (Phase 4 of TDD)
   - Read `user_commands/browser-test-template.md`
   - Customize for React SPA (SWR caching, routing, deep links)

**`.cursor/commands/check-performance.md`** content:
```markdown
# Check Performance Patterns

Validate code against Vercel Engineering's React Best Practices.

## Checks

### CRITICAL (Must Fix)
- [ ] No barrel file imports (import directly from source)
- [ ] Route-based code splitting with React.lazy()
- [ ] Heavy components are lazy loaded
- [ ] No sequential API calls for independent data

### HIGH (Should Fix)
- [ ] Using SWR or React Query for data fetching
- [ ] SWR deduplication is working
- [ ] Optimistic updates for mutations

### MEDIUM (Recommended)
- [ ] Functional setState updates
- [ ] Lazy state initialization
- [ ] Derived state with useMediaQuery patterns
- [ ] content-visibility for long lists

## Commands

```bash
# Check bundle size
npm run build -- --stats
npx source-map-explorer 'dist/assets/*.js'

# Find barrel imports
grep -r "from 'lucide-react'" --include="*.tsx" --include="*.ts" src/
grep -r "from '@mui/material'" --include="*.tsx" --include="*.ts" src/

# Find missing lazy loading
grep -r "import.*from '\./pages" --include="*.tsx" src/App.tsx
```
```

## Tech Assumptions

- Vite + React (or specified alternative)
- TypeScript strict mode
- Zustand for client state (or specified)
- SWR for server state (or specified)
- Tailwind CSS (or specified)
- Vitest + React Testing Library

Use MY actual project name, tech choices, and features in all examples.

Start with question #1.
