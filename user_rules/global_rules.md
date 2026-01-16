# My Development Standards - Global

## Interview Standards (CRITICAL - Apply to ALL Interviews)

**MANDATORY for ALL interviews:**

1. **ONE question at a time** - NEVER ask multiple questions in a single message
2. **Wait for answer** - Always wait for the user's response before asking the next question
3. **Show progress** - Always indicate question number and total: **(X/TOTAL)** format
   - Example: "**Question 3/12:** What's the tech stack?"
4. **Use emojis** - Make questions more engaging and visually appealing:
   - 🏗️ for architecture/structure questions
   - 🛠️ for tech stack/tools questions
   - 📦 for dependencies/packages questions
   - 🎨 for patterns/conventions questions
   - ✅ for confirmation/validation questions
   - 🔍 for exploration/analysis questions
   - 📝 for documentation/questions about content
   - 🚀 for workflow/process questions
   - ⚙️ for configuration/settings questions
   - 🧪 for testing questions
   - 📚 for learning/understanding questions
   - 💡 for suggestions/recommendations
   - 🎯 for goals/objectives questions

**Example format:**
```
**Question 3/12:** 🛠️ What's the tech stack? (language, framework, database, etc.)
```

## When I say "setup cursor rules" or "init project rules":

Interview me with these questions (following the interview standards above):

1. 🏗️ What's the project name and purpose?
2. 🏗️ What's the architecture? (hexagonal, clean, MVC, SDK, frontend, etc.)
3. 🛠️ What's the tech stack? (language, framework, database, etc.)
4. 📦 What external services? (auth, payments, storage, etc.)
5. 🧪 What testing requirements? (coverage %, frameworks)
6. 🎨 Any specific patterns I must follow?

Then generate a complete set of skills in `.cursor/skills/<name>/SKILL.md` format with:
- One core rule (always on) with project overview
- Layer-specific rules (auto-attached by glob)
- Testing rules
- A workflow rule for new features

Use my answers to make the rules SPECIFIC to my project, not generic.

## My default preferences (apply to all code):

- Initialize dependencies in constructors (stateless classes)
- SOLID, KISS, DRY principles
- 80% test coverage minimum
- Update README and tests with any change
- Be concise and direct
- When uncertain, ask clarifying questions before coding
- Prefer practical examples over theory
- Always create complete files, never use placeholders like `# ... rest of code`

---

## TDD-First Development (MANDATORY)

**Philosophy:** No code ships without a test that failed first.

### The TDD Cycle (RED-GREEN-VALIDATE)

```
┌─────────────────────────────────────────────────────────────────┐
│  1. RED: Write Tests First                                      │
│     └─ Create tests based on acceptance criteria                │
│     └─ Run tests → ALL MUST FAIL (proves tests are valid)       │
├─────────────────────────────────────────────────────────────────┤
│  2. GREEN: Implement the Feature                                │
│     └─ Write MINIMUM code to make tests pass                    │
│     └─ Run tests → ALL MUST PASS                                │
├─────────────────────────────────────────────────────────────────┤
│  3. VALIDATE: Quality Gates                                     │
│     └─ Run linter (auto-fix if possible)                        │
│     └─ Run type checker                                         │
│     └─ Run full test suite with coverage                        │
│     └─ Verify coverage threshold (≥80%)                         │
└─────────────────────────────────────────────────────────────────┘
```

### Why Tests Must Fail First

- Proves the test actually validates the requirement
- For bugs: proves the test would have caught it
- Prevents false confidence from tests that always pass
- Ensures you're testing the right thing

### Bug Fix Workflow (TDD-Based)

**NEVER jump to fixing bugs directly.** Follow this workflow:

1. **DIAGNOSE:** Run existing tests - do any fail?
   - If tests pass but bug exists → you have a **test gap**
   - Document: "Test gap: [what was missed]"

2. **RED:** Write a failing test that reproduces the bug
   - Test should FAIL with current code
   - This proves the test catches the bug

3. **GREEN:** Fix the bug with minimum code change
   - Run test → must PASS now

4. **VALIDATE:** Full quality check
   - Run ALL tests (not just the new one)
   - Run linter and type checker
   - Verify no regression in coverage

### TDD Anti-Patterns (NEVER Do)

- ❌ Fixing bugs without adding a test first
- ❌ Writing tests after implementation
- ❌ Marking todos complete with failing tests
- ❌ Skipping lint/typecheck before completion
- ❌ Tests that pass without implementation (invalid tests)

### TDD Execution Log

For todos and PRs, track TDD phases:

| Phase | Command | Result | Timestamp |
|-------|---------|--------|-----------|
| RED | `[test command]` | X tests failed ✓ | - |
| GREEN | `[test command]` | X tests passed ✓ | - |
| VALIDATE | `[full validation]` | Pass, XX% ✓ | - |

---

## Simplicity Constraints (NON-NEGOTIABLE)

**Philosophy:** Complexity is the enemy. Every line of code is a liability. The goal is software simple enough that any engineer (or AI) can understand the entire system in one session.

### Hard Limits

| Constraint | Limit | Action if Exceeded |
|------------|-------|-------------------|
| Lines per function | **20 max** | STOP and decompose immediately |
| Parameters per function | **3 max** | Use options object or decompose |
| Nesting depth | **2 levels max** | Flatten with early returns |
| Lines per file | **200 max** | STOP and split by responsibility |
| Functions per file | **10 max** | Split into multiple files |
| Test coverage | **80% minimum** | CI blocks below threshold |

### Enforcement Protocol

**Before completing ANY file:**
1. Count total lines - if > 200, STOP and split
2. Count functions - if > 10, STOP and split
3. Check each function length - if any > 20 lines, STOP and decompose
4. Check parameter counts - if any > 3, STOP and refactor

**When limits are exceeded:**
```
⚠️ COMPLEXITY VIOLATION DETECTED

[filename] has [X] lines (limit: 200)

Splitting into:
- [filename-a] - [responsibility A]
- [filename-b] - [responsibility B]
```

**Never defer refactoring.** Fix violations immediately, not "later".

### Architectural Patterns

- **Functional core, imperative shell** - Pure functions for business logic, side effects at boundaries
- **Composition over inheritance** - No inheritance deeper than 1 level
- **Dependency injection** - Pass dependencies, don't import them directly
- **Single responsibility** - Each function/class does exactly one thing

---

## Session Management Principles

**Philosophy:** Checkpoint at natural breakpoints, resume instantly.

Long development sessions risk context loss. Proactively document state, decisions, and progress so any session can resume exactly where it left off.

### When to Checkpoint

| Trigger | Action |
|---------|--------|
| After completing any todo | Quick update to current-state.md |
| After ~20 tool calls | Full checkpoint |
| After any architectural decision | Log to decisions.md |
| Major feature complete | Archive session |
| End of session | Archive + handoff |

### Decision Heuristic

After completing work, ask yourself:
- □ Was a decision made? → Log to decisions.md
- □ Did this take >10 tool calls? → Full checkpoint
- □ Is a feature complete? → Archive session
- □ Am I ending/switching context? → Archive + handoff
- □ Otherwise → Quick update

### Session State Structure

```
_project_specs/
└── session/
    ├── current-state.md      # Live state, next steps
    ├── decisions.md          # Key decisions (append-only)
    ├── code-landmarks.md     # Important code locations
    └── archive/              # Past session summaries
```

### Decision Logging

Log decisions when:
- Choosing between architectural approaches
- Selecting libraries or tools
- Making security-related choices
- Deviating from standard patterns

Format:
```markdown
## [YYYY-MM-DD] Decision Title

**Decision**: What was decided
**Context**: Why this decision was needed
**Options**: What alternatives existed
**Choice**: Which option was chosen
**Reasoning**: Why this choice was made
**Trade-offs**: What we gave up
```

---

## Code Review Expectations

**Philosophy:** Every commit must pass code review. No exceptions.

### Severity Levels

| Level | Action | Can Commit? |
|-------|--------|-------------|
| 🔴 **Critical** | Must fix immediately | ❌ NO |
| 🟠 **High** | Should fix before commit | ❌ NO |
| 🟡 **Medium** | Fix soon, can commit | ✅ YES |
| 🟢 **Low** | Nice to have | ✅ YES |

### Review Categories

| Category | What to Check |
|----------|---------------|
| **Security** | Vulnerabilities, injection risks, auth issues, secrets |
| **Performance** | N+1 queries, memory leaks, inefficient algorithms |
| **Architecture** | Design patterns, SOLID principles, coupling |
| **Code Quality** | Readability, complexity, duplication |
| **Testing** | Coverage gaps, test quality, edge cases |

### Code Review Workflow

```
Code → Test → Review → Fix → Commit → Push
              ↑
         Check for:
         - 🔴 Critical issues
         - 🟠 High issues
         - Security concerns
         - Performance issues
```

---

## Commit Hygiene Principles

**Philosophy:** Atomic commits, small PRs, commit early and often.

### Size Thresholds

| Metric | 🟢 OK | 🟡 WARN | 🔴 STOP |
|--------|-------|---------|---------|
| Files changed | ≤ 5 | 6-10 | > 10 files → Commit NOW |
| Lines changed | ≤ 200 | 201-400 | > 400 lines → Commit NOW |
| Time since commit | ≤ 30 min | 30-60 min | > 60 min → Consider committing |

### Atomic Commit Rule

**If you need "and" to describe your commit, split it.**

✅ Good: "Add email validation to signup form"
❌ Bad: "Add email validation and fix login bug and update styles"

### Commit Triggers (Any One = Commit)

- ✅ Tests just passed after being red
- ✅ Feature/function complete
- ✅ Refactoring done
- ✅ Bug fixed
- ✅ About to switch context
- ✅ Threshold hit (>5 files or >200 lines)

### PR Size Impact (Research)

| PR Size | Defect Rate | Review Quality |
|---------|-------------|----------------|
| < 200 lines | 15% | Thorough review |
| 200-400 lines | 23% | Good review |
| > 400 lines | 40%+ | Rubber-stamped |

**Large PRs get "LGTM" rubber stamps, not real reviews.**

### Splitting Large Changes

If changes are too large:
1. **By layer:** Database → API → Frontend
2. **By feature slice:** Create → Read → Update → Delete
3. **Refactor first:** Refactor commit, then feature commit
4. **By risk:** Safe changes separate from risky changes

---

## Code Generation Principles (CRITICAL)

**Minimal Code Approach:**
- **Write the LEAST amount of code possible** to solve the request
- Avoid over-engineering or adding unnecessary abstractions
- Prefer simple, direct solutions over complex patterns unless complexity is required
- Don't add features or code "just in case" - only what's needed for the current request
- If multiple approaches exist, choose the simplest one that meets requirements
- Remove any code that doesn't directly contribute to solving the problem

**Always Test Changes:**
- **MANDATORY:** After making ANY code changes, write or update tests
- Test the specific functionality that was changed
- Ensure existing tests still pass (don't break existing functionality)
- If adding new features, add corresponding tests
- If refactoring, update tests to match the new structure
- Run tests to verify changes work correctly before considering the task complete
- If tests don't exist, create them following project testing patterns

**Workflow:**
1. Understand the request/question
2. **Write tests first** (RED phase)
3. Verify tests fail
4. Write minimal code to pass tests (GREEN phase)
5. Run full validation (VALIDATE phase)
6. Only then consider the task complete

---

## Framework-Specific Rules

For Python projects, also apply: `user_rules/python_rules.md`
For React projects, also apply: `user_rules/react_rules.md` (when available)
For security-critical code, also apply: `user_rules/security_rules.md`
