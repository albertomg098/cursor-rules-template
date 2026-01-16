# User Rules

Global rules that apply to all your projects. Copy these to **Cursor Settings → Rules** (`Ctrl+,` → search "Rules").

## Rule Files

### `global_rules.md` (Required)
**Always include this file.** Contains:
- Interview standards (how AI should ask questions)
- **TDD-first development** (RED-GREEN-VALIDATE workflow)
- **Simplicity constraints** (20 lines/function, 200 lines/file)
- **Session management principles** (checkpoints, decision logging)
- **Code review expectations** (severity levels, workflow)
- **Commit hygiene** (atomic commits, PR size limits)
- General coding preferences (SOLID, KISS, DRY, test coverage)
- Project setup workflow instructions

### `python_rules.md` (Python Projects)
**Include for Python projects.** Contains:
- Type hints requirements
- **Python-specific TDD workflow** (pytest commands by phase)
- Testing standards (pytest, fixtures, mocking, conftest patterns)
- Code style and structure guidelines
- Async/await patterns and error handling

### `security_rules.md` (Security-Critical Code)
**Include for projects handling sensitive data.** Contains:
- **Client-exposed env var warnings** (VITE_*, NEXT_PUBLIC_*)
- Secrets management (gitignore, .env.example)
- Input validation (SQL injection, XSS prevention)
- Authentication best practices (bcrypt, JWT, rate limiting)
- Pre-commit security check script
- Security checklist for releases

### `react_rules.md` (React Projects)
**Include for React projects.** (Coming soon)

## Setup Instructions

1. **Copy `global_rules.md`** to Cursor Settings → Rules
2. **For Python projects:** Also copy `python_rules.md` and append to Rules
3. **For security-critical projects:** Also copy `security_rules.md` and append to Rules
4. **For React projects:** Also copy `react_rules.md` and append to Rules (when available)

**Note:** You can combine all rule files into a single Rules field in Cursor Settings, or keep them separate if you prefer. The `global_rules.md` should always be included.

## What's New

### TDD-First Development
- Mandatory RED-GREEN-VALIDATE workflow
- Tests must fail before implementation
- Bug fix workflow with test gap analysis
- TDD execution log template for todos

### Simplicity Constraints
- Hard limits: 20 lines/function, 200 lines/file, 3 params max
- Enforcement protocol (check before completing any file)
- Never defer refactoring

### Session Management
- Checkpoint triggers (when to save state)
- Decision logging for architectural choices
- Session file structure for resumability

### Code Review & Commit Hygiene
- Severity levels (Critical/High block commits)
- Size thresholds (≤5 files, ≤200 lines)
- Atomic commit principle

### Security Rules
- Client-exposed env var warnings (CRITICAL!)
- Comprehensive security checklist
- Pre-commit security check script

## Updating Rules

1. Edit the relevant rule file(s) in this repo
2. Copy updated contents to Cursor Settings → Rules
3. Changes apply to all projects automatically

## Quick Reference

| Principle | Limit |
|-----------|-------|
| Lines per function | 20 max |
| Lines per file | 200 max |
| Parameters per function | 3 max |
| Nesting depth | 2 levels max |
| Test coverage | 80% minimum |
| Files per commit | ≤5 (warn at 6-10) |
| Lines per PR | ≤200 (warn at 201-400) |
