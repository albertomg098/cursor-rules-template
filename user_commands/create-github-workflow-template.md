# Create GitHub Actions Workflow

Create or update GitHub Actions workflows in `.github/workflows/` folder.

**CRITICAL:** Follow interview standards - ONE question at a time, show progress (X/TOTAL), use emojis, wait for answer before proceeding.

## Interview

Ask ONE at a time:

1. **Question 1/15:** 🎯 What workflow do you want to create?
   - CI workflow (run tests, lint, build on push/PR)
   - CD workflow (deploy on release/tag)
   - Release workflow (version bump, changelog, publish)
   - Custom workflow (specify purpose)

2. **Question 2/15:** 🔍 Do you want to create a new workflow or update an existing one?
   - Check if `.github/workflows/` folder exists
   - List existing workflow files (if any)
   - Wait for answer

3. **Question 3/15:** ⚙️ What steps should the workflow perform?
   - Examples: "run tests", "lint code", "build package", "deploy", "publish"
   - Wait for answer

4. **Question 4/15:** 🛠️ What Python version should the workflow use? (if Python project)
   - Examples: "3.9", "3.10", "3.11", "3.12", or matrix of versions
   - Wait for answer

5. **Question 5/15:** 🛠️ What OS should the workflow run on?
   - Options: ubuntu-latest, windows-latest, macos-latest, or matrix
   - Wait for answer

6. **Question 6/15:** ⚙️ What triggers should start the workflow?
   - Examples: push, pull_request, release, workflow_dispatch, tags, etc.
   - Wait for answer

7. **Question 7/15:** 🧪 Should the workflow run tests?
   - Wait for answer
   - If yes, follow up with: "What testing framework? (pytest, unittest, etc.)"
   - Wait for answer

8. **Question 8/15:** 🧪 Should the workflow check test coverage?
   - Wait for answer
   - If yes, follow up with: "What coverage threshold? (e.g., 80%, 90%)"
   - Wait for answer

9. **Question 9/15:** ⚙️ How should dependencies be installed?
   - Options: requirements.txt, poetry, pipenv, pip, conda, etc.
   - Wait for answer

10. **Question 10/15:** ✅ Should the workflow run linters?
    - Wait for answer
    - If yes, follow up with: "Which linters? (ruff, black, pylint, mypy, etc.)"
    - Wait for answer

11. **Question 11/15:** ✅ Should the workflow run formatters?
    - Wait for answer
    - If yes, follow up with: "Which formatters? (black, ruff format, etc.)"
    - Wait for answer

12. **Question 12/15:** ✅ Should the workflow fail on linting errors or just warn?
    - Options: fail (stop workflow), warn (continue with warning)
    - Wait for answer

13. **Question 13/15:** 🚀 Should the workflow deploy or publish? (if applicable)
    - Wait for answer
    - If yes, follow up with: "Deploy to where? (production, staging, PyPI, Docker Hub, etc.)"
    - Wait for answer

14. **Question 14/15:** ⚙️ What secrets or environment variables are needed for deployment/publishing?
    - Wait for answer

15. **Question 15/15:** 🚀 What conditions should trigger deployment/publishing?
    - Examples: tags, specific branches, manual dispatch, release events
    - Wait for answer

## Generate Workflow

Based on answers, create `.github/workflows/{{workflow_name}}.yml`:

### Basic Structure

```yaml
name: {{Workflow Name}}

on:
  {{triggers_from_Q6}}

jobs:
  {{job_name}}:
    runs-on: {{os_from_Q5}}
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '{{python_version_from_Q4}}'
      
      - name: Install dependencies
        run: |
          {{install_commands_from_Q9}}
      
      - name: Run tests
        run: |
          {{test_commands_from_Q7}}
      
      - name: Run linters
        run: |
          {{lint_commands_from_Q10}}
      
      {{deployment_steps_from_Q13_Q14_Q15_if_applicable}}
```

### Common Patterns

**CI Workflow:**
- Trigger: `push`, `pull_request`
- Steps: checkout → setup → install → test → lint
- No deployment

**CD Workflow:**
- Trigger: `release`, `push: tags: 'v*'`
- Steps: checkout → setup → install → test → build → deploy
- Requires secrets

**Release Workflow:**
- Trigger: `release: types: [published]`, `workflow_dispatch`
- Steps: checkout → setup → version bump → changelog → test → publish
- May create PR or tag

## Important Notes

- Workflows must be in `.github/workflows/` folder
- Use GitHub Actions marketplace actions when possible
- Store secrets in GitHub Secrets, reference with `${{ secrets.SECRET_NAME }}`
- Use matrix strategy for multiple Python versions/OS combinations
- Add workflow status badge to README if desired
- Keep workflows focused (one workflow per purpose)
- Use `workflow_dispatch` for manual triggers when needed

## Customization Based on Project Type

### SDK Python
- Test: `pytest tests/`
- Lint: `ruff check .`, `mypy src/`
- Build: `python -m build`
- Publish: `twine upload dist/*` (if PyPI)

### Hexagonal Python
- Test: `pytest tests/`
- Lint: `ruff check .`, `mypy src/`
- Build: Docker image (if containerized)
- Deploy: Deploy to cloud platform (if applicable)

### Streamlit
- Test: `pytest tests/` (if tests exist)
- Lint: `ruff check .`
- Deploy: Deploy to Streamlit Cloud or other platform

Start with question #1.