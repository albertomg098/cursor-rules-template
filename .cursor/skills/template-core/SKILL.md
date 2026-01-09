# Cursor Rules Toolkit - Template Repository Rules

## Repository Purpose

This repository contains:
- **User Rules** (`user_rules/`) - Global instructions to copy to Cursor Settings → Rules
- **Markdown Prompts** (`user_commands/`) - Prompts to copy/paste into chat that generate project-specific skills in `.cursor/skills/<name>/SKILL.md`

**Note:** Files in `user_commands/` are markdown prompts, not Cursor commands. They're designed to be copied/pasted into Cursor chat. Actual Cursor commands would be in `.cursor/commands/<name>.md` if needed.

## Working on This Repo

When editing files in this repository:

### Command Files (`user_commands/*.md`)

- Commands must be **self-contained** - work when pasted directly into Cursor chat
- Include **complete instructions** for the AI to follow
- Use **interview pattern** - ask one question at a time, wait for answers
- Commands should **generate project-specific skills** using actual project details
- Include **real code examples**, not placeholders

### Skill Templates

When commands generate skills, they must:
- Create **folders** `.cursor/skills/<name>/` with `SKILL.md` inside
- Include **real, runnable code examples**
- Reference **actual libraries/frameworks** from the project's tech stack
- Show **DO/DON'T patterns**
- Explain **WHY** behind patterns
- Keep under **200 lines** per skill

### Router Pattern

- `setup-project.md` is the **single entry point**
- It routes to specific commands based on project type
- Generates both skills (rules) AND commands
- When adding new project types:
  1. Create new command file in `user_commands/`
  2. Update `setup-project.md` routing list (or use `/add-project-type` command)
  3. Update `user_commands/README.md` index (or use `/add-project-type` command)

### File Naming Conventions

- Commands: `init_<project_type>.md` or `add_<action>.md`
- Generated skills: `.cursor/skills/<name>/SKILL.md` where name follows convention:
  - `000-project-core` = Always-on core rules
  - `010-language-standards` = Always-on language standards
  - `100-<layer>` = Auto-attach layer rules
  - `200-testing` = Auto-attach testing rules
  - `300-<tool>` = Auto-attach infrastructure/tooling
  - `900-<workflow>` = Manual workflow rules
