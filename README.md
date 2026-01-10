# Cursor Rules Toolkit

> **One-time setup, infinite productivity.** Generate project-specific Cursor IDE rules and commands through an automated interview process.

---

## 🎯 What This Does

**Cursor Rules Toolkit** is a template repository that helps you:

1. **Set up global coding standards** once (copy to Cursor Settings → Rules)
2. **Generate project-specific rules** automatically for any project type
3. **Create reusable commands** that work across all your projects

Instead of manually writing Cursor rules for each project, this toolkit uses an **interview-driven workflow** to generate tailored rules and commands based on your project's architecture, tech stack, and patterns.

### Key Benefits

- ⚡ **Fast setup** - Generate complete rule sets in minutes
- 🎯 **Project-specific** - Rules adapt to your actual architecture and stack
- 🔄 **Consistent patterns** - Enforce standards across all projects
- 🛠️ **Extensible** - Easy to add support for new project types
- 📦 **Self-contained** - Commands work when pasted directly into Cursor chat

---

## 🚀 Quick Start

### One-Time Setup (~10 minutes)

**No cloning needed!** Just copy/paste directly from GitHub. This is a one-time setup that works for all your projects.

1. **Set global rules** (applies to ALL projects)
   - Open `user_rules/global_rules.md` on GitHub
   - Copy entire contents (click "Raw" button for clean copy)
   - Paste into **Cursor Settings → Rules** (`Ctrl+,` → search "Rules")
   - Save

2. **Create global commands** ⚠️ **REQUIRED for router to work**
   
   The files in `user_commands/` are markdown prompts that **MUST be set up as User Commands** in Cursor Settings. This is required because:
   - ✅ You can easily access `setup-project` in any project via `/setup-project`
   - ✅ The router can access the other `init_*.md` files when routing
   - ❌ **Without this, the router will fail** when trying to route to specific project types
   
   **Steps:**
   - Open **Cursor Settings → User Commands** (or `Ctrl+,` → search "User Commands")
   - For each file below, open it on GitHub, copy entire contents, and create a User Command:
     
     **Main Command (Required):**
     - ✅ **Command name:** `setup-project` (or `setup`)
     - ✅ **Content:** Copy from `user_commands/setup-project.md` on GitHub
     - ✅ **Description:** "Generate project-specific Cursor rules and commands"
     
     **Supporting Commands (Required for router):**
     - ✅ **Command name:** `init-hexagonal-python`
        - ✅ **Content:** Copy from `user_commands/init_hexagonal_python.md` on GitHub
     
     - ✅ **Command name:** `init-sdk-python`
        - ✅ **Content:** Copy from `user_commands/init_sdk_python.md` on GitHub
     
     - ✅ **Command name:** `init-streamlit`
        - ✅ **Content:** Copy from `user_commands/init_streamlit.md` on GitHub
     
     - ✅ **Command name:** `init-react-frontend`
        - ✅ **Content:** Copy from `user_commands/init_react_frontend.md` on GitHub
   
   **⚠️ Critical:** The `setup-project` command acts as a router and **requires** these commands to be set up as User Commands. Without them, routing will fail.

**That's it!** Once set up, you can use `/setup-project` in any project. The repo doesn't need to stay accessible - everything is copied to Cursor Settings.

### Use in Your Projects

For **any new or existing project**:

**Option 1: Using Global Command (Recommended)**
1. Open your project in Cursor
2. Open Cursor chat (`Ctrl+L` or `Cmd+L`)
3. Type `/setup-project` (or `/setup` if you named it differently)
4. Answer the interview questions
5. Project-specific rules and commands are generated automatically ✨

**Option 2: Copy/Paste (Fallback)**
1. Open your project in Cursor
2. Open Cursor chat (`Ctrl+L` or `Cmd+L`)
3. Copy contents of `user_commands/setup-project.md` from GitHub
4. Paste into chat and answer the interview questions
5. Project-specific rules and commands are generated automatically ✨

**That's it!** Your project now has tailored Cursor rules and commands.

**Note:** If you haven't set up the global commands (Step 2), the router might not be able to access the `init_*.md` files. Make sure to complete the setup!

---

## 📖 How It Works

### The Workflow

```
┌─────────────────────────────────────────────────────────┐
│  1. One-Time Setup (Do Once)                           │
│     • Copy global_rules.md → Cursor Settings → Rules    │
│     • Set up User Commands (setup-project + init_*.md)  │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  2. For Each Project (Repeat as Needed)                 │
│     • Type /setup-project in Cursor chat                │
│     • Answer interview questions                        │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  3. Generated Output (In YOUR Project)                  │
│     • Skills: .cursor/skills/<name>/SKILL.md           │
│     • Commands: .cursor/commands/<name>.md             │
│     • All customized for your project!                 │
└─────────────────────────────────────────────────────────┘
```

### What Gets Generated (In YOUR Project)

**Skills (Rules)** - `.cursor/skills/<name>/SKILL.md` in YOUR project
- Architecture patterns and guidelines specific to your project
- Layer-specific coding standards
- Auto-activate based on file patterns (via globs)
- Or always-on for core project rules

**Commands** - `.cursor/commands/<name>.md` in YOUR project
- Reusable workflows accessible via `/` in Cursor chat
- Project-specific helpers and checklists
- Custom automation tailored to your project structure
- **Important:** These are generated in YOUR project, not in this template repo
- **Common examples:**
  - `/create-or-refine-tests` (always for Python projects)
  - `/create-use-case`, `/add-entity` (for Hexagonal Python)
  - `/create-github-workflow` (optional, if you want CI/CD)

### Supported Project Types

- **Hexagonal Python** - FastAPI + Airflow backend applications
- **Python SDK** - Library/package development
- **Streamlit** - MVP applications
- **React Frontend** - Production React apps (Vite/Next.js)
- **Custom** - Any other architecture (full interview)

---

## 📁 Repository Structure

```
cursor-rules-template/
├── README.md                    # This file
├── PLAN.md                      # Implementation plan
│
├── user_rules/                  # Global rules (one-time setup)
│   └── global_rules.md          # Copy to Cursor Settings → Rules
│
├── user_commands/               # Templates for generating YOUR project commands
│   ├── README.md                # Command index
│   ├── setup-project.md         # Main entry point (router)
│   ├── init_hexagonal_python.md # Hexagonal Python quick-start
│   ├── init_sdk_python.md       # Python SDK quick-start
│   ├── init_streamlit.md        # Streamlit quick-start
│   ├── init_react_frontend.md   # React quick-start
│   ├── create-or-refine-tests-template.md # Template for test command (auto-generated for Python projects)
│   └── create-github-workflow-template.md # Template for CI/CD workflows (optional)
│
└── .cursor/                     # Commands for THIS template repo (use `/` in this repo)
    ├── commands/                # Template repo commands (NOT project commands)
    │   ├── add-project-type.md  # Add new project type support
    │   ├── modify-project-type.md # Modify/extend existing project type
    │   ├── explore-project-type.md # Understand project types
    │   └── add-skill.md         # Add skill to other projects
    └── skills/                  # Rules for working on this repo
        ├── template-core/       # Core template rules
        └── commands/            # Rules for editing commands
```

### Key Distinctions

| Location | Purpose | Usage |
|----------|---------|-------|
| `user_commands/` | **Templates** for generating project commands | Used by init commands to generate commands in YOUR projects |
| `.cursor/commands/` | Commands for **this template repo only** | Type `/command-name` when working in THIS template repo |
| `user_rules/` | Global rules | Copy to Cursor Settings → Rules (one-time) |

**Important:** Commands in `user_commands/` are TEMPLATES. When you run `/setup-project`, they generate commands in YOUR project's `.cursor/commands/` folder, not in this template repo.

---

## 🎓 Understanding Cursor: Rules vs Commands

Cursor has two distinct systems that work together:

### Rules (Skills) - `.cursor/skills/<name>/SKILL.md`

**Purpose:** Guide AI behavior when coding

- **Global Rules** (Cursor Settings → Rules)
  - Apply to ALL projects
  - Your personal coding standards
  - Active on every Cursor prompt

- **Project Rules** (`.cursor/skills/<name>/SKILL.md`)
  - Per-project patterns and architecture
  - Auto-activate based on file patterns (via globs)
  - Or always-on for core project rules

**Activation:**
- `alwaysApply: true` → Always active
- `globs: ["pattern/**"]` → Active when editing matching files
- Manual → Reference by name when needed

### Commands - `.cursor/commands/<name>.md`

**Purpose:** Reusable prompts accessible via `/` in chat

- **Global Commands** (Cursor Settings → User Commands)
  - Available in ALL projects
  - Type `/` to see list

- **Project Commands** (`.cursor/commands/<name>.md`)
  - Project-specific workflows
  - Type `/command-name` in that project
  - Direct `.md` files (not in folders)

**Discovery:**
- Type `/` in Cursor chat to see available commands
- Commands appear automatically from `.cursor/commands/`
- Skills work silently in the background based on file patterns

---

## 🔧 Usage Guide

### Setting Up a New Project

**Using Global Command (Recommended):**
1. **Open your project** in Cursor
2. **Open Cursor chat** (`Ctrl+L` or `Cmd+L`)
3. **Type `/setup-project`** (or `/setup` if you named it differently)
4. **Answer the interview questions:**
   - First: "What type of project?" (hexagonal-python, sdk-python, streamlit, react-frontend, custom)
   - Command automatically routes to appropriate specific command
   - Continue answering detailed questions
   - AI will ask follow-ups if answers are unclear
5. **Verify:** Check `.cursor/skills/` and `.cursor/commands/` folders

**Using Copy/Paste (If global commands not set up):**
1. **Open your project** in Cursor
2. **Open Cursor chat** (`Ctrl+L` or `Cmd+L`)
3. **Copy** entire contents of `user_commands/setup-project.md` from GitHub
4. **Paste** into Cursor chat
5. Follow same interview process as above

**Note:** Copy/paste works, but the router functionality may be limited. For best results, set up the global commands (Step 2 of Quick Start) so the router can access the `init_*.md` files.

### Setting Up an Existing Project

Same process as new projects. Existing skills won't be overwritten unless you explicitly ask to regenerate.

### Adding a Single Skill to Your Project

1. Open your project in Cursor
2. Copy content from `.cursor/commands/add-skill.md` on GitHub (this is a template repo command, used when working on the template repo)
3. Paste into chat
4. Answer questions about what the skill should cover
5. Single skill folder is created: `.cursor/skills/<name>/SKILL.md` in YOUR project

### Project Commands vs Template Commands

**Template Repo Commands** (`.cursor/commands/` in this repo):
- Used ONLY when working on THIS template repo
- Examples: `/add-project-type`, `/modify-project-type`, `/explore-project-type`, `/add-skill`
- Type `/` in Cursor when working in this template repo to see them

**Project-Generated Commands** (`.cursor/commands/` in YOUR projects):
- Generated automatically when you run `/setup-project` in your project
- Examples: `/create-use-case`, `/add-entity`, `/create-or-refine-tests` (for Python projects)
- Type `/` in Cursor when working in your project to see them
- These are customized for YOUR project structure, package names, and patterns
- **Location:** Generated in YOUR project's `.cursor/commands/` folder, not in this template repo

### Project-Generated Commands

When you run `/setup-project`, several commands are automatically generated in your project's `.cursor/commands/` folder:

**Test Creation Command** (`create-or-refine-tests`) - **Always generated for Python projects**
- Creates, extends, or refines tests following your project's standards
- Follows your project structure (mirrors src/ with unit/integration/e2e folders)
- Uses hierarchical conftest.py files
- Follows initialization strategy for mocking (optional params in constructors)
- Ensures 80% coverage minimum
- Customized for your project type (SDK Python, Hexagonal Python)

**CI/CD Workflow Command** (`create-github-workflow`) - **Optional, only if you want it**
- Creates GitHub Actions workflows in `.github/workflows/`
- Only generated if you mention CI/CD during project setup
- Helps create CI/CD workflows following GitHub Actions best practices

**Other Project-Specific Commands** (varies by project type)
- Hexagonal Python: `/create-use-case`, `/add-entity`, `/create-adapter`, etc.
- SDK Python: Component-specific commands based on your structure
- Generated based on your answers during the interview

---

## 🛠️ Extending This Template

**Note:** This section is only needed if you want to extend or customize the template itself. For regular usage, you don't need to clone the repo.

### Adding a New Project Type

To add support for a new architecture (e.g., Next.js, Vue, Django):

1. **Clone this repo** (only needed for extending the template)
2. **Open the cloned repo** in Cursor
3. **Type `/add-project-type`** in Cursor chat
4. **Answer the interview:**
   - Project type name
   - Typical structure
   - Key layers/components
   - Tech stack
   - Patterns/conventions
   - Interview questions for that type
   - Skills to generate
   - Command filename
   - Router option name
5. **Command automatically:**
   - Creates new `init_<type>.md` file in `user_commands/`
   - Updates `user_commands/README.md` index
   - Updates `user_commands/setup-project.md` routing
   - No manual steps required!

### Modifying or Extending Existing Project Types

To adjust an existing project type to match your standards and architecture:

1. **Clone this repo** (only needed for modifying the template)
2. **Open the cloned repo** in Cursor
3. **Type `/modify-project-type`** in Cursor chat
4. **Select** which project type to modify (e.g., `sdk-python`, `hexagonal-python`)
5. **Answer the interview questions** one by one:
   - Architecture & structure review
   - Patterns & conventions review
   - Skills review
   - Interview questions review
   - Key principles review
6. **Review the modification plan** and confirm changes
7. **Command automatically updates** the `init_*.md` file in `user_commands/`

This is useful when:
- Your architecture differs from the default implementation
- You want to add custom patterns or conventions
- You need different skills or glob patterns
- You want to capture additional context during project setup

### Exploring Existing Project Types

To understand what a project type includes:

1. **Clone this repo** (only needed for exploring)
2. **Open the cloned repo** in Cursor
3. **Type `/explore-project-type`** in Cursor chat
4. **Specify** which project type to explore
5. **Get detailed explanation** of structure, skills, and patterns

### Updating Global Rules

1. **Clone this repo** (only needed for updating)
2. Edit `user_rules/global_rules.md` in the cloned repo
3. Copy updated contents to Cursor Settings → Rules
4. Commit changes to version control (optional)

**Note:** After updating global rules, they apply to all projects automatically.

---

## 🏗️ Architecture

### Router Pattern

This toolkit uses a **router pattern** with **markdown prompt files**:

1. **Single Entry Point:** `setup-project.md` acts as the main router
2. **Project Type Detection:** Asks user what type of project they have
3. **Internal Routing:** Reads the appropriate specific command file
4. **Command Execution:** Executes that command's interview and generation logic
5. **Generation:** Creates skills (rules) AND commands

### Why This Structure?

**Separation of Concerns:**
- `user_rules/` = Global rules (copy to Cursor Settings → Rules)
- `user_commands/` = Markdown prompts that **MUST be set up as User Commands** in Cursor Settings
- `.cursor/skills/` = Project skills (rules) generated in target projects
- `.cursor/commands/` = Project commands generated in target projects

**Important: User Commands Setup Required**

The files in `user_commands/` are markdown prompts that **must be set up as User Commands** in Cursor Settings → User Commands. This is required because:

1. **Router Access:** The `setup-project` command acts as a router and needs to access the `init_*.md` files. Without setting them up as User Commands, the router cannot route properly.

2. **Easy Access:** Setting them up as User Commands allows you to type `/setup-project` in any project instead of copying/pasting.

3. **Reliability:** User Commands are more reliable than copy/paste for the router pattern.

**Markdown Prompt Files:**
- Each file in `user_commands/` is a **self-contained prompt**
- **Must be set up as User Commands** in Cursor Settings (see Quick Start Step 3)
- Can also be copy/pasted directly into Cursor chat (but router might not work)
- Includes **complete instructions** for the AI to follow
- **Interview-driven** - asks specific questions one at a time
- **Project-specific** - uses actual project details in generated skills and commands

**Skill Files (SKILL.md):**
- Generated in target project's `.cursor/skills/<name>/SKILL.md` format
- Each skill is a **folder** with `SKILL.md` inside
- Frontmatter controls activation:
  - `alwaysApply: true` = Active on every prompt
  - `globs: ["pattern/**"]` = Auto-attach when editing matching files
  - Neither = Manual reference only

### Skill Activation Example

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

---

## 📝 Version Control

- **This repo:** Version control your rules and command prompts
- **Generated skills:** Commit `.cursor/skills/` in each project
- **Generated commands:** Commit `.cursor/commands/` in each project
- **Global rules:** Update `user_rules/global_rules.md` and sync to Cursor Settings → Rules

---

## 🤝 Contributing

This is a template repository designed to be customized for your needs. To extend it:

1. Use `/add-project-type` to add new project types
2. Use `/modify-project-type` to adjust existing project types to match your standards
3. Edit `user_rules/global_rules.md` to update your coding standards
4. Create custom commands in `user_commands/` for your workflows
5. Share improvements back to the community if desired

---

## 📚 Additional Resources

- **Command Index:** See `user_commands/README.md` for all available commands
- **Implementation Plan:** See `PLAN.md` for detailed architecture and specifications
- **Cursor Documentation:** [Cursor IDE Docs](https://cursor.sh/docs)

---

## ❓ FAQ

**Q: Do I need to set this up for every project?**  
A: Global rules and commands are set once. For each project, just type `/setup-project` (or use the command) to generate project-specific rules.

**Q: Why do I need to set up User Commands?**  
A: The `setup-project` command acts as a router and needs to access the `init_*.md` files. Setting them up as User Commands ensures the router can find and execute them properly. Without this, the router might fail when trying to route to specific project types.

**Q: Can I just copy/paste instead of setting up commands?**  
A: Yes, but the router functionality might not work properly. The router needs to access other commands, so it's recommended to set them up as User Commands for full functionality.

**Q: Can I modify generated rules?**  
A: Yes! Generated rules are regular files you can edit. They won't be overwritten unless you explicitly regenerate.

**Q: How do I see what commands are available?**  
A: Type `/` in Cursor chat to see all available commands (both global and project-specific).

**Q: How do skills activate?**  
A: Skills activate automatically based on file patterns (globs) or are always-on. Check the frontmatter in each `SKILL.md` file.

**Q: Can I use this with existing projects?**  
A: Absolutely! Just run `/setup-project` (or paste `setup-project.md`) in any existing project to add Cursor rules and commands.

**Q: What commands are generated in my project?**  
A: For Python projects, `/create-or-refine-tests` is always generated. Other commands depend on your project type and answers. CI/CD workflow command is optional and only generated if you want it.

**Q: Where are project commands generated?**  
A: In YOUR project's `.cursor/commands/` folder, not in this template repo. Type `/` in Cursor when working in your project to see them.

---

**Made with ❤️ for the Cursor community**