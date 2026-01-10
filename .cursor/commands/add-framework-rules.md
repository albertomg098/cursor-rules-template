# Add Framework/Language Global Rules

Create a new framework or language-specific global rule file (e.g., `react_rules.md`, `typescript_rules.md`, `go_rules.md`).

This will generate a new file in `user_rules/` and automatically update `global_rules.md` and `user_rules/README.md` to reference it.

## Interview

**CRITICAL:** Follow interview standards - ONE question at a time, show progress (X/TOTAL), use emojis, wait for answer before proceeding.

Ask ONE at a time:

### Framework/Language Identification

1. **Question 1/12:** 🎯 What framework or language are you adding rules for?
   - Examples: "React", "TypeScript", "Go", "Rust", "Vue", "Next.js", "Django"
   - Wait for answer, then proceed.

### Type System & Language Features

2. **Question 2/12:** 🔍 Type system and language features?
   - Ask: "What are your type system requirements? (TypeScript strict mode, type annotations, etc.)"
   - Ask: "What language version/features do you use? (e.g., ES2022, Python 3.11+, Go 1.21+)"
   - Ask: "Any specific language features you prefer or avoid?"
   - Wait for answer.

### Code Style & Formatting

3. **Question 3/12:** 🎨 Code style and formatting?
   - Ask: "What code style guide do you follow? (PEP 8, Airbnb, Google, etc.)"
   - Ask: "What formatter do you use? (Prettier, Black, gofmt, rustfmt, etc.)"
   - Ask: "Any naming conventions? (camelCase, snake_case, PascalCase, etc.)"
   - Ask: "How do you handle imports/modules? (import order, grouping, etc.)"
   - Wait for answer.

### Patterns & Conventions

4. **Question 4/12:** 🏗️ Key patterns and conventions?
   - Ask: "What architectural patterns do you follow? (e.g., component composition, hooks, functional programming, OOP)"
   - Ask: "Any specific patterns for this framework? (e.g., React hooks, Vue composition API, Go interfaces)"
   - Ask: "How do you organize code? (file structure, component organization, etc.)"
   - Wait for answer.

### Error Handling

5. **Question 5/12:** ⚠️ Error handling approach?
   - Ask: "How do you handle errors? (try/catch, Result types, custom exceptions, error boundaries)"
   - Ask: "Do you use custom error types or classes?"
   - Ask: "How do you handle async errors?"
   - Wait for answer.

### Testing Standards

6. **Question 6/12:** 🧪 Testing framework and approach?
   - Ask: "What testing framework? (Jest, Vitest, pytest, Go testing, etc.)"
   - Ask: "What testing patterns? (unit tests, integration tests, component tests, e2e)"
   - Ask: "How do you mock dependencies? (mocking libraries, test doubles, fixtures)"
   - Ask: "What's your test coverage target? (percentage or 'not specified')"
   - Wait for answer.

### Dependencies & Package Management

7. **Question 7/12:** 📦 Dependencies and package management?
   - Ask: "How do you manage dependencies? (npm, yarn, pnpm, pip, go mod, cargo, etc.)"
   - Ask: "Do you pin versions? (exact versions, ranges, lock files)"
   - Ask: "Any dependency management best practices?"
   - Wait for answer.

### Project Structure

8. **Question 8/12:** 📁 Project structure preferences?
   - Ask: "What folder structure do you prefer? (src/, components/, lib/, etc.)"
   - Ask: "How do you organize files? (by feature, by type, flat structure)"
   - Ask: "Any specific conventions for file naming or organization?"
   - Wait for answer.

### Performance & Optimization

9. **Question 9/12:** ⚡ Performance considerations?
   - Ask: "What performance patterns do you follow? (memoization, code splitting, lazy loading, etc.)"
   - Ask: "How do you profile/debug performance? (tools, techniques)"
   - Ask: "Any optimization best practices?"
   - Wait for answer.

### Documentation

10. **Question 10/12:** 📝 Documentation standards?
    - Ask: "What documentation style? (JSDoc, TSDoc, doc comments, README format)"
    - Ask: "Do you require documentation for functions/classes/components?"
    - Ask: "Any documentation generation tools? (TypeDoc, Sphinx, godoc, etc.)"
    - Wait for answer.

### Additional Standards

11. **Question 11/12:** ✅ Any other important standards or preferences?
    - Ask: "Are there other framework-specific or language-specific standards you want to enforce?"
    - Ask: "Any tools or linters you use? (ESLint, pylint, golangci-lint, clippy, etc.)"
    - Ask: "Any security considerations? (dependency scanning, secure coding practices)"
    - Wait for answer.

### File Naming

12. **Question 12/12:** 📝 What should the rule file be named?
    - Suggest: `{{framework}}_rules.md` or `{{language}}_rules.md` (e.g., `react_rules.md`, `typescript_rules.md`, `go_rules.md`)
    - Confirm the filename with the user
    - Wait for answer.

## Generate Rule File

After collecting all answers, create `user_rules/{{filename}}.md` with:

### File Structure

```markdown
# My Development Standards - {{Framework/Language}}

## Type System
[Type system requirements, language version, features]

## Code Style
[Style guide, formatter, naming conventions, imports]

## Patterns & Conventions
[Architectural patterns, framework-specific patterns, code organization]

## Error Handling
[Error handling approach, custom error types, async errors]

## Testing
[Testing framework, patterns, mocking, coverage]

## Dependencies
[Package management, version pinning, best practices]

## Project Structure
[Folder structure, file organization, naming conventions]

## Performance
[Performance patterns, profiling, optimization]

## Documentation
[Documentation style, requirements, tools]
```

### Content Requirements

Each section MUST:
- Use **bold** for key requirements (e.g., **Use TypeScript strict mode**)
- Include brief explanations after dashes
- Reference actual tools/libraries from the interview
- Be specific to the framework/language
- Use clear, actionable guidelines
- Follow the same format as `python_rules.md`

### Example Sections

**Type System:**
```markdown
## Type System

- **Use TypeScript strict mode** - Enable all strict type checking options
- **Use explicit return types** - All functions must have explicit return type annotations
- **Avoid `any` type** - Use `unknown` or proper types instead
- **Use type inference** - Only when types are obvious from context
```

**Code Style:**
```markdown
## Code Style

- **Follow Airbnb Style Guide** - Use ESLint with Airbnb config
- **Use Prettier** - Automatic code formatting with consistent style
- **Use camelCase** - For variables and functions
- **Use PascalCase** - For components and classes
```

## Update References

After generating the rule file, you MUST update these files:

1. **Update `user_rules/global_rules.md`:**
   - Find the "Framework-Specific Rules" section (near the end of the file)
   - Add a new line: `For {{Framework}} projects, also apply: \`user_rules/{{filename}}\``
   - Example: `For React projects, also apply: \`user_rules/react_rules.md\``
   - Place it in alphabetical order or logical grouping with other framework rules

2. **Update `user_rules/README.md`:**
   - Find the "Rule Files" section
   - Add a new entry BEFORE the "Setup Instructions" section:
     ```markdown
     ### `{{filename}}` ({{Framework}} Projects)
     **Include for {{Framework}} projects.** Contains:
     - [List 3-5 main topics from the generated file, e.g., "Type system requirements", "Component patterns", "Testing standards", "State management"]
     ```
   - Update the "Setup Instructions" section:
     - Add a new numbered step: `**For {{Framework}} projects:** Also copy `{{filename}}` and append to Rules`
     - Place it in logical order with other framework-specific instructions

## Important Notes

- Use the actual framework/language name from Q1 in all examples
- Reference actual tools and libraries mentioned in the interview
- Keep each section focused and concise
- Follow the same structure and style as `python_rules.md`
- Make guidelines specific and actionable
- Use **bold** for requirements, explanations after dashes

Start with question #1.
