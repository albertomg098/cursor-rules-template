# Cursor Rules Toolkit

Personal, version-controlled system for generating Cursor IDE rules (skills) and commands across all projects.

## Repository Structure: Two Types of Files

This repository contains two types of files with different purposes:

### 1. `init_*` Files in `user_commands/` (Markdown Prompts)
- **Purpose:** Generate rules (skills) in **OTHER projects**
- **Usage:** Copy/paste into Cursor chat when working on a project
- **Examples:** `setup-project.md`, `init_hexagonal_python.md`, `init_react_frontend.md`
- **Stay as markdown files** - not converted to Cursor commands

### 2. Commands in `.cursor/commands/` (Actual Cursor Commands)
- **Purpose:** Work **ON the template repo itself**
- **Usage:** Type `/command-name` in Cursor chat (e.g., `/add-project-type`)
- **Examples:** `add-project-type.md`, `explore-project-type.md`
- **Automatically update index files** - no manual steps needed

**Key Point:** Commands without `init` prefix are for extending the template repo. They're actual Cursor commands accessible via `/`.

## Understanding Cursor: Rules (Skills) vs Commands

Cursor has two distinct systems:

### Rules (Skills) - `.cursor/skills/<name>/SKILL.md`
**Purpose:** Guide AI behavior when coding

- **User Rules:** Set in Cursor Settings → Rules (apply to ALL projects)
  - Global coding standards
  - Personal preferences
  - Applied on every Cursor prompt
  
- **Project Rules (Skills):** Located in `.cursor/skills/<name>/SKILL.md` (per-project)
  - Each rule is a folder with `SKILL.md` inside
  - Example: `.cursor/skills/test/SKILL.md` creates a rule named "test"
  - Project-specific patterns
  - Architecture guidelines
  - Can auto-attach based on file patterns (via globs) or be always-on

### Commands - `.cursor/commands/<name>.md`
**Purpose:** Reusable prompts/instructions accessible via `/` in chat

- **User Commands:** Set in Cursor Settings → User Commands (available in ALL projects)
  - Accessible via `/` in any project
  - Global workflows
  
- **Project Commands:** Located in `.cursor/commands/<name>.md` (per-project)
  - Example: `.cursor/commands/check.md` creates a command named "check"
  - Project-specific workflows
  - Accessible via `/` only in that project
  - Direct `.md` files (not in folders)

### Discovering Commands and Skills in Cursor

**Commands:**
- Type `/` in Cursor chat to see a list of available commands
- Commands from `.cursor/commands/` appear automatically
- User commands (from Settings) also appear
- You can type `/command-name` directly or select from the list

**Skills (Rules):**
- Skills are **not directly listed** in chat - they activate automatically based on:
  - `alwaysApply: true` → Always active
  - `globs: ["pattern/**"]` → Active when editing matching files
  - Manual reference → You reference them by name when needed
- To see what skills exist in a project, check `.cursor/skills/` directory
- Cursor's AI is aware of all skills and uses them automatically when relevant

**Note:** Cursor's chat interface shows commands (via `/`) but skills work silently in the background based on file patterns and settings.

## Setup

### 1. Set Global User Rules

Copy the global rules to Cursor Settings:

1. Open **Cursor Settings** → **Rules** (or `Ctrl+,` → search "Rules")
2. Open `user_rules/global_rules.md` in this repo
3. Copy **entire contents** of `global_rules.md`
4. Paste into Cursor Settings → Rules
5. Save

These rules apply to **all projects** and include your coding standards and the command to generate project-specific skills.

### 2. Set User Commands (Optional)

The files in `user_commands/` are **markdown prompts** designed to be copied/pasted into Cursor chat. They are NOT Cursor commands.

If you want to create actual Cursor commands accessible via `/`:

1. Open **Cursor Settings** → **User Commands**
2. Create commands that reference the markdown files in `user_commands/`
3. Or simply bookmark the `user_commands/` folder for easy access

**Note:** The current workflow uses copy/paste, which works well. Converting to actual Cursor commands is optional.

## Usage

### New Project

1. **Open your new project** in Cursor
2. **Open Cursor chat** (`Ctrl+L` or `Cmd+L`)
3. **Copy** entire contents of `user_commands/setup-project.md`
4. **Paste** into Cursor chat
5. **Answer the questions:**
   - First question: "What type of project?" (hexagonal-python, sdk-python, streamlit, react-frontend, custom)
   - The command will automatically route to the appropriate specific command
   - Continue answering questions as prompted (interview is detailed - be specific!)
6. **Project skills AND commands are generated:**
   - Skills in `.cursor/skills/<name>/SKILL.md` format
   - Commands in `.cursor/commands/<name>.md` format
7. **Verify:** Check `.cursor/skills/` and `.cursor/commands/` folders

### Existing Project

Same process as new project:

1. Open existing project in Cursor
2. Copy `user_commands/setup-project.md`
3. Paste into chat and follow detailed interview
4. Project skills and commands are generated/updated in `.cursor/skills/` and `.cursor/commands/`

**Note:** Existing skills won't be overwritten unless you explicitly ask to regenerate.

### Adding a Single Skill

**For other projects:**
1. Open your project in Cursor
2. Copy the content from `.cursor/commands/add-skill.md` in the template repo (or create your own project command)
3. Paste into chat
4. Answer questions about what the skill should cover
5. Single skill folder is created: `.cursor/skills/<name>/SKILL.md`

**Note:** The `/add-skill` command in `.cursor/commands/` is for the template repo. For other projects, you can create your own project command or use the markdown prompt.

## Extension

### Understanding Commands vs Prompts

**Important Distinction:**

- **`init_*` commands** (e.g., `setup-project.md`, `init_hexagonal_python.md`):
  - These are **markdown prompts** stored in `user_commands/`
  - Used for generating rules in **OTHER projects** (not the template repo)
  - Copy/paste into Cursor chat when working on a project
  - Stay as markdown files (not Cursor commands)

- **Commands without `init` prefix** (e.g., `add-project-type`, `add-skill`, `explore-project-type`):
  - These are **actual Cursor commands** stored in `.cursor/commands/`
  - Used for working **ON the template repo itself**
  - Accessible via `/` in Cursor chat (e.g., `/add-project-type`)
  - Automatically update index files - no manual steps needed

### Adding a New Project Type

To add support for a new architecture (e.g., Next.js, Vue, Django, JavaScript):

1. **Open this template repo** in Cursor
2. **Type `/add-project-type`** in Cursor chat (or use the command palette)
3. **Answer the interview:**
   - Project type name
   - Typical structure
   - Key layers/components
   - Tech stack
   - Patterns/conventions
   - Interview questions for that type
   - Skills to generate
   - Command filename
   - Router option name
4. **Command automatically:**
   - Creates new `init_<type>.md` file in `user_commands/`
   - Updates `user_commands/README.md` index
   - Updates `user_commands/init_project_rules.md` routing
   - No manual steps required!

### Understanding a Project Type

To explore what a project type includes (structure, skills, patterns):

1. **Open this template repo** in Cursor
2. **Type `/explore-project-type`** in Cursor chat
3. **Specify** which project type to explore (hexagonal-python, sdk-python, streamlit, react-frontend)
4. **Get detailed explanation** of that project type's structure, skills, and patterns

### Updating Global Rules

1. Edit `user_rules/global_rules.md` in this repo
2. Copy updated contents to Cursor Settings → Rules
3. Commit changes to version control

## Architecture

### How It Works

This toolkit uses a **router pattern** with **markdown prompt files**:

1. **Single Entry Point:** `setup-project.md` acts as the main router
2. **Project Type Detection:** Asks user what type of project they have
3. **Internal Routing:** Reads the appropriate specific command file (e.g., `init_hexagonal_python.md`)
4. **Command Execution:** Executes that command's interview and generation logic
5. **Generation:** Creates:
   - **Skills (rules):** `.cursor/skills/<name>/SKILL.md` with project-specific patterns
   - **Commands:** `.cursor/commands/<name>.md` with useful workflow commands

### Why This Structure?

**Separation of Concerns:**
- `user_rules/` = Global rules (copy to Cursor Settings → Rules)
- `user_commands/` = Markdown prompts (copy/paste into chat) - generate skills AND commands
- `.cursor/skills/` = Project skills (rules) generated in target projects
- `.cursor/commands/` = Project commands generated in target projects (workflow helpers)

**Router Pattern:**
- Users only interact with **one prompt** (`setup-project.md`)
- Internal commands are **automatically selected** based on project type
- Easy to add new project types without changing user workflow

**Markdown Prompt Files:**
- Each file in `user_commands/` is a **self-contained prompt** - can be pasted directly into Cursor chat
- Prompts include **complete instructions** for the AI to follow
- **Detailed interview-driven** - asks specific questions one at a time, waits for answers, asks follow-ups if unclear
- **Project-specific** - uses actual project details in generated skills and commands
- **Generates both** - creates skills (rules) AND commands for maximum productivity

**Skill Files (SKILL.md):**
- Generated in target project's `.cursor/skills/<name>/SKILL.md` format
- Each skill is a **folder** with `SKILL.md` inside
- Can include frontmatter to control activation:
  - `alwaysApply: true` = Active on every prompt
  - `globs: ["pattern/**"]` = Auto-attach when editing matching files
  - Neither = Manual reference only
- **Layer-specific** skills auto-attach to matching file patterns
- **Manual skills** provide workflows and checklists

### Directory Structure

```
cursor-rules-toolkit/
├── README.md                    # This file
├── PLAN.md                      # Implementation plan
├── .cursor/
│   ├── skills/                 # Project skills (rules) for THIS repo
│   │   ├── template-core/
│   │   │   └── SKILL.md        # Always-on: core rules for template repo
│   │   └── commands/
│   │       └── SKILL.md        # Auto-attach: rules for editing commands
│   └── commands/               # Cursor commands for THIS repo (accessible via /)
│       ├── add-project-type.md # Add new project type support (auto-updates indexes)
│       ├── add-skill.md        # Add skill to other projects
│       └── explore-project-type.md # Explore project type details
├── user_rules/
│   └── global_rules.md         # Copy to Cursor Settings → Rules
└── user_commands/
    ├── README.md               # Command index
    ├── setup-project.md        # Main entry point (router) - generates skills AND commands
    ├── init_hexagonal_python.md    # Internal: hexagonal Python
    ├── init_sdk_python.md          # Internal: Python SDK
    ├── init_streamlit.md           # Internal: Streamlit
    └── init_react_frontend.md      # Internal: React
```

**Note:** 
- Files in `user_commands/` with `init_` prefix are **markdown prompts** for generating rules in other projects (copy/paste workflow)
- Files in `.cursor/commands/` are **actual Cursor commands** for working on the template repo itself (accessible via `/`)
- Commands in `.cursor/commands/` automatically update index files - no manual steps needed

### Skill Activation

Skills activate based on **frontmatter** in `SKILL.md`:

- **Always-on:** `alwaysApply: true` - Active on every prompt
- **Auto-attach:** `globs: ["pattern/**"]` - Active when editing matching files
- **Manual:** No globs, no alwaysApply - User references when needed

Example `SKILL.md`:
```markdown
---
description: "Domain layer patterns"
globs: ["src/domain/**"]
alwaysApply: false
---

# Domain Layer Patterns

[Skill content]
```

This skill activates automatically when editing files in `src/domain/`.

### Version Control

- **This repo:** Version control your rules and command prompts
- **Generated skills:** Commit `.cursor/skills/` in each project
- **Generated commands:** Commit `.cursor/commands/` in each project (if created)
- **Global rules:** Update `user_rules/global_rules.md` and sync to Cursor Settings → Rules
