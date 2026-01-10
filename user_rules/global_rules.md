# My Development Standards

## Interview Standards (CRITICAL - Apply to ALL Interviews)

**MANDATORY for ALL interviews:**

1. **ONE question at a time** - NEVER ask multiple questions in a single message
2. **Wait for answer** - Always wait for the user's response before asking the next question
3. **Show progress** - Always indicate question number and total: **(X/TOTAL)** format
   - Example: "**Question 3/12:** What's the tech stack?"
4. **Use emojis** - Make questions more engaging and visually appealing:
   - 🏗️ for architecture/structure questions
   - 🛠️ for tech stack/tools questions
   - 📦 for dependencies/packages questions
   - 🎨 for patterns/conventions questions
   - ✅ for confirmation/validation questions
   - 🔍 for exploration/analysis questions
   - 📝 for documentation/questions about content
   - 🚀 for workflow/process questions
   - ⚙️ for configuration/settings questions
   - 🧪 for testing questions
   - 📚 for learning/understanding questions
   - 💡 for suggestions/recommendations
   - 🎯 for goals/objectives questions

**Example format:**
```
**Question 3/12:** 🛠️ What's the tech stack? (language, framework, database, etc.)
```

## When I say "setup cursor rules" or "init project rules":

Interview me with these questions (following the interview standards above):

1. 🏗️ What's the project name and purpose?
2. 🏗️ What's the architecture? (hexagonal, clean, MVC, SDK, frontend, etc.)
3. 🛠️ What's the tech stack? (language, framework, database, etc.)
4. 📦 What external services? (auth, payments, storage, etc.)
5. 🧪 What testing requirements? (coverage %, frameworks)
6. 🎨 Any specific patterns I must follow?

Then generate a complete set of skills in `.cursor/skills/<name>/SKILL.md` format with:
- One core rule (always on) with project overview
- Layer-specific rules (auto-attached by glob)
- Testing rules
- A workflow rule for new features

Use my answers to make the rules SPECIFIC to my project, not generic.

## My default preferences (apply to all code):

- Use type hints everywhere
- Initialize dependencies in constructors (stateless classes)
- SOLID principles
- 80% test coverage minimum
- Update README and tests with any change
- Be concise and direct
- When uncertain, ask clarifying questions before coding
- Prefer practical examples over theory
- Always create complete files, never use placeholders like `# ... rest of code`
