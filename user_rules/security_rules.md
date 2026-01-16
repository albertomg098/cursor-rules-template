# My Development Standards - Security

## Core Principle

**Security is not optional.** Every project must pass security checks before merge. Assume all input is malicious, all secrets will leak if committed, and all dependencies have vulnerabilities.

---

## Client-Exposed Environment Variables (CRITICAL!)

**NEVER put secrets in client-exposed env vars.** These are bundled into the browser and visible to anyone.

### Framework Prefixes

| Framework | Client-Exposed Prefix | Server-Only |
|-----------|----------------------|-------------|
| Vite | `VITE_*` | No prefix |
| Next.js | `NEXT_PUBLIC_*` | No prefix |
| Create React App | `REACT_APP_*` | N/A (no server) |
| Nuxt | `NUXT_PUBLIC_*` | No prefix |

### Examples

```typescript
// ❌ WRONG - Secret exposed to browser bundle!
const apiKey = import.meta.env.VITE_ANTHROPIC_API_KEY;
const dbUrl = import.meta.env.VITE_DATABASE_URL;

// ✅ CORRECT - Only public values client-side
const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

// ✅ CORRECT - Secrets stay server-side only (API routes, server functions)
const apiKey = process.env.ANTHROPIC_API_KEY;
const dbUrl = process.env.DATABASE_URL;
```

### Quick Check

Before deploying, verify in browser devtools → Sources → your bundle:
- Search for secret patterns (sk-, api_key, secret, password)
- If found, you've exposed secrets!

---

## Required Security Setup

### 1. Gitignore (NON-NEGOTIABLE)

Every project must have these in `.gitignore`:

```gitignore
# Environment files - NEVER commit
.env
.env.*
!.env.example

# Secrets
*.pem
*.key
*.p12
*.pfx
credentials.json
secrets.json
*-credentials.json
service-account*.json

# IDE and OS
.idea/
.vscode/settings.json
.DS_Store

# Dependencies
node_modules/
__pycache__/
*.pyc
.venv/
venv/
```

### 2. Environment Variables

**Create `.env.example`** with all required vars (no actual values):

```bash
# .env.example - Copy to .env and fill in values

# Server-side only (NEVER prefix with VITE_ or NEXT_PUBLIC_)
DATABASE_URL=
ANTHROPIC_API_KEY=
STRIPE_SECRET_KEY=
SUPABASE_SERVICE_ROLE_KEY=

# Client-side safe (public, non-sensitive)
VITE_SUPABASE_URL=
VITE_SUPABASE_ANON_KEY=
VITE_STRIPE_PUBLISHABLE_KEY=
```

### 3. Validate Environment at Startup

**TypeScript/Node:**
```typescript
import { z } from 'zod';

const envSchema = z.object({
  DATABASE_URL: z.string().url(),
  ANTHROPIC_API_KEY: z.string().min(1),
  NODE_ENV: z.enum(['development', 'production', 'test']),
});

export const env = envSchema.parse(process.env);
```

**Python:**
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    anthropic_api_key: str
    environment: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()
```

---

## Input Validation (OWASP Top 10)

### 1. SQL Injection Prevention

```typescript
// ❌ BAD - SQL injection vulnerable
const user = await db.query(`SELECT * FROM users WHERE id = ${userId}`);

// ✅ GOOD - Parameterized query
const user = await db.query('SELECT * FROM users WHERE id = $1', [userId]);

// ✅ GOOD - Using ORM (Kysely, Prisma, Drizzle)
const user = await db.selectFrom('users').where('id', '=', userId).execute();
```

```python
# ❌ BAD - SQL injection vulnerable
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# ✅ GOOD - Parameterized query
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# ✅ GOOD - Using ORM (SQLAlchemy)
user = session.query(User).filter(User.id == user_id).first()
```

### 2. XSS Prevention

```typescript
// ❌ BAD - XSS vulnerable
element.innerHTML = userInput;

// ✅ GOOD - Sanitized
import DOMPurify from 'dompurify';
element.innerHTML = DOMPurify.sanitize(userInput);

// ✅ BEST - Use framework's built-in escaping (React does this by default)
return <div>{userInput}</div>;  // Safe in React

// ⚠️ DANGER - Bypasses React's protection
return <div dangerouslySetInnerHTML={{ __html: userInput }} />;  // Avoid!
```

### 3. Validate All External Input

```typescript
// Validate ALL external input with Zod
import { z } from 'zod';

const CreateUserSchema = z.object({
  email: z.string().email().max(255),
  name: z.string().min(1).max(100).regex(/^[a-zA-Z\s]+$/),
  age: z.number().int().min(0).max(150),
});

// In route handler
app.post('/users', async (req, res) => {
  const result = CreateUserSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({ error: result.error });
  }
  // result.data is now typed and validated
});
```

---

## Authentication & Authorization

### Password Hashing

```typescript
import bcrypt from 'bcrypt';

const SALT_ROUNDS = 12;  // Minimum 10, recommended 12+

async function hashPassword(password: string): Promise<string> {
  return bcrypt.hash(password, SALT_ROUNDS);
}

async function verifyPassword(password: string, hash: string): Promise<boolean> {
  return bcrypt.compare(password, hash);
}
```

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)
```

### JWT Best Practices

- Use short expiration (15 min for access tokens)
- Use refresh tokens (7 days) in HttpOnly cookies
- Explicitly specify allowed algorithms
- Never put sensitive data in JWT payload

### Rate Limiting

```typescript
import rateLimit from 'express-rate-limit';

// General rate limit
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,  // 15 minutes
  max: 100,                   // 100 requests per window
});

// Strict limit for auth routes
app.use('/api/auth', rateLimit({
  windowMs: 60 * 1000,  // 1 minute
  max: 5,                // 5 attempts per minute
  message: 'Too many login attempts, please try again later',
}));
```

---

## Pre-Commit Security Check Script

Create `scripts/security-check.sh`:

```bash
#!/bin/bash
set -e

echo "🔒 Running security checks..."

# Check .env is not staged
if git diff --cached --name-only | grep -E '^\.env$|^\.env\.' | grep -v '\.example$'; then
  echo "❌ ERROR: .env file is staged for commit!"
  exit 1
fi

# Check for common secret patterns in staged files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM)
if [ -n "$STAGED_FILES" ]; then
  # Check for hardcoded secrets
  if echo "$STAGED_FILES" | xargs grep -l -E '(password|secret|api_key|apikey|token)\s*[:=]\s*["\047][^"\047]{8,}["\047]' 2>/dev/null; then
    echo "⚠️ WARNING: Possible secrets found in staged files - please verify"
  fi
  
  # Check for VITE_* secrets (common mistake)
  if echo "$STAGED_FILES" | xargs grep -l -E 'VITE_.*SECRET|VITE_.*KEY.*=.*[a-zA-Z0-9]{20,}' 2>/dev/null; then
    echo "❌ ERROR: Secrets in VITE_* env vars are exposed to client!"
    exit 1
  fi
fi

# Dependency audit
if [ -f "package.json" ]; then
  echo "🔍 Checking npm dependencies..."
  npm audit --audit-level=high || echo "⚠️ Warning: npm audit found issues"
fi

if [ -f "pyproject.toml" ] || [ -f "requirements.txt" ]; then
  if command -v safety &> /dev/null; then
    echo "🔍 Checking Python dependencies..."
    safety check || echo "⚠️ Warning: safety found issues"
  fi
fi

echo "✅ Security checks complete!"
```

---

## Security Anti-Patterns (NEVER Do)

- ❌ Secrets in `VITE_*`, `NEXT_PUBLIC_*`, or `REACT_APP_*` env vars
- ❌ Secrets in code or config files committed to git
- ❌ .env files without .gitignore entry
- ❌ String concatenation for SQL queries
- ❌ `dangerouslySetInnerHTML` without sanitization
- ❌ `eval()` or `new Function()` with user input
- ❌ Passwords stored as plain text or weak hash (MD5, SHA1)
- ❌ JWTs with no expiration or very long expiration
- ❌ No rate limiting on authentication endpoints
- ❌ Logging sensitive data (passwords, tokens, PII)
- ❌ Using `*` for CORS origins in production
- ❌ Ignoring npm audit / safety check warnings
- ❌ Disabling SSL/TLS verification

---

## Security Checklist

Run before every release:

### Secrets & Environment
- [ ] No secrets in code (run detect-secrets or grep)
- [ ] .env files in .gitignore
- [ ] .env.example exists with all required vars
- [ ] Environment validated at startup
- [ ] No secrets in client-exposed env vars

### Dependencies
- [ ] npm audit / safety check passes
- [ ] No known vulnerabilities in dependencies
- [ ] Dependencies up to date (Dependabot enabled)

### Input Validation
- [ ] All API inputs validated with schema (Zod/Pydantic)
- [ ] File uploads restricted by type and size
- [ ] Path traversal prevented

### Authentication
- [ ] Passwords hashed with bcrypt (12+ rounds)
- [ ] JWTs use short expiration
- [ ] Rate limiting on auth endpoints
- [ ] Session tokens rotated on login

### Database
- [ ] Parameterized queries only
- [ ] Least privilege database user
- [ ] Connection strings not logged

### Headers & CORS
- [ ] Security headers enabled (helmet)
- [ ] CORS restricted to known origins
- [ ] HTTPS only in production
