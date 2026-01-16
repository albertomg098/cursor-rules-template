# Code Review Command Template

Run a code review on the current changes or specified files with severity classification.

**CRITICAL:** This command should be customized based on project type when generated. The examples below are templates - replace with actual project patterns.

## Step 1: Determine Review Scope

Ask ONE question:

**Question 1/2:** 🔍 What should I review?
- `staged` - Review staged changes (git diff --cached)
- `unstaged` - Review all unstaged changes (git diff)
- `file` - Review a specific file (provide path)
- `commit` - Review last commit (git show HEAD)
- `branch` - Review branch diff against main/master

Wait for answer.

## Step 2: Load Project Context

**MUST DO FIRST:** Read project skills/rules to understand:
1. Check `.cursor/skills/` for project rules
2. Load `080-code-review/SKILL.md` for review requirements
3. Load language-specific skills (e.g., `010-python-standards`)
4. Load architecture skills (e.g., `000-project-core`, `100-domain-layer`)

## Step 3: Run Review

### Get Changes to Review

Based on Q1:
```bash
# Staged changes
git diff --cached

# Unstaged changes
git diff

# Specific file
git diff HEAD -- path/to/file

# Last commit
git show HEAD

# Branch diff
git diff main...HEAD
```

### Review Categories

For each changed file, check:

#### 1. Security 🔒
- [ ] No hardcoded secrets
- [ ] No secrets in client-exposed env vars (VITE_*, NEXT_PUBLIC_*)
- [ ] Input validation present
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (sanitized output)
- [ ] Authentication/authorization checks

#### 2. Performance ⚡
- [ ] No N+1 queries
- [ ] No unnecessary loops
- [ ] Efficient algorithms
- [ ] Proper caching where needed
- [ ] No memory leaks

#### 3. Architecture 🏗️
- [ ] Correct dependency direction
- [ ] Layer purity (domain has no infrastructure imports)
- [ ] SOLID principles followed
- [ ] Single responsibility
- [ ] Proper abstraction level

#### 4. Code Quality 📝
- [ ] Type hints present (if required)
- [ ] Docstrings present (if required)
- [ ] Naming conventions followed
- [ ] No code duplication
- [ ] Complexity within limits (20 lines/function, 200 lines/file)

#### 5. Testing 🧪
- [ ] Tests exist for new code
- [ ] Edge cases covered
- [ ] Mocks used appropriately
- [ ] Test coverage maintained (≥80%)

## Step 4: Output Results

### Severity Levels

| Level | Action | Can Commit? |
|-------|--------|-------------|
| 🔴 **Critical** | Must fix immediately | ❌ NO |
| 🟠 **High** | Should fix before commit | ❌ NO |
| 🟡 **Medium** | Fix soon, can commit | ✅ YES |
| 🟢 **Low** | Nice to have | ✅ YES |

### Output Format

For each issue found:

```markdown
### [SEVERITY] Issue Title

**File:** `path/to/file.py:line_number`
**Category:** Security | Performance | Architecture | Code Quality | Testing
**Issue:** Description of the problem
**Impact:** Why this matters
**Fix:** Suggested solution
```

### Summary

```markdown
## Review Summary

**Files Reviewed:** X
**Issues Found:** X (X 🔴, X 🟠, X 🟡, X 🟢)
**Status:** BLOCKED | ADVISORY | CLEAR

### Critical Issues (Must Fix)
1. [Issue 1]
2. [Issue 2]

### High Issues (Should Fix)
1. [Issue 1]

### Medium Issues (Fix Soon)
1. [Issue 1]

### Low Issues (Nice to Have)
1. [Issue 1]
```

## Step 5: Blocking Rules

| Condition | Status | Action |
|-----------|--------|--------|
| Any 🔴 Critical | **BLOCKED** | Fix immediately before commit |
| Any 🟠 High | **BLOCKED** | Fix before commit |
| Only 🟡 Medium | **ADVISORY** | Can commit, create follow-up task |
| Only 🟢 Low | **CLEAR** | Can commit, fix when convenient |

## Customization Notes

When generating this command for a specific project:

1. **Python/Hexagonal:** Add checks for:
   - ABC usage for ports (not Protocol)
   - BaseRegistry pattern usage
   - Domain layer purity
   - Use case structure

2. **React/Frontend:** Add checks for:
   - Component composition
   - Hook rules
   - Prop types/TypeScript
   - Accessibility

3. **SDK/Library:** Add checks for:
   - Public API consistency
   - Backward compatibility
   - Documentation quality
   - Export structure

Start with Question 1.
