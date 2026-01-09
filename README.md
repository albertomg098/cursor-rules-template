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

### One-Time Setup (10 minutes)

**No cloning needed!** Just copy/paste directly from GitHub.

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

**That's it!** Once set up, you can use `/setup-project` in any project. No need to keep the repo accessible.

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

**Note:** If you haven't set up the global commands, the router might not be able to access the `init_*.md` files. Make sure to complete Step 3 of the setup!

---

## 📖 How It Works

### The Workflow

```
┌─────────────────────────────────────────────────────────┐
│  1. One-Time Setup                                       │
│     Copy global_rules.md → Cursor Settings → Rules      │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  2. For Each Project                                     │
│     Paste setup-project.md → Answer questions           │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  3. Generated Output                                     │
│     • Skills (rules) in .cursor/skills/<name>/SKILL.md  │
│     • Commands in .cursor/commands/<name>.md            │
└─────────────────────────────────────────────────────────┘
```

### What Gets Generated

**Skills (Rules)** - `.cursor/skills/<name>/SKILL.md`
- Architecture patterns and guidelines
- Layer-specific coding standards
- Auto-activate based on file patterns (via globs)
- Or always-on for core rules

**Commands** - `.cursor/commands/<name>.md`
- Reusable workflows accessible via `/` in Cursor chat
- Project-specific helpers and checklists
- Custom automation for your project

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
├── user_commands/               # Commands for YOUR projects
│   ├── README.md                # Command index
│   ├── setup-project.md         # Main entry point (router)
│   ├── init_hexagonal_python.md # Hexagonal Python quick-start
│   ├── init_sdk_python.md       # Python SDK quick-start
│   ├── init_streamlit.md        # Streamlit quick-start
│   └── init_react_frontend.md   # React quick-start
│
└── .cursor/                     # Commands for THIS template repo
    ├── commands/                # Extend the template (use `/` in this repo)
    │   ├── add-project-type.md  # Add new project type support
    │   ├── explore-project-type.md # Understand project types
    │   └── add-skill.md         # Add skill to other projects
    └── skills/                  # Rules for working on this repo
        ├── template-core/       # Core template rules
        └── commands/            # Rules for editing commands
```

### Key Distinctions

| Location | Purpose | Usage |
|----------|---------|-------|
| `user_commands/` | Commands for **your projects** | Copy/paste into Cursor chat in your projects |
| `.cursor/commands/` | Commands for **this template repo** | Type `/command-name` when working in this repo |
| `user_rules/` | Global rules | Copy to Cursor Settings → Rules (one-time) |

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

**Using Copy/Paste (If commands not set up):**
1. **Open your project** in Cursor
2. **Open Cursor chat** (`Ctrl+L` or `Cmd+L`)
3. **Copy** entire contents of `user_commands/setup-project.md` from GitHub
4. **Paste** into Cursor chat
5. Follow same interview process as above

**Important:** If you use copy/paste, make sure the router can access the `init_*.md` files. They should be set up as User Commands for the router to work properly.

### Setting Up an Existing Project

Same process as new projects. Existing skills won't be overwritten unless you explicitly ask to regenerate.

### Adding a Single Skill

1. Open your project in Cursor
2. Copy content from `.cursor/commands/add-skill.md` on GitHub
3. Paste into chat
4. Answer questions about what the skill should cover
5. Single skill folder is created: `.cursor/skills/<name>/SKILL.md`

---

## 🛠️ Extending This Template

**Note:** This section is only needed if you want to extend or customize the template itself. For regular usage, you don't need to clone the repo.

### Adding a New Project Type

To add support for a new architecture (e.g., Next.js, Vue, Django):

1. **Clone this repo** (only needed for extending the template)
2. **Open the cloned repo** in Cursor
3. **Type `/add-project-type`** in Cursor chat
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
   - Updates `user_commands/setup-project.md` routing
   - No manual steps required!

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
2. Edit `user_rules/global_rules.md` to update your coding standards
3. Create custom commands in `user_commands/` for your workflows
4. Share improvements back to the community if desired

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
A: Absolutely! Just run `setup-project.md` in any existing project to add Cursor rules and commands.

---

**Made with ❤️ for the Cursor community**