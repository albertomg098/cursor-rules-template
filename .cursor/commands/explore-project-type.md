# Explore Project Type

Understand the structure, skills, and patterns for a specific project type in this toolkit.

## Interview

Ask me ONE question:

**Which project type do you want to explore?**
- `hexagonal-python` - Python backend with hexagonal architecture
- `sdk-python` - Python SDK/Library package
- `streamlit` - Streamlit MVP application
- `react-frontend` - React frontend application

Wait for my answer, then proceed.

## Exploration Process

Based on my answer, you must:

1. **Read the corresponding command file** from `user_commands/`:
   - `hexagonal-python` → Read `init_hexagonal_python.md`
   - `sdk-python` → Read `init_sdk_python.md`
   - `streamlit` → Read `init_streamlit.md`
   - `react-frontend` → Read `init_react_frontend.md`

2. **Provide a comprehensive explanation** covering:

   **a) Project Structure:**
   - Show the complete folder structure that would be generated
   - Explain the purpose of each directory
   - Explain the architectural layers and their relationships

   **b) Skills That Would Be Generated:**
   - List all skill folders that would be created (`.cursor/skills/<name>/SKILL.md`)
   - For each skill, explain:
     - Skill name and purpose
     - When it activates (always-on, auto-attach with glob, or manual)
     - What patterns/conventions it enforces
     - Key examples of what it covers

   **c) Key Patterns and Conventions:**
   - Explain the main architectural patterns used
   - Explain coding conventions specific to this project type
   - Explain how layers interact (dependency direction, etc.)
   - Explain testing approaches

   **d) Interview Questions:**
   - List the questions that would be asked when using this command
   - Explain why each question is important
   - Show how answers affect what gets generated

   **e) Example Usage:**
   - Show a sample interview flow with example answers
   - Show what would be generated based on those answers

3. **Format the explanation clearly** with sections, code blocks, and examples.

Start by asking: **"Which project type do you want to explore?"** (with the options listed above)
