# User Rules

Global rules that apply to all your projects. Copy these to **Cursor Settings → Rules** (`Ctrl+,` → search "Rules").

## Rule Files

### `global_rules.md` (Required)
**Always include this file.** Contains:
- Interview standards (how AI should ask questions)
- General coding preferences (SOLID, KISS, DRY, test coverage)
- Project setup workflow instructions

### `python_rules.md` (Python Projects)
**Include for Python projects.** Contains:
- Type hints requirements
- Python-specific patterns (async/await, error handling)
- Testing standards (pytest, fixtures, mocking)
- Code style and structure guidelines

### `react_rules.md` (React Projects)
**Include for React projects.** (Coming soon)

## Setup Instructions

1. **Copy `global_rules.md`** to Cursor Settings → Rules
2. **For Python projects:** Also copy `python_rules.md` and append to Rules
3. **For React projects:** Also copy `react_rules.md` and append to Rules (when available)

**Note:** You can combine all rule files into a single Rules field in Cursor Settings, or keep them separate if you prefer. The general `global_rules.md` should always be included.

## Updating Rules

1. Edit the relevant rule file(s) in this repo
2. Copy updated contents to Cursor Settings → Rules
3. Changes apply to all projects automatically
