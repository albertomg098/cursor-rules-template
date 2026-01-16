# My Development Standards - Python

## Type System

- **Use type hints everywhere** - All functions, methods, and class attributes must have type annotations
- **Use Python 3.11+ features** - Prefer modern Python syntax and features
- **Use `typing` module** - Import from `typing` for complex types (Optional, Union, List, Dict, etc.)
- **Use `from __future__ import annotations`** - For forward references and cleaner type hints
- **Type check with mypy** - Ensure type hints are correct and consistent

## Code Style

- **Follow PEP 8** - Use Black or Ruff for formatting
- **Use descriptive names** - Variable and function names should clearly express intent
- **Keep functions focused** - Single responsibility principle
- **Use docstrings** - NumPy-style docstrings for complex functions/classes
- **English docstrings** - All docstrings in English

## Async/Await Patterns

- **Use async/await** - Prefer async functions for I/O operations
- **Use proper async libraries** - httpx instead of requests, async database drivers
- **Handle async context properly** - Use async context managers and proper cleanup

## Error Handling

- **Use custom exceptions** - Create domain-specific exception hierarchies
- **Raise exceptions early** - Fail fast with clear error messages
- **Handle exceptions explicitly** - Don't use bare `except:` clauses
- **Use exception chaining** - Use `raise ... from ...` when appropriate

---

## TDD Workflow (Python/pytest)

### Commands by Phase

**RED Phase (Tests Must Fail):**
```bash
# Run specific tests - expect failures
pytest -k "test_description" -v

# Or run a specific test file
pytest tests/unit/module/test_feature.py -v

# All new tests should FAIL - this proves they're valid
```

**GREEN Phase (Make Tests Pass):**
```bash
# Run same tests - expect pass
pytest -k "test_description" -v

# All tests should PASS now
```

**VALIDATE Phase (Full Quality Check):**
```bash
# Run full validation pipeline
ruff check . && mypy . && pytest --cov --cov-fail-under=80

# Or step by step:
ruff check .                    # Linting
mypy .                          # Type checking
pytest --cov --cov-fail-under=80  # Tests with coverage
```

### TDD Execution Log Template

Add to todos/PRs for Python projects:

```markdown
### TDD Execution Log
| Phase | Command | Result | Timestamp |
|-------|---------|--------|-----------|
| RED | `pytest -k "test_name" -v` | 3 tests failed ✓ | - |
| GREEN | `pytest -k "test_name" -v` | 3 tests passed ✓ | - |
| VALIDATE | `ruff check . && mypy . && pytest --cov` | Pass, 85% ✓ | - |
```

### Blocking Conditions

**NEVER mark a todo as complete if:**
- ❌ Tests were not written first (skipped RED phase)
- ❌ Tests did not fail initially (invalid tests - rewrite them)
- ❌ Any test is failing
- ❌ `ruff check` has errors
- ❌ `mypy` has errors
- ❌ Coverage dropped below 80%

### Bug Fix Workflow (Python-Specific)

```bash
# 1. DIAGNOSE - Run existing tests
pytest -v
# If all pass but bug exists → test gap!

# 2. RED - Write failing test
# Add test to tests/unit/... that reproduces the bug
pytest -k "test_bug_description" -v
# Should FAIL

# 3. GREEN - Fix the bug
# Implement fix
pytest -k "test_bug_description" -v
# Should PASS

# 4. VALIDATE - Full check
ruff check . && mypy . && pytest --cov --cov-fail-under=80
```

---

## Testing

- **Use pytest** - Standard testing framework
- **Use pytest fixtures** - For test setup and teardown
- **Mock external dependencies** - Use unittest.mock or pytest-mock
- **Test structure mirrors source** - Keep test organization aligned with source code structure
- **80% coverage minimum** - Enforce with pytest-cov
- **Hierarchical conftest.py** - Place fixtures at appropriate levels

### Test Structure

```
tests/
├── conftest.py              # Shared fixtures
├── unit/
│   ├── conftest.py          # Unit test fixtures
│   ├── domain/
│   │   └── test_entities.py
│   └── application/
│       └── test_use_cases.py
├── integration/
│   ├── conftest.py          # Integration fixtures
│   └── test_api.py
└── e2e/
    └── test_workflows.py
```

### Fixture Patterns

```python
# conftest.py
import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_repository():
    """Mock repository for unit tests."""
    return Mock()

@pytest.fixture
def sample_entity():
    """Sample entity for testing."""
    return Entity(id="123", name="Test")
```

### Test Naming Convention

```python
def test_<function>_<scenario>_<expected_result>():
    """Test description."""
    # Arrange
    # Act
    # Assert

# Examples:
def test_validate_email_valid_input_returns_true():
def test_validate_email_missing_at_raises_validation_error():
def test_create_user_duplicate_email_raises_conflict_error():
```

---

## Dependencies

- **Pin versions** - Use requirements.txt or pyproject.toml with version constraints
- **Use uv for environment management** - Standard tool for virtual environments and dependency management (`uv venv`, `uv pip install`, `uv sync`)
- **Document dependencies** - Keep dependency lists up to date

## Project Structure

- **Use src/ layout** - Keep source code in `src/` directory
- **Separate concerns** - Domain, application, infrastructure layers
- **Use __init__.py** - Properly structure packages
- **Keep imports organized** - Standard library, third-party, local imports

```
project/
├── src/
│   └── package_name/
│       ├── __init__.py
│       ├── domain/
│       ├── application/
│       └── infrastructure/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── pyproject.toml
└── README.md
```

## Performance

- **Profile before optimizing** - Use cProfile or line_profiler
- **Use generators** - For large datasets or streaming
- **Cache appropriately** - Use functools.lru_cache or caching libraries when needed

---

## Simplicity Constraints (Python-Specific)

### Line Counting

```python
# Check function length (should be ≤20 lines)
# Check file length (should be ≤200 lines)
# Check parameter count (should be ≤3)

# If too many parameters, use dataclass or TypedDict:
from dataclasses import dataclass

@dataclass
class CreateUserRequest:
    email: str
    name: str
    role: str
    department: str
    # ... more fields

def create_user(request: CreateUserRequest) -> User:
    # Now only 1 parameter instead of many
    ...
```

### Nesting Reduction

```python
# ❌ Bad: Deep nesting
def process(data):
    if data:
        if data.is_valid:
            if data.status == "active":
                # ... logic
                pass

# ✅ Good: Early returns
def process(data):
    if not data:
        return None
    if not data.is_valid:
        raise ValidationError("Invalid data")
    if data.status != "active":
        return None
    
    # ... logic (flat)
```

---

## Quality Check Script

Create `scripts/validate.sh` for full validation:

```bash
#!/bin/bash
set -e

echo "🔍 Running linter..."
ruff check .

echo "🔍 Running type checker..."
mypy .

echo "🧪 Running tests with coverage..."
pytest --cov --cov-fail-under=80 --cov-report=term-missing

echo "✅ All checks passed!"
```
