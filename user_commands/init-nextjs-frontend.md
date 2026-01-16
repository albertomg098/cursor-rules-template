# Generate Next.js Frontend Rules (Vercel Best Practices)

Quick-start for production Next.js App Router applications following **Vercel Engineering's React Best Practices**.

This command generates skills and commands incorporating 45+ performance optimization rules from Vercel's engineering team, covering:
- Eliminating waterfalls (CRITICAL)
- Bundle size optimization (CRITICAL)
- Server-side performance (HIGH)
- Client-side data fetching (MEDIUM-HIGH)
- Re-render optimization (MEDIUM)
- Rendering performance (MEDIUM)
- JavaScript micro-optimizations (LOW-MEDIUM)
- Advanced patterns (LOW)

## Interview

**CRITICAL:** Follow interview standards - ONE question at a time, show progress (X/TOTAL), use emojis, wait for answer before proceeding.

Ask ONE at a time:

1. **Question 1/7:** 📦 Project name? (e.g., "admin-dashboard", "customer-portal")

2. **Question 2/7:** 🏗️ Next.js version and router? 
   - Next.js 14+ with App Router (recommended)
   - Next.js 13 with App Router
   - Next.js with Pages Router (legacy)

3. **Question 3/7:** ⚙️ State management approach?
   - Server-first (React Server Components + minimal client state)
   - Zustand for global client state
   - Jotai for atomic state
   - Redux Toolkit
   - Context API only

4. **Question 4/7:** 📦 Data fetching strategy?
   - SWR (recommended for client-side)
   - React Query / TanStack Query
   - Server Actions + RSC (Next.js 14+)
   - Custom fetch with React.cache()

5. **Question 5/7:** 🎨 Styling solution?
   - Tailwind CSS (recommended)
   - CSS Modules
   - styled-components / Emotion
   - Vanilla Extract

6. **Question 6/7:** 🔐 Authentication approach? (if any)
   - NextAuth.js / Auth.js
   - Clerk
   - Custom JWT
   - None

7. **Question 7/7:** 📊 Key features to implement?
   - Dashboard with data tables
   - Forms with validation
   - Real-time updates
   - File uploads
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
     - Identify custom vs. template-generated content
     - Merge strategy: Update patterns, preserve project-specific examples
     - Show diff before writing
   - For new files: Generate normally

## Generate Structure

```
app/
├── (auth)/                 # Auth route group
│   ├── login/
│   └── register/
├── (dashboard)/            # Dashboard route group
│   ├── layout.tsx          # Shared dashboard layout
│   └── [feature]/
├── api/                    # API routes (if needed)
├── layout.tsx              # Root layout
├── page.tsx                # Home page
└── globals.css
components/
├── ui/                     # Primitive UI components
├── features/               # Feature-specific components
└── layouts/                # Layout components
lib/
├── actions/                # Server Actions
├── api/                    # API client utilities
├── hooks/                  # Custom hooks
├── stores/                 # Client state (Zustand/Jotai)
├── utils/                  # Utility functions
└── validations/            # Zod schemas
types/
└── index.ts                # TypeScript types
```

## Generate Skills and Rules

**CRITICAL:** Generate both formats for maximum compatibility:
1. **Skills** in `.cursor/skills/<name>/SKILL.md` format
2. **Rules** in `.cursor/rules/<rule_name>.mdc` format

### Always-On Skills and Rules

#### 000-project-core (Always-On)
`.cursor/skills/000-project-core/SKILL.md` AND `.cursor/rules/000-project-core.mdc`

**Frontmatter:**
```yaml
---
name: "000-project-core"
description: "Next.js App Router architecture, conventions, and project context"
alwaysApply: true
---
```

**Content MUST include:**

```markdown
# Next.js App Router Project Core

## Project Context

- **Project Name:** {{project_name from Q1}}
- **Purpose:** {{brief description from features}}
- **Tech Stack:** Next.js {{version}} with App Router, {{state management}}, {{data fetching}}, {{styling}}
- **Authentication:** {{auth approach}}

## Architecture Principles

### Server-First Architecture
- Default to Server Components (RSC)
- Use `'use client'` directive only when necessary:
  - Event handlers (onClick, onChange, etc.)
  - Browser APIs (localStorage, window)
  - Hooks that use state (useState, useEffect)
  - Third-party client-only libraries

### File Conventions
- `page.tsx` - Route entry point
- `layout.tsx` - Shared UI wrapper
- `loading.tsx` - Suspense fallback
- `error.tsx` - Error boundary
- `not-found.tsx` - 404 page

### Folder Conventions
- `(group)` - Route groups (no URL impact)
- `[param]` - Dynamic segments
- `@slot` - Parallel routes
- `_private` - Private folders (excluded from routing)

## Component Organization

### Colocation Strategy
- Keep components close to where they're used
- Feature-specific components in `components/features/[feature]/`
- Shared UI primitives in `components/ui/`
- Layouts in `components/layouts/`

### Naming Conventions
- Components: PascalCase (`UserProfile.tsx`)
- Hooks: camelCase with `use` prefix (`useAuth.ts`)
- Utilities: camelCase (`formatDate.ts`)
- Types: PascalCase with descriptive names (`UserProfileProps`)
```

#### 010-typescript (Always-On)
`.cursor/skills/010-typescript/SKILL.md` AND `.cursor/rules/010-typescript.mdc`

**Frontmatter:**
```yaml
---
name: "010-typescript"
description: "TypeScript strict mode standards for Next.js"
alwaysApply: true
---
```

**Content:**
```markdown
# TypeScript Standards for Next.js

## Strict Configuration

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitReturns": true,
    "exactOptionalPropertyTypes": true
  }
}
```

## Type Patterns

### Component Props
```tsx
// DO: Use interface for component props
interface UserCardProps {
  user: User
  onSelect?: (user: User) => void
}

export function UserCard({ user, onSelect }: UserCardProps) {
  return <div onClick={() => onSelect?.(user)}>{user.name}</div>
}

// DON'T: Inline types or any
export function UserCard({ user }: { user: any }) { ... }
```

### Server Actions
```tsx
// DO: Type server action returns
type ActionResult<T> = 
  | { success: true; data: T }
  | { success: false; error: string }

export async function createUser(
  formData: FormData
): Promise<ActionResult<User>> {
  // ...
}
```

### API Routes
```tsx
// DO: Type request/response
import { NextRequest, NextResponse } from 'next/server'

export async function GET(
  request: NextRequest,
  { params }: { params: { id: string } }
): Promise<NextResponse<User | { error: string }>> {
  // ...
}
```
```

#### 020-vercel-performance-critical (Always-On) - **CRITICAL RULES**
`.cursor/skills/020-vercel-performance-critical/SKILL.md` AND `.cursor/rules/020-vercel-performance-critical.mdc`

**Frontmatter:**
```yaml
---
name: "020-vercel-performance-critical"
description: "Vercel Engineering's CRITICAL performance patterns - eliminating waterfalls and bundle optimization"
alwaysApply: true
---
```

**Content:**
```markdown
# Vercel Performance: CRITICAL Patterns

These patterns from Vercel Engineering have the highest impact on performance.

## 1. Eliminating Waterfalls (CRITICAL)

Waterfalls are the #1 performance killer. Each sequential await adds full network latency.

### 1.1 Promise.all() for Independent Operations

**DON'T: Sequential execution (3 round trips)**
```tsx
const user = await fetchUser()
const posts = await fetchPosts()
const comments = await fetchComments()
```

**DO: Parallel execution (1 round trip)**
```tsx
const [user, posts, comments] = await Promise.all([
  fetchUser(),
  fetchPosts(),
  fetchComments()
])
```

### 1.2 Defer Await Until Needed

**DON'T: Block both branches**
```tsx
async function handleRequest(userId: string, skipProcessing: boolean) {
  const userData = await fetchUserData(userId) // Always waits
  
  if (skipProcessing) {
    return { skipped: true }
  }
  
  return processUserData(userData)
}
```

**DO: Only await when needed**
```tsx
async function handleRequest(userId: string, skipProcessing: boolean) {
  if (skipProcessing) {
    return { skipped: true } // Returns immediately
  }
  
  const userData = await fetchUserData(userId) // Only when needed
  return processUserData(userData)
}
```

### 1.3 Start Promises Early in API Routes

**DON'T: Config waits for auth**
```tsx
export async function GET(request: Request) {
  const session = await auth()
  const config = await fetchConfig()
  const data = await fetchData(session.user.id)
  return Response.json({ data, config })
}
```

**DO: Start independent operations immediately**
```tsx
export async function GET(request: Request) {
  const sessionPromise = auth()
  const configPromise = fetchConfig()
  
  const session = await sessionPromise
  const [config, data] = await Promise.all([
    configPromise,
    fetchData(session.user.id)
  ])
  return Response.json({ data, config })
}
```

### 1.4 Strategic Suspense Boundaries

**DON'T: Block entire page with data**
```tsx
async function Page() {
  const data = await fetchData() // Blocks entire page
  
  return (
    <div>
      <Sidebar />
      <DataDisplay data={data} />
      <Footer />
    </div>
  )
}
```

**DO: Stream content with Suspense**
```tsx
function Page() {
  return (
    <div>
      <Sidebar />
      <Suspense fallback={<Skeleton />}>
        <DataDisplay />
      </Suspense>
      <Footer />
    </div>
  )
}

async function DataDisplay() {
  const data = await fetchData() // Only blocks this component
  return <div>{data.content}</div>
}
```

## 2. Bundle Size Optimization (CRITICAL)

### 2.1 Avoid Barrel File Imports (CRITICAL - 200-800ms impact)

Barrel files can add 200-800ms to cold starts. Import directly from source.

**DON'T: Import from barrel (loads 1,583+ modules)**
```tsx
import { Check, X, Menu } from 'lucide-react'
import { Button, TextField } from '@mui/material'
```

**DO: Import directly (loads only what you use)**
```tsx
import Check from 'lucide-react/dist/esm/icons/check'
import X from 'lucide-react/dist/esm/icons/x'
import Menu from 'lucide-react/dist/esm/icons/menu'
```

**OR: Use Next.js optimizePackageImports (Next.js 13.5+)**
```js
// next.config.js
module.exports = {
  experimental: {
    optimizePackageImports: ['lucide-react', '@mui/material', '@radix-ui/react-*']
  }
}
```

**Commonly affected libraries:**
- `lucide-react`, `react-icons`, `@tabler/icons-react`
- `@mui/material`, `@mui/icons-material`
- `@headlessui/react`, `@radix-ui/react-*`
- `lodash`, `date-fns`, `rxjs`

### 2.2 Dynamic Imports for Heavy Components

**DON'T: Bundle Monaco with main chunk (~300KB)**
```tsx
import { MonacoEditor } from './monaco-editor'
```

**DO: Load on demand**
```tsx
import dynamic from 'next/dynamic'

const MonacoEditor = dynamic(
  () => import('./monaco-editor').then(m => m.MonacoEditor),
  { ssr: false }
)
```

### 2.3 Defer Non-Critical Third-Party Libraries

Analytics, logging, error tracking don't block user interaction.

**DON'T: Block initial bundle**
```tsx
import { Analytics } from '@vercel/analytics/react'
```

**DO: Load after hydration**
```tsx
import dynamic from 'next/dynamic'

const Analytics = dynamic(
  () => import('@vercel/analytics/react').then(m => m.Analytics),
  { ssr: false }
)
```

### 2.4 Preload on User Intent

```tsx
function EditorButton({ onClick }: { onClick: () => void }) {
  const preload = () => {
    if (typeof window !== 'undefined') {
      void import('./monaco-editor')
    }
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

## Impact Reference

| Pattern | Impact | Improvement |
|---------|--------|-------------|
| Promise.all() | CRITICAL | 2-10× faster |
| Direct imports | CRITICAL | 200-800ms cold start |
| Dynamic imports | CRITICAL | Reduces initial bundle |
| Suspense boundaries | HIGH | Faster initial paint |
| Preload on intent | MEDIUM | Better perceived speed |
```

#### 030-vercel-performance-high (Always-On)
`.cursor/skills/030-vercel-performance-high/SKILL.md` AND `.cursor/rules/030-vercel-performance-high.mdc`

**Frontmatter:**
```yaml
---
name: "030-vercel-performance-high"
description: "Vercel Engineering's HIGH impact patterns - server-side and client-side optimization"
alwaysApply: true
---
```

**Content:**
```markdown
# Vercel Performance: HIGH Impact Patterns

## 3. Server-Side Performance (HIGH)

### 3.1 Per-Request Deduplication with React.cache()

```tsx
import { cache } from 'react'

export const getCurrentUser = cache(async () => {
  const session = await auth()
  if (!session?.user?.id) return null
  return await db.user.findUnique({
    where: { id: session.user.id }
  })
})

// Multiple calls in one request = single DB query
```

### 3.2 Cross-Request LRU Caching

For data shared across requests:

```tsx
import { LRUCache } from 'lru-cache'

const cache = new LRUCache<string, any>({
  max: 1000,
  ttl: 5 * 60 * 1000 // 5 minutes
})

export async function getUser(id: string) {
  const cached = cache.get(id)
  if (cached) return cached

  const user = await db.user.findUnique({ where: { id } })
  cache.set(id, user)
  return user
}
```

### 3.3 Minimize Serialization at RSC Boundaries

**DON'T: Serialize all 50 fields**
```tsx
async function Page() {
  const user = await fetchUser() // 50 fields
  return <Profile user={user} />
}

'use client'
function Profile({ user }: { user: User }) {
  return <div>{user.name}</div> // uses 1 field
}
```

**DO: Pass only needed fields**
```tsx
async function Page() {
  const user = await fetchUser()
  return <Profile name={user.name} />
}

'use client'
function Profile({ name }: { name: string }) {
  return <div>{name}</div>
}
```

### 3.4 Parallel Data Fetching with Component Composition

**DON'T: Sequential fetching**
```tsx
export default async function Page() {
  const header = await fetchHeader()
  return (
    <div>
      <div>{header}</div>
      <Sidebar />
    </div>
  )
}

async function Sidebar() {
  const items = await fetchSidebarItems() // Waits for header
  return <nav>{items.map(renderItem)}</nav>
}
```

**DO: Parallel fetching with composition**
```tsx
async function Header() {
  const data = await fetchHeader()
  return <div>{data}</div>
}

async function Sidebar() {
  const items = await fetchSidebarItems()
  return <nav>{items.map(renderItem)}</nav>
}

export default function Page() {
  return (
    <div>
      <Header />  {/* Both fetch simultaneously */}
      <Sidebar />
    </div>
  )
}
```

### 3.5 Use after() for Non-Blocking Operations

```tsx
import { after } from 'next/server'

export async function POST(request: Request) {
  await updateDatabase(request)
  
  // Log after response is sent
  after(async () => {
    const userAgent = (await headers()).get('user-agent')
    await logUserAction({ userAgent })
  })
  
  return Response.json({ status: 'success' })
}
```

## 4. Client-Side Data Fetching (MEDIUM-HIGH)

### 4.1 Use SWR for Automatic Deduplication

**DON'T: Manual fetch (no deduplication)**
```tsx
function UserList() {
  const [users, setUsers] = useState([])
  useEffect(() => {
    fetch('/api/users')
      .then(r => r.json())
      .then(setUsers)
  }, [])
}
```

**DO: SWR (automatic deduplication)**
```tsx
import useSWR from 'swr'

function UserList() {
  const { data: users } = useSWR('/api/users', fetcher)
}
```

### 4.2 Deduplicate Global Event Listeners

```tsx
import useSWRSubscription from 'swr/subscription'

const keyCallbacks = new Map<string, Set<() => void>>()

function useKeyboardShortcut(key: string, callback: () => void) {
  useEffect(() => {
    if (!keyCallbacks.has(key)) {
      keyCallbacks.set(key, new Set())
    }
    keyCallbacks.get(key)!.add(callback)
    return () => {
      keyCallbacks.get(key)?.delete(callback)
    }
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

## 5. Re-render Optimization (MEDIUM)

### 5.1 Use Functional setState Updates

**DON'T: Requires state dependency**
```tsx
const addItems = useCallback((newItems: Item[]) => {
  setItems([...items, ...newItems])
}, [items]) // Recreated on every items change
```

**DO: Stable callback**
```tsx
const addItems = useCallback((newItems: Item[]) => {
  setItems(curr => [...curr, ...newItems])
}, []) // Never recreated
```

### 5.2 Lazy State Initialization

**DON'T: Runs on every render**
```tsx
const [searchIndex] = useState(buildSearchIndex(items))
```

**DO: Runs only once**
```tsx
const [searchIndex] = useState(() => buildSearchIndex(items))
```

### 5.3 Defer State Reads to Usage Point

**DON'T: Subscribe to all searchParams changes**
```tsx
function ShareButton({ chatId }: { chatId: string }) {
  const searchParams = useSearchParams()

  const handleShare = () => {
    const ref = searchParams.get('ref')
    shareChat(chatId, { ref })
  }

  return <button onClick={handleShare}>Share</button>
}
```

**DO: Read on demand**
```tsx
function ShareButton({ chatId }: { chatId: string }) {
  const handleShare = () => {
    const params = new URLSearchParams(window.location.search)
    const ref = params.get('ref')
    shareChat(chatId, { ref })
  }

  return <button onClick={handleShare}>Share</button>
}
```

### 5.4 Subscribe to Derived State

**DON'T: Re-renders on every pixel**
```tsx
function Sidebar() {
  const width = useWindowWidth() // Updates continuously
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

### 5.5 Use Transitions for Non-Urgent Updates

```tsx
import { startTransition } from 'react'

function ScrollTracker() {
  const [scrollY, setScrollY] = useState(0)
  
  useEffect(() => {
    const handler = () => {
      startTransition(() => setScrollY(window.scrollY))
    }
    window.addEventListener('scroll', handler, { passive: true })
    return () => window.removeEventListener('scroll', handler)
  }, [])
}
```

### 5.6 Narrow Effect Dependencies

**DON'T: Re-runs on any user change**
```tsx
useEffect(() => {
  console.log(user.id)
}, [user])
```

**DO: Re-runs only on id change**
```tsx
useEffect(() => {
  console.log(user.id)
}, [user.id])
```

## 6. Rendering Performance (MEDIUM)

### 6.1 CSS content-visibility for Long Lists

```css
.message-item {
  content-visibility: auto;
  contain-intrinsic-size: 0 80px;
}
```

For 1000 items, browser skips layout/paint for ~990 off-screen items.

### 6.2 Animate SVG Wrapper, Not SVG

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

### 6.3 Prevent Hydration Mismatch Without Flickering

```tsx
function ThemeWrapper({ children }: { children: ReactNode }) {
  return (
    <>
      <div id="theme-wrapper">{children}</div>
      <script
        dangerouslySetInnerHTML={{
          __html: `
            (function() {
              var theme = localStorage.getItem('theme') || 'light';
              document.getElementById('theme-wrapper').className = theme;
            })();
          `,
        }}
      />
    </>
  )
}
```

### 6.4 Use Explicit Conditional Rendering

**DON'T: Renders "0" when count is 0**
```tsx
{count && <Badge>{count}</Badge>}
```

**DO: Renders nothing when count is 0**
```tsx
{count > 0 ? <Badge>{count}</Badge> : null}
```

### 6.5 Hoist Static JSX Elements

**DON'T: Recreates every render**
```tsx
function Container() {
  return <div>{loading && <Skeleton />}</div>
}
```

**DO: Reuses same element**
```tsx
const skeleton = <Skeleton />

function Container() {
  return <div>{loading && skeleton}</div>
}
```
```

### Quality & Process Skills (050-090)

#### 050-tdd-workflow (Always-On) - **INCLUDES BROWSER TESTING**
`.cursor/skills/050-tdd-workflow/SKILL.md` AND `.cursor/rules/050-tdd-workflow.mdc`

**Frontmatter:**
```yaml
---
name: "050-tdd-workflow"
description: "TDD workflow with RED-GREEN-VALIDATE-DEPLOY phases for Next.js"
alwaysApply: true
---
```

**Content:**
```markdown
# TDD Workflow for Next.js

## The Four Phases: RED → GREEN → VALIDATE → DEPLOY

### Phase 1: RED (Write Failing Test)
```bash
npm test -- --testPathPattern="ComponentName" --watch
```
- Write test first
- Verify it fails for the right reason

### Phase 2: GREEN (Make It Pass)
```bash
npm test -- --testPathPattern="ComponentName"
```
- Write minimal code to pass
- No refactoring yet

### Phase 3: VALIDATE (Full Suite)
```bash
npm run lint && npm run typecheck && npm test -- --coverage --watchAll=false
```
- Run full test suite
- Check coverage meets 80% minimum
- Fix any lint/type errors

### Phase 4: DEPLOY & BROWSER TEST (CRITICAL)
```bash
# Start dev server
npm run dev

# Or build and preview production
npm run build && npm run start
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

**When to Skip Browser Testing:**
- Pure utility function changes (no UI impact)
- Type-only changes
- Test file changes only

**When Browser Testing is MANDATORY:**
- Any component changes
- Any styling changes
- Any data fetching changes
- Any routing changes
- Any state management changes

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
```

## Blocking Conditions

**DO NOT mark complete if:**
- Tests are failing
- Lint errors exist
- TypeScript errors exist
- Coverage dropped below 80%
- **Browser shows errors/warnings in console**
- **UI is broken on mobile viewport**
- **Network requests are failing**
```

Include other standard quality skills:
- `060-simplicity-constraints` - Code limits
- `070-session-management` - Checkpoint triggers
- `080-code-review` - Severity levels with React-specific checks
- `090-commit-hygiene` - Atomic commits

### Auto-Attach Skills

#### 100-components (Auto-Attach)
`.cursor/skills/100-components/SKILL.md` AND `.cursor/rules/100-components.mdc`

**Frontmatter:**
```yaml
---
name: "100-components"
description: "React component patterns for Next.js"
globs: ["components/**", "app/**/components/**"]
---
```

**Content includes:**
- Server vs Client component decision tree
- Props interface patterns
- Composition over configuration
- Forward ref patterns
- Compound component patterns

#### 110-app-router (Auto-Attach)
`.cursor/skills/110-app-router/SKILL.md` AND `.cursor/rules/110-app-router.mdc`

**Frontmatter:**
```yaml
---
name: "110-app-router"
description: "Next.js App Router patterns and conventions"
globs: ["app/**"]
---
```

**Content includes:**
- Route segment conventions
- Metadata and SEO patterns
- Loading and error boundaries
- Parallel and intercepting routes
- Route handlers patterns

#### 120-hooks (Auto-Attach)
`.cursor/skills/120-hooks/SKILL.md` AND `.cursor/rules/120-hooks.mdc`

**Frontmatter:**
```yaml
---
name: "120-hooks"
description: "Custom hook patterns following Vercel best practices"
globs: ["lib/hooks/**", "hooks/**"]
---
```

#### 130-server-actions (Auto-Attach)
`.cursor/skills/130-server-actions/SKILL.md` AND `.cursor/rules/130-server-actions.mdc`

**Frontmatter:**
```yaml
---
name: "130-server-actions"
description: "Server Actions patterns for Next.js 14+"
globs: ["lib/actions/**", "app/**/actions/**"]
---
```

**Content includes:**
- Server Action conventions
- Form handling patterns
- Optimistic updates
- Error handling
- Revalidation strategies

#### 140-data-fetching (Auto-Attach)
`.cursor/skills/140-data-fetching/SKILL.md` AND `.cursor/rules/140-data-fetching.mdc`

**Frontmatter:**
```yaml
---
name: "140-data-fetching"
description: "Data fetching patterns - SWR, React.cache, fetch"
globs: ["lib/api/**", "lib/data/**"]
---
```

#### 200-testing (Auto-Attach)
`.cursor/skills/200-testing/SKILL.md` AND `.cursor/rules/200-testing.mdc`

**Frontmatter:**
```yaml
---
name: "200-testing"
description: "Vitest + React Testing Library patterns for Next.js"
globs: ["**/*.test.tsx", "**/*.test.ts", "__tests__/**"]
---
```

**Content includes:**
- Component testing with RSC mocking
- Server Action testing
- API route testing
- Integration testing patterns

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
2. **`.cursor/commands/review-and-refactor.md`** - Review and refactor using Vercel patterns
3. **`.cursor/commands/create-or-refine-tests.md`** - TDD workflow with Vitest
4. **`.cursor/commands/code-review.md`** - Code review with React/Next.js specific checks
5. **`.cursor/commands/check-commit-size.md`** - Commit size thresholds
6. **`.cursor/commands/check-performance.md`** - Validate against Vercel performance patterns
7. **`.cursor/commands/browser-test.md`** - Browser testing checklist (Phase 4 of TDD)

**To generate browser-test command:**
1. Read `user_commands/browser-test-template.md` from this template repo
2. Customize for Next.js (add Server Component checks, Suspense, metadata)
3. Generate as `.cursor/commands/browser-test.md` in the user's project

**`.cursor/commands/check-performance.md`** content:
```markdown
# Check Performance Patterns

Validate code against Vercel Engineering's React Best Practices.

## Checks

### CRITICAL (Must Fix)
- [ ] No sequential awaits for independent operations
- [ ] No barrel file imports (or using optimizePackageImports)
- [ ] Heavy components use dynamic imports
- [ ] Suspense boundaries for async data

### HIGH (Should Fix)
- [ ] Using React.cache() for request deduplication
- [ ] Minimal data passed to client components
- [ ] Parallel component composition
- [ ] SWR/React Query for client data

### MEDIUM (Recommended)
- [ ] Functional setState updates
- [ ] Lazy state initialization
- [ ] Derived state subscriptions
- [ ] content-visibility for long lists

## Commands

```bash
# Check bundle size
npx @next/bundle-analyzer

# Check for barrel imports
grep -r "from 'lucide-react'" --include="*.tsx" --include="*.ts"

# Find sequential awaits
grep -r "await.*\n.*await" --include="*.tsx" --include="*.ts"
```
```

## Tech Assumptions

- Next.js 14+ with App Router
- TypeScript strict mode
- Tailwind CSS (or specified alternative)
- SWR for client-side data (or specified alternative)
- Vitest + React Testing Library

Use MY actual project name, tech choices, and features in all examples.

Start with question #1.
