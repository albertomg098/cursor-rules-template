# Generate Next.js Fullstack Rules (Vercel Best Practices)

Quick-start for production Next.js fullstack applications with database, authentication, and API routes, following **Vercel Engineering's React Best Practices**.

This builds on top of `init-nextjs-frontend` and adds:
- Database layer (Prisma, Drizzle, or other ORMs)
- Authentication patterns
- API route design
- Server Actions with database operations
- Background jobs and cron
- Deployment and environment configuration

## Interview

**CRITICAL:** Follow interview standards - ONE question at a time, show progress (X/TOTAL), use emojis, wait for answer before proceeding.

Ask ONE at a time:

1. **Question 1/10:** 📦 Project name? (e.g., "saas-platform", "e-commerce-app")

2. **Question 2/10:** 🏗️ Next.js version and router?
   - Next.js 14+ with App Router (recommended)
   - Next.js 13 with App Router

3. **Question 3/10:** 🗄️ Database and ORM?
   - PostgreSQL + Prisma (recommended)
   - PostgreSQL + Drizzle
   - MySQL + Prisma
   - MongoDB + Mongoose
   - Supabase (PostgreSQL + built-in auth)
   - PlanetScale (MySQL)
   - Neon (PostgreSQL)
   - Other (specify)

4. **Question 4/10:** 🔐 Authentication approach?
   - NextAuth.js / Auth.js (OAuth + credentials)
   - Clerk (managed auth + components)
   - Supabase Auth
   - Lucia Auth
   - Custom JWT implementation
   - None (API-only backend)

5. **Question 5/10:** ⚙️ State management for client?
   - Server-first (React Server Components + minimal client state)
   - Zustand for global client state
   - Jotai for atomic state
   - Redux Toolkit

6. **Question 6/10:** 📦 Data fetching and caching?
   - SWR (client-side)
   - React Query / TanStack Query
   - Server Actions + RSC only
   - tRPC (end-to-end typesafe)

7. **Question 7/10:** 🎨 Styling solution?
   - Tailwind CSS (recommended)
   - CSS Modules
   - styled-components

8. **Question 8/10:** 📧 External services needed?
   - Email (Resend, SendGrid, Postmark)
   - File storage (S3, Cloudflare R2, Uploadthing)
   - Payments (Stripe, Lemon Squeezy)
   - Background jobs (Inngest, Trigger.dev, QStash)
   - Real-time (Pusher, Ably, Liveblocks)
   - None / specify others

9. **Question 9/10:** 🏢 Main domain entities?
   - What are the core business objects? (e.g., User, Organization, Project, Task)
   - List 3-5 main entities

10. **Question 10/10:** 📊 Key features to implement?
    - Multi-tenancy (organizations/workspaces)
    - Role-based access control (RBAC)
    - Subscription/billing
    - Admin dashboard
    - API for external integrations
    - Webhooks
    - Other (specify)

## Check for Existing Files

**CRITICAL:** Before generating any files, check for existing skills and commands.

1. Check `.cursor/skills/` and `.cursor/commands/` directories
2. Show user what exists
3. Ask how to handle: `overwrite`, `refine`, `skip`, or `selective`
4. Apply chosen strategy

## Generate Structure

```
app/
├── (auth)/                     # Auth route group
│   ├── login/page.tsx
│   ├── register/page.tsx
│   └── layout.tsx
├── (dashboard)/                # Protected dashboard
│   ├── layout.tsx              # Auth check, sidebar
│   ├── page.tsx                # Dashboard home
│   ├── [entity]/               # Entity CRUD pages
│   │   ├── page.tsx            # List
│   │   ├── [id]/page.tsx       # Detail
│   │   └── new/page.tsx        # Create
│   └── settings/
│       └── page.tsx
├── (marketing)/                # Public marketing pages
│   ├── page.tsx                # Landing
│   ├── pricing/page.tsx
│   └── layout.tsx
├── api/                        # API routes
│   ├── auth/[...nextauth]/     # NextAuth (if used)
│   ├── webhooks/               # Webhook handlers
│   └── v1/                     # Versioned API
│       └── [resource]/route.ts
├── layout.tsx                  # Root layout
└── globals.css
components/
├── ui/                         # Shadcn/UI primitives
├── forms/                      # Form components
├── data-tables/                # Data table components
└── layouts/                    # Layout components
lib/
├── actions/                    # Server Actions
│   ├── auth.ts
│   └── [entity].ts
├── db/                         # Database
│   ├── index.ts                # DB client
│   ├── schema.ts               # Schema (Drizzle) or reference
│   └── queries/                # Query functions
├── auth/                       # Auth utilities
│   ├── config.ts
│   └── session.ts
├── api/                        # API client
├── hooks/                      # Custom hooks
├── stores/                     # Zustand stores
├── utils/                      # Utilities
└── validations/                # Zod schemas
prisma/                         # Prisma (if used)
├── schema.prisma
└── migrations/
types/
└── index.ts
```

## Generate Skills and Rules

**CRITICAL:** Generate BOTH formats:
1. `.cursor/skills/<name>/SKILL.md`
2. `.cursor/rules/<name>.mdc`

### Always-On Skills

#### 000-project-core (Always-On)
**Frontmatter:**
```yaml
---
name: "000-project-core"
description: "Next.js Fullstack architecture, domain, and conventions"
alwaysApply: true
---
```

**Content MUST include:**
```markdown
# Next.js Fullstack Project Core

## Project Context

- **Project Name:** {{project_name}}
- **Purpose:** {{description}}
- **Tech Stack:** 
  - Framework: Next.js {{version}} with App Router
  - Database: {{database}} with {{orm}}
  - Authentication: {{auth_approach}}
  - State: {{state_management}}
  - Data Fetching: {{data_fetching}}
  - Styling: {{styling}}
- **Domain Entities:** {{entities from Q9}}
- **Key Features:** {{features from Q10}}

## Architecture Principles

### Layered Architecture
1. **Presentation Layer** (`app/`, `components/`)
   - React Server Components by default
   - Client components only when needed
   - Server Actions for mutations

2. **Application Layer** (`lib/actions/`, `lib/api/`)
   - Server Actions for form mutations
   - API routes for external access
   - Business logic orchestration

3. **Domain Layer** (`lib/db/queries/`, `types/`)
   - Query functions with React.cache()
   - Domain types and interfaces
   - Validation schemas

4. **Infrastructure Layer** (`lib/db/`, `lib/auth/`, `lib/services/`)
   - Database client and schema
   - Auth configuration
   - External service integrations

### Data Flow
```
Client Request
    ↓
Route Handler / Server Component / Server Action
    ↓
Application Logic (lib/actions/ or lib/api/)
    ↓
Query Functions (lib/db/queries/) + React.cache()
    ↓
Database (Prisma/Drizzle)
```

## Conventions

### File Naming
- Components: `PascalCase.tsx`
- Server Actions: `kebab-case.ts` (e.g., `create-user.ts`)
- Query functions: `camelCase.ts` (e.g., `getUser.ts`)
- API routes: `route.ts` in appropriate folder

### Entity Pattern
For each entity, create:
- `lib/db/queries/[entity].ts` - Query functions
- `lib/actions/[entity].ts` - Server Actions
- `lib/validations/[entity].ts` - Zod schemas
- `types/[entity].ts` - TypeScript types
- `app/(dashboard)/[entity]/` - CRUD pages
```

#### 010-typescript (Always-On)
Standard TypeScript with Prisma/Drizzle types

#### 020-vercel-performance-critical (Always-On)
Same as frontend - CRITICAL patterns for waterfalls and bundle

#### 025-database-patterns (Always-On)
`.cursor/skills/025-database-patterns/SKILL.md` AND `.cursor/rules/025-database-patterns.mdc`

**Frontmatter:**
```yaml
---
name: "025-database-patterns"
description: "Database query patterns with performance optimization"
alwaysApply: true
---
```

**Content:**
```markdown
# Database Patterns

## Query Deduplication with React.cache()

**CRITICAL:** Wrap all query functions with React.cache() for per-request deduplication.

```tsx
import { cache } from 'react'
import { db } from '@/lib/db'

export const getUser = cache(async (id: string) => {
  return db.user.findUnique({
    where: { id },
    select: {
      id: true,
      name: true,
      email: true,
      // Only select needed fields
    }
  })
})

// Multiple calls in one request = single DB query
```

## N+1 Query Prevention

**DON'T: N+1 queries**
```tsx
const users = await db.user.findMany()
for (const user of users) {
  const posts = await db.post.findMany({ where: { authorId: user.id } })
  // N additional queries!
}
```

**DO: Include relations**
```tsx
const users = await db.user.findMany({
  include: {
    posts: true
  }
})
```

## Parallel Queries

**DON'T: Sequential**
```tsx
const user = await getUser(id)
const projects = await getProjects(id)
const notifications = await getNotifications(id)
```

**DO: Parallel with Promise.all**
```tsx
const [user, projects, notifications] = await Promise.all([
  getUser(id),
  getProjects(id),
  getNotifications(id)
])
```

## Transaction Patterns

```tsx
// Prisma
await db.$transaction(async (tx) => {
  const user = await tx.user.create({ data: userData })
  await tx.profile.create({ 
    data: { ...profileData, userId: user.id } 
  })
  return user
})

// Drizzle
await db.transaction(async (tx) => {
  const [user] = await tx.insert(users).values(userData).returning()
  await tx.insert(profiles).values({ ...profileData, userId: user.id })
  return user
})
```

## Select Only What You Need

**DON'T: Select all columns**
```tsx
const user = await db.user.findUnique({ where: { id } })
// Returns all 50 fields
```

**DO: Select specific fields**
```tsx
const user = await db.user.findUnique({
  where: { id },
  select: {
    id: true,
    name: true,
    email: true
  }
})
```
```

#### 030-vercel-performance-high (Always-On)
Same as frontend

#### 035-auth-patterns (Always-On)
`.cursor/skills/035-auth-patterns/SKILL.md` AND `.cursor/rules/035-auth-patterns.mdc`

**Frontmatter:**
```yaml
---
name: "035-auth-patterns"
description: "Authentication and authorization patterns"
alwaysApply: true
---
```

**Content varies by auth choice (NextAuth, Clerk, Supabase, etc.)**

```markdown
# Authentication Patterns

## Session Retrieval (Cached)

```tsx
import { cache } from 'react'
import { auth } from '@/lib/auth/config'

export const getCurrentSession = cache(async () => {
  return auth()
})

export const getCurrentUser = cache(async () => {
  const session = await getCurrentSession()
  if (!session?.user?.id) return null
  
  return db.user.findUnique({
    where: { id: session.user.id },
    select: { id: true, name: true, email: true, role: true }
  })
})
```

## Route Protection

### Server Component Protection
```tsx
import { redirect } from 'next/navigation'
import { getCurrentUser } from '@/lib/auth/session'

export default async function ProtectedPage() {
  const user = await getCurrentUser()
  
  if (!user) {
    redirect('/login')
  }
  
  return <Dashboard user={user} />
}
```

### Middleware Protection
```tsx
// middleware.ts
import { auth } from '@/lib/auth/config'

export default auth((req) => {
  const isLoggedIn = !!req.auth
  const isProtected = req.nextUrl.pathname.startsWith('/dashboard')
  
  if (isProtected && !isLoggedIn) {
    return Response.redirect(new URL('/login', req.url))
  }
})

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)']
}
```

## Role-Based Access Control

```tsx
type Role = 'admin' | 'member' | 'viewer'

const permissions = {
  admin: ['read', 'write', 'delete', 'manage'],
  member: ['read', 'write'],
  viewer: ['read']
} as const

export function hasPermission(
  userRole: Role,
  permission: string
): boolean {
  return permissions[userRole]?.includes(permission) ?? false
}

// Usage in Server Action
export async function deleteProject(id: string) {
  const user = await getCurrentUser()
  if (!hasPermission(user.role, 'delete')) {
    throw new Error('Unauthorized')
  }
  // ...
}
```
```

#### 040-vercel-performance-medium (Always-On)
Same as frontend

#### 050-tdd-workflow (Always-On) - **INCLUDES BROWSER TESTING**
`.cursor/skills/050-tdd-workflow/SKILL.md` AND `.cursor/rules/050-tdd-workflow.mdc`

**Frontmatter:**
```yaml
---
name: "050-tdd-workflow"
description: "TDD workflow with RED-GREEN-VALIDATE-DEPLOY phases for Next.js Fullstack"
alwaysApply: true
---
```

**Content:**
```markdown
# TDD Workflow for Next.js Fullstack

## The Four Phases: RED → GREEN → VALIDATE → DEPLOY

### Phase 1: RED (Write Failing Test)
```bash
npm test -- --testPathPattern="ComponentName" --watch
```
- Write test first (component, server action, or API route)
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
# Start dev server with database
npm run dev

# Or build and test production
npm run build && npm run start
```

**Browser Testing Checklist:**
- [ ] Navigate to changed pages/components
- [ ] Test on desktop AND mobile viewport (use DevTools)
- [ ] Check console for errors/warnings
- [ ] Verify network requests in DevTools (no failed requests)
- [ ] Test user interactions (clicks, forms, navigation)
- [ ] Check loading states and error states
- [ ] Verify responsive layout at breakpoints
- [ ] Test with slow network (DevTools → Network → Slow 3G)

**Fullstack-Specific Checks:**
- [ ] Server Actions execute correctly (check Network tab for POST to same URL)
- [ ] Database operations work (create, read, update, delete)
- [ ] Authentication flow works (login, logout, protected routes)
- [ ] Form validation errors display correctly
- [ ] Optimistic updates work and revert on error
- [ ] Revalidation after mutations updates UI

**When to Skip Browser Testing:**
- Pure utility function changes (no UI/DB impact)
- Type-only changes
- Test file changes only
- Database migration only (test with DB client instead)

**When Browser Testing is MANDATORY:**
- Any component changes
- Any Server Action changes
- Any API route changes
- Any database query changes
- Any authentication changes
- Any form changes

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
  - Server Actions: working
  - Database ops: verified
```

## Blocking Conditions

**DO NOT mark complete if:**
- Tests are failing
- Lint errors exist
- TypeScript errors exist
- Coverage dropped below 80%
- **Browser shows errors/warnings in console**
- **UI is broken on mobile viewport**
- **Server Actions are failing**
- **Database operations are failing**
- **Authentication is broken**
```

Standard quality skills (also generate):
- `060-simplicity-constraints`
- `070-session-management`
- `080-code-review`
- `090-commit-hygiene`

### Auto-Attach Skills

#### 100-components
Same as frontend

#### 110-app-router
Same as frontend

#### 115-api-routes (Auto-Attach)
`.cursor/skills/115-api-routes/SKILL.md` AND `.cursor/rules/115-api-routes.mdc`

**Frontmatter:**
```yaml
---
name: "115-api-routes"
description: "API route patterns for Next.js"
globs: ["app/api/**"]
---
```

**Content:**
```markdown
# API Route Patterns

## Basic Route Handler

```tsx
import { NextRequest, NextResponse } from 'next/server'
import { getCurrentUser } from '@/lib/auth/session'
import { getResource } from '@/lib/db/queries/resource'

export async function GET(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  try {
    const user = await getCurrentUser()
    if (!user) {
      return NextResponse.json(
        { error: 'Unauthorized' },
        { status: 401 }
      )
    }

    const resource = await getResource(params.id)
    if (!resource) {
      return NextResponse.json(
        { error: 'Not found' },
        { status: 404 }
      )
    }

    return NextResponse.json(resource)
  } catch (error) {
    console.error('GET /api/resource/[id]:', error)
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    )
  }
}
```

## Parallel Operations in Routes

```tsx
export async function GET(request: NextRequest) {
  const sessionPromise = getCurrentSession()
  const configPromise = getConfig()
  
  const session = await sessionPromise
  const [config, data] = await Promise.all([
    configPromise,
    fetchData(session.user.id)
  ])
  
  return NextResponse.json({ data, config })
}
```

## Non-Blocking Operations with after()

```tsx
import { after } from 'next/server'

export async function POST(request: NextRequest) {
  const data = await request.json()
  const result = await createResource(data)
  
  // Log after response
  after(async () => {
    await logActivity({ action: 'create', resourceId: result.id })
  })
  
  return NextResponse.json(result, { status: 201 })
}
```

## Webhook Handlers

```tsx
// app/api/webhooks/stripe/route.ts
import { headers } from 'next/headers'
import Stripe from 'stripe'

export async function POST(request: NextRequest) {
  const body = await request.text()
  const signature = headers().get('stripe-signature')!
  
  let event: Stripe.Event
  try {
    event = stripe.webhooks.constructEvent(
      body,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET!
    )
  } catch (err) {
    return NextResponse.json(
      { error: 'Invalid signature' },
      { status: 400 }
    )
  }
  
  // Handle event
  switch (event.type) {
    case 'checkout.session.completed':
      await handleCheckoutComplete(event.data.object)
      break
    // ...
  }
  
  return NextResponse.json({ received: true })
}
```
```

#### 120-hooks
Same as frontend

#### 130-server-actions (Auto-Attach)
`.cursor/skills/130-server-actions/SKILL.md` AND `.cursor/rules/130-server-actions.mdc`

**Frontmatter:**
```yaml
---
name: "130-server-actions"
description: "Server Actions patterns with database operations"
globs: ["lib/actions/**", "app/**/actions/**"]
---
```

**Content:**
```markdown
# Server Actions Patterns

## Action Result Type

```tsx
type ActionResult<T> = 
  | { success: true; data: T }
  | { success: false; error: string }
```

## Basic CRUD Actions

```tsx
'use server'

import { revalidatePath } from 'next/cache'
import { redirect } from 'next/navigation'
import { z } from 'zod'
import { getCurrentUser } from '@/lib/auth/session'
import { db } from '@/lib/db'

const CreateProjectSchema = z.object({
  name: z.string().min(1).max(100),
  description: z.string().optional()
})

export async function createProject(
  formData: FormData
): Promise<ActionResult<{ id: string }>> {
  const user = await getCurrentUser()
  if (!user) {
    return { success: false, error: 'Unauthorized' }
  }

  const parsed = CreateProjectSchema.safeParse({
    name: formData.get('name'),
    description: formData.get('description')
  })

  if (!parsed.success) {
    return { success: false, error: parsed.error.message }
  }

  try {
    const project = await db.project.create({
      data: {
        ...parsed.data,
        ownerId: user.id
      }
    })

    revalidatePath('/dashboard/projects')
    return { success: true, data: { id: project.id } }
  } catch (error) {
    console.error('createProject:', error)
    return { success: false, error: 'Failed to create project' }
  }
}
```

## Optimistic Updates

```tsx
'use client'

import { useOptimistic } from 'react'
import { toggleLike } from '@/lib/actions/posts'

function LikeButton({ postId, isLiked }: Props) {
  const [optimisticLiked, setOptimisticLiked] = useOptimistic(isLiked)

  async function handleClick() {
    setOptimisticLiked(!optimisticLiked)
    await toggleLike(postId)
  }

  return (
    <button onClick={handleClick}>
      {optimisticLiked ? '❤️' : '🤍'}
    </button>
  )
}
```

## With useFormState

```tsx
'use client'

import { useFormState, useFormStatus } from 'react-dom'
import { createProject } from '@/lib/actions/projects'

function SubmitButton() {
  const { pending } = useFormStatus()
  return (
    <button type="submit" disabled={pending}>
      {pending ? 'Creating...' : 'Create Project'}
    </button>
  )
}

export function CreateProjectForm() {
  const [state, formAction] = useFormState(createProject, null)

  return (
    <form action={formAction}>
      <input name="name" placeholder="Project name" />
      {state?.error && <p className="text-red-500">{state.error}</p>}
      <SubmitButton />
    </form>
  )
}
```
```

#### 140-db-queries (Auto-Attach)
`.cursor/skills/140-db-queries/SKILL.md` AND `.cursor/rules/140-db-queries.mdc`

**Frontmatter:**
```yaml
---
name: "140-db-queries"
description: "Database query patterns with React.cache()"
globs: ["lib/db/**", "prisma/**"]
---
```

#### 200-testing (Auto-Attach)
Include patterns for:
- Server Action testing
- API route testing
- Database mocking
- Auth mocking

### Session Management Structure

Create:
```bash
mkdir -p _project_specs/session/archive
```

## Generate Commands

**ALWAYS generate these commands:**

1. **`.cursor/commands/build-project.md`** - Build complete fullstack structure
2. **`.cursor/commands/review-and-refactor.md`** - Review with database/auth patterns
3. **`.cursor/commands/create-or-refine-tests.md`** - TDD with DB mocking
4. **`.cursor/commands/code-review.md`** - Include security checks
5. **`.cursor/commands/check-commit-size.md`**
6. **`.cursor/commands/check-performance.md`** - Vercel patterns validation
7. **`.cursor/commands/create-entity.md`** - Generate entity CRUD
8. **`.cursor/commands/browser-test.md`** - Browser testing checklist (Phase 4 of TDD)
   - Read `user_commands/browser-test-template.md`
   - Customize for fullstack (Server Actions, DB ops, auth flow)

**`.cursor/commands/create-entity.md`** content:
```markdown
# Create Entity

Generate complete CRUD for a new entity.

## Questions

1. Entity name? (e.g., "Project", "Task")
2. Fields? (name: string, status: enum, etc.)
3. Relations? (belongs to User, has many Tasks)
4. Features needed? (soft delete, timestamps, audit log)

## Generate

For entity `{{Entity}}`:

1. **Database Schema** (Prisma/Drizzle)
   - `prisma/schema.prisma` or `lib/db/schema.ts`
   - Add model with fields and relations

2. **Types**
   - `types/{{entity}}.ts`
   - Entity type, CreateInput, UpdateInput

3. **Validations**
   - `lib/validations/{{entity}}.ts`
   - Zod schemas for create/update

4. **Query Functions**
   - `lib/db/queries/{{entity}}.ts`
   - get{{Entity}}, get{{Entity}}s, with React.cache()

5. **Server Actions**
   - `lib/actions/{{entity}}.ts`
   - create, update, delete actions

6. **Pages**
   - `app/(dashboard)/{{entities}}/page.tsx` - List
   - `app/(dashboard)/{{entities}}/[id]/page.tsx` - Detail
   - `app/(dashboard)/{{entities}}/new/page.tsx` - Create
   - `app/(dashboard)/{{entities}}/[id]/edit/page.tsx` - Edit

7. **Components**
   - `components/features/{{entity}}/{{Entity}}Card.tsx`
   - `components/features/{{entity}}/{{Entity}}Form.tsx`
   - `components/features/{{entity}}/{{Entity}}Table.tsx`

8. **Tests**
   - `__tests__/actions/{{entity}}.test.ts`
   - `__tests__/components/{{Entity}}Form.test.tsx`
```

## Tech Assumptions

- Next.js 14+ with App Router
- PostgreSQL + Prisma (or specified alternative)
- NextAuth.js or Clerk (or specified alternative)
- TypeScript strict mode
- Tailwind CSS
- Vitest + React Testing Library

Use MY actual project name, entities, and tech choices in all examples.

Start with question #1.
