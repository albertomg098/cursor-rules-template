# Add Single Skill to Project

Add a single skill to an existing project's `.cursor/skills/` directory.

**Note:** This command is for adding skills to OTHER projects, not the template repo itself.

## Interview

Ask ONE at a time:

1. **What should this skill cover?** (description - e.g., "API route patterns", "Database migration rules")

2. **When should it activate?**
   - Always (alwaysApply: true)
   - Auto-attach to files matching a glob pattern (provide glob)
   - Manual (no auto-attach, user references it)

3. **If auto-attach, what glob pattern?** (e.g., `src/api/**`, `migrations/**`, `*.test.ts`)

4. **Any specific patterns or examples to include?** (describe key patterns, DO/DON'T examples, or say "use common patterns")

5. **What should the skill be named?** (follow convention: `XXX-description` where XXX is number prefix, e.g., `100-domain-layer`)

## Generate Skill

Create `.cursor/skills/{{name}}/SKILL.md` with:

1. **Create folder:** `.cursor/skills/{{name}}/`
2. **Create file:** `SKILL.md` inside that folder
3. **Frontmatter** (at top of SKILL.md):
   ```yaml
   ---
   description: "{{description from Q1}}"
   globs: ["{{glob from Q3}}"]  # Only if auto-attach
   alwaysApply: true/false      # Based on Q2
   ---
   ```

4. **Content:**
   - Clear title
   - Overview of what this skill enforces
   - Real code examples (DO patterns)
   - Anti-patterns (DON'T patterns)
   - WHY explanations
   - Keep under 200 lines

5. **Naming convention:** Use the name from Q5, following:
   - `000-` for always-on core skills
   - `010-` for always-on language standards
   - `100-` for auto-attach layer skills
   - `200-` for auto-attach testing skills
   - `300-` for auto-attach infrastructure/tooling
   - `900-` for manual workflow skills

Start with question #1.
