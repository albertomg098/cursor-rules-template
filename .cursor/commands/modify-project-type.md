# Modify or Extend Project Type

Review and modify an existing project type command to match your standards and architecture patterns.

This command will:
1. Explore the current implementation using `/explore-project-type`
2. Interview you to check if it matches your standards
3. Plan modifications if needed
4. Update the command file accordingly

## Interview

**CRITICAL:** Follow interview standards - ONE question at a time, show progress (X/TOTAL), use emojis, wait for answer before proceeding.

### Phase 1: Select Project Type

1. **Question 1/12:** 🎯 Which project type do you want to modify or extend?
   - `hexagonal-python` - Python backend with hexagonal architecture
   - `sdk-python` - Python SDK/Library package
   - `streamlit` - Streamlit MVP application
   - `react-frontend` - React frontend application
   
   Wait for answer, then proceed to Phase 2.

### Phase 2: Explore Current Implementation

2. **Question 2/12:** 🔍 Use `/explore-project-type` to get comprehensive information about the selected project type.
   - Read the corresponding `init_*.md` file from `user_commands/`
   - Understand the current structure, skills, patterns, and interview questions
   - Prepare to compare against user's standards

### Phase 3: Architecture & Structure Review

3. **Question 3/12:** 🏗️ Does the project structure match your standards?
   - Show the current structure from the command file
   - Ask: "Does this folder structure match your architecture? If not, what should change?"
   - Wait for answer

4. **Question 4/12:** 🎨 Are the architectural layers/components correct?
   - Show current layers/components
   - Ask: "Do these layers match your architecture? Are any missing or incorrectly named?"
   - Wait for answer

5. **Question 5/12:** 🛠️ Does the tech stack align with your choices?
   - Show current tech stack assumptions
   - Ask: "What tech stack do you use? (framework versions, libraries, tools)"
   - Wait for answer

### Phase 4: Patterns & Conventions Review

6. **Question 6/12:** 🎨 Do the coding patterns match your conventions?
   - Show current patterns from the command
   - Ask: "What coding patterns and conventions do you follow? (e.g., dependency injection, error handling, async patterns)"
   - Wait for answer

7. **Question 7/12:** 🎨 Are the architectural patterns correct?
   - Show current architectural patterns
   - Ask: "What architectural patterns do you use? (e.g., ports/adapters, MVC, clean architecture, etc.)"
   - Wait for answer

### Phase 5: Skills Review

8. **Question 8/12:** 🔍 Do the skills match your needs?
   - Show current skills (always-on, auto-attach, manual)
   - Ask: "Are these skills appropriate? Should any be added, removed, or modified?"
   - Wait for answer

9. **Question 9/12:** ⚙️ Are the skill glob patterns correct?
   - Show current glob patterns for auto-attach skills
   - Ask: "Do these file patterns match your project structure? Should any globs be adjusted?"
   - Wait for answer

### Phase 6: Interview Questions Review

10. **Question 10/12:** 📝 Are the interview questions appropriate?
    - Show current interview questions
    - Ask: "Do these questions capture what you need? Should any be added, removed, or reworded?"
    - Wait for answer

11. **Question 11/12:** 🔍 What additional context should be captured?
    - Ask: "Is there any other information that should be asked during project setup?"
    - Wait for answer

### Phase 7: Key Principles Review

12. **Question 12/12:** 💡 Do the key principles match your standards?
    - Show current principles from the command
    - Ask: "What are your key architectural and coding principles? (e.g., API stability, deprecation policy, testing requirements)"
    - Wait for answer

## Analysis & Planning

After completing all questions:

1. **Summarize findings:**
   - List what matches your standards (keep as-is)
   - List what needs modification
   - List what needs to be added
   - List what should be removed

2. **Create modification plan:**
   - For each change needed, specify:
     - What section to modify (Structure, Skills, Interview, Principles, etc.)
     - What the change is
     - Why it's needed

3. **Ask for confirmation:**
   - "Based on your answers, I've identified X changes needed. Should I proceed with updating the command file?"

## Generate Updated Command File

If confirmed, update `user_commands/init_{{project_type}}.md`:

1. **Update Structure section** (if needed)
   - Modify folder structure based on answers
   - Update directory purposes

2. **Update Skills section** (if needed)
   - Add/remove/modify skills based on answers
   - Update glob patterns
   - Update skill purposes

3. **Update Interview section** (if needed)
   - Add/remove/modify questions
   - Reorder if needed
   - Update question wording

4. **Update Key Principles section** (if needed)
   - Update principles based on answers
   - Add new principles
   - Remove outdated ones

5. **Update Generate Structure section** (if structure changed)
   - Update the structure template

6. **Update Skill Content Requirements** (if skills changed)
   - Update what each skill should cover

## Important Notes

- Compare current implementation against user's actual standards
- Be thorough in identifying mismatches
- Only modify what needs changing - don't rewrite unnecessarily
- Preserve what works well
- Ensure all changes align with user's answers
- Keep the command self-contained and interview-driven

Start with question #1 (Phase 1).