# Check Commit Size Command Template

Check current changes against commit size thresholds and suggest actions.

**CRITICAL:** This command helps enforce atomic commits and small PRs. Use it before committing to ensure changes are appropriately sized.

## Step 1: Check Current State

Run these commands to assess the current state:

```bash
# Check files changed (staged)
git diff --cached --stat

# Check files changed (unstaged)
git diff --stat

# Check line counts (staged)
git diff --cached --shortstat

# Check line counts (unstaged)
git diff --shortstat
```

## Step 2: Apply Thresholds

### Size Thresholds

| Metric | 🟢 OK | 🟡 WARN | 🔴 STOP |
|--------|-------|---------|---------|
| Files changed | ≤ 5 | 6-10 | > 10 |
| Lines changed | ≤ 200 | 201-400 | > 400 |
| Time since commit | ≤ 30 min | 30-60 min | > 60 min |

### Evaluate Changes

Based on the output:

```markdown
## Current State

**Files Changed:** X
**Lines Changed:** +X / -X (total: X)
**Status:** 🟢 OK | 🟡 WARN | 🔴 STOP

### Assessment

[Based on thresholds, provide assessment]
```

## Step 3: Output Recommendations

### If 🟢 OK (≤5 files, ≤200 lines)

```markdown
## ✅ Commit Size: OK

Your changes are within recommended limits:
- Files: X/5 (OK)
- Lines: X/200 (OK)

**Recommendation:** Good to commit when ready.

### Before Committing
- [ ] Tests pass
- [ ] Linter passes
- [ ] Type checker passes
- [ ] Commit message describes "why"
```

### If 🟡 WARN (6-10 files, 201-400 lines)

```markdown
## ⚠️ Commit Size: WARNING

Your changes are getting large:
- Files: X/5 (over limit)
- Lines: X/200 (over limit)

**Recommendation:** Consider committing soon. Review if changes can be split.

### Options
1. **Commit now** - If changes are cohesive and related
2. **Split by layer** - Commit domain, then application, then infrastructure
3. **Split by feature** - Commit each feature slice separately

### If Committing Now
Make sure:
- [ ] All changes are related to ONE purpose
- [ ] Commit message is clear and focused
- [ ] Tests pass for all changes
```

### If 🔴 STOP (>10 files, >400 lines)

```markdown
## 🛑 Commit Size: TOO LARGE

Your changes are too large for effective review:
- Files: X (limit: 10)
- Lines: X (limit: 400)

**Recommendation:** STOP and split your changes before continuing.

### Why This Matters

| PR Size | Defect Rate | Review Quality |
|---------|-------------|----------------|
| < 200 lines | 15% | Thorough review |
| 200-400 lines | 23% | Good review |
| > 400 lines | 40%+ | Rubber-stamped |

Large PRs get "LGTM" rubber stamps, not real reviews.

### How to Split

#### Option 1: By Layer (Recommended for Hexagonal)
1. **Commit 1:** Domain entities and exceptions
2. **Commit 2:** Application use cases
3. **Commit 3:** Infrastructure adapters
4. **Commit 4:** API routes / CLI commands
5. **Commit 5:** Tests (or with each layer)

#### Option 2: By Feature Slice
1. **Commit 1:** Create functionality
2. **Commit 2:** Read functionality
3. **Commit 3:** Update functionality
4. **Commit 4:** Delete functionality

#### Option 3: Refactor First
1. **Commit 1:** Refactoring (no behavior change)
2. **Commit 2:** New feature (new behavior)

#### Option 4: By Risk
1. **Commit 1:** Safe changes (formatting, docs, tests)
2. **Commit 2:** Risky changes (business logic, security)

### Interactive Splitting

Would you like me to help split these changes? I can:
- Analyze the changed files
- Suggest logical groupings
- Help stage specific files for separate commits
```

## Step 4: Atomic Commit Check

### The Atomic Commit Rule

**If you need "and" to describe your commit, split it.**

✅ Good commit messages:
- "Add email validation to signup form"
- "Fix null pointer in user service"
- "Refactor payment processing for clarity"

❌ Bad commit messages:
- "Add email validation and fix login bug and update styles"
- "Implement user feature and refactor database"

### Commit Triggers

Any of these = time to commit:
- ✅ Tests just passed after being red (GREEN phase complete)
- ✅ Feature/function complete
- ✅ Refactoring done
- ✅ Bug fixed
- ✅ About to switch context
- ✅ Threshold hit (>5 files or >200 lines)

## Customization Notes

When generating this command for a specific project:

1. **Python/Hexagonal:** Splitting by layer is most natural
   - Domain (entities, value objects, ports, exceptions)
   - Application (use cases, services)
   - Infrastructure (adapters, config)
   - Interfaces (API, CLI)

2. **Frontend:** Splitting by feature is most natural
   - Component + styles
   - State management
   - API integration
   - Tests

3. **SDK:** Splitting by module is most natural
   - Core functionality
   - Public API changes
   - Documentation
   - Tests

Start by running the git commands to check current state.
