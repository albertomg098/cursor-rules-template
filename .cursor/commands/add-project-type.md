# Add New Project Type

Create a new quick-start command for a project type not yet supported (e.g., Next.js, Vue, Django, JavaScript, etc.).

This will generate a new file in `user_commands/` and automatically update the index files.

## Interview

Ask ONE at a time:

1. **What project type are you adding?** (e.g., "Next.js", "Vue 3", "Django REST", "JavaScript", "Go microservice")

2. **What's the typical project structure?** (describe folder layout - e.g., `app/`, `components/`, `lib/`, etc.)

3. **What are the key architectural layers/components?** (e.g., "pages, components, api routes, middleware, database models")

4. **What's the tech stack?** (list: framework version, language, state management, database, testing framework, styling, etc.)

5. **What are the main patterns/conventions?** (e.g., "server components vs client components", "file-based routing", "API routes in app/api")

6. **What interview questions should the command ask?** (list 3-5 essential questions - e.g., "Project name?", "Has authentication?", "Database type?")

7. **What skills should be generated?** (list skills with their purposes and globs):
   - Always-on skills (project core, language standards) - format: `.cursor/skills/<name>/SKILL.md`
   - Auto-attach skills (layer-specific with globs)
   - Testing skills
   - Manual workflow skills

8. **What should the command filename be?** (e.g., `init_nextjs.md`, `init_vue.md`, `init_javascript.md`)

9. **What option name should appear in the router?** (e.g., "nextjs", "vue", "javascript" - used in `setup-project.md` routing)

## Generate Command File

Create `user_commands/{{filename}}.md` with:

1. **Header:** `# Generate {{Project Type}} Rules`

2. **Brief description:** What this command is for

3. **Interview section:** List the questions from Q6, formatted as "Ask ONE at a time:"

4. **Generate Structure section:** Show the folder structure from Q2

5. **Generate Skills section:** List all skills from Q7 with:
   - Skill name (folder name)
   - Full path format: `.cursor/skills/<name>/SKILL.md`
   - Purpose
   - Glob pattern (if auto-attach)
   - Always-on flag (if applicable)

6. **Skill Content Requirements section:** Remind to use actual project details in examples

7. **Start instruction:** "Start with question #1."

## Automatically Update Index Files

After generating the command file, you MUST:

1. **Update `user_commands/README.md`:**
   - Find the "Quick-Start Commands" table
   - Add a new row with:
     - Command: `{{filename}}`
     - Description: Brief description of the project type
     - Use When: When to use this command

2. **Update `user_commands/setup-project.md`:**
   - Find the "What type of project is this?" question
   - Add the new option: `- \`{{option_name}}\` - {{brief description}}`
   - Also add it to the routing section below

3. **Confirm completion:** Tell me what was updated

## Important Notes

- The command should be self-contained (works when pasted into Cursor)
- Interview should be minimal (3-5 essential questions)
- Skills should be specific to this project type's patterns
- Use real code examples, not generic placeholders
- **All index updates are automatic** - don't ask me to do them manually

Start with question #1.
