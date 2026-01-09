# Command File Standards

When creating or editing files in this repository:

## Two Types of Files

1. **`init_*` files in `user_commands/`** - Markdown prompts for generating rules in OTHER projects
2. **Commands in `.cursor/commands/`** - Actual Cursor commands for working ON the template repo

## Creating/Editing `init_*` Files in `user_commands/`:

## Structure

Every command file should have:

1. **Header:** `# <Command Title>`
2. **Brief description** of what the command does
3. **Interview section** with questions (ONE at a time)
4. **Generation instructions** specifying what to create
5. **Content requirements** for generated files

## Interview Pattern

- Ask **ONE question at a time**
- **Wait for answer** before proceeding
- Questions should be **clear and specific**
- Provide **options** when applicable (e.g., "hexagonal-python, sdk-python, ...")

## Generation Instructions

Be explicit about:
- **What skills to create** (with paths: `.cursor/skills/<name>/SKILL.md`)
- **What content to include** in each skill
- **How to customize** based on user answers
- **What patterns to follow**

## Code Examples

- Use **real code**, not pseudo-code
- Reference **actual libraries** from the tech stack
- Show **complete examples**, not snippets with `...`
- Include **DO/DON'T** patterns where helpful

## Router Commands

For commands that route to others (like `setup-project.md`):
- Clearly specify **which command file to read**
- Explain **how to execute** that command's logic
- Handle **custom/unknown** project types gracefully

## Creating/Editing Commands in `.cursor/commands/`:

For commands that work on the template repo (like `add-project-type.md`):
- Commands are **actual Cursor commands** accessible via `/`
- Must **automatically update index files** (README.md, setup-project.md)
- Include **complete automation** - no manual steps for user
- Use clear, descriptive names (kebab-case)

## Extension Commands

For commands that extend the repo (like `/add-project-type`):
- Generate **complete `init_*` files** in `user_commands/`
- **Automatically update** `user_commands/README.md` index
- **Automatically update** `user_commands/setup-project.md` routing
- Remind user to **test** the new command
