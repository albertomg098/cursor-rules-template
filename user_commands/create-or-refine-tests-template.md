# Create or Refine Tests

Create, extend, or refine tests following project standards: structure mirrors src/, hierarchical conftest.py, initialization strategy for mocking, manual DI, 80% coverage minimum, SOLID/DRY/KISS principles.

**CRITICAL:** Follow interview standards - ONE question at a time, show progress (X/TOTAL), use emojis, wait for answer before proceeding.

## Interview

Ask ONE at a time:

1. **Question 1/8:** 🎯 What do you want to do?
   - Create new tests for a file/module
   - Extend existing tests
   - Refine/improve existing tests
   - Check and improve test coverage

2. **Question 2/8:** 📁 What file/module/component needs tests?
   - Ask for specific path relative to project root (e.g., `src/{{package}}/client.py`, `src/domain/entities/user.py`)
   - If creating new: "What file/module should I create tests for?"
   - If extending/refining: "What test file should I extend? (or what source file needs more tests?)"

3. **Question 3/8:** 🔍 Analyze the target:
   - Read the source file to understand:
     - Classes and functions (public vs private)
     - Dependencies (imports, external services)
     - Manual DI patterns (constructors with optional params for mocking)
     - Error handling and edge cases
   - If extending/refining: Read existing test file to understand current coverage

4. **Question 4/8:** 🧪 What type of tests?
   - Unit tests (test individual functions/classes in isolation)
   - Integration tests (test interactions between components)
   - E2E tests (test full workflows)
   - All of the above (start with unit, then integration, then e2e if needed)

5. **Question 5/8:** 📂 Confirm test location:
   - Based on source file location, determine test path:
     - Source: `src/{{package}}/client.py` → Test: `tests/unit/{{package}}/client/test_client.py`
     - Source: `src/domain/entities/user.py` → Test: `tests/unit/domain/entities/test_user.py`
   - Ask: "Should tests go in `tests/unit/`, `tests/integration/`, or `tests/e2e/`?" (or confirm based on Q4)

6. **Question 6/8:** 🎭 What needs to be mocked?
   - Analyze dependencies from source file
   - Ask: "What external dependencies should be mocked? (APIs, databases, file system, other modules)"
   - Confirm: Use initialization strategy (optional params in constructors) for mocking
   - Ask: "Should mocks go in conftest.py or inline in test file?"

7. **Question 7/8:** ✅ Coverage requirements:
   - Confirm: 80% minimum coverage (project standard)
   - If extending/refining: Check current coverage and identify gaps
   - Ask: "What specific scenarios/edge cases are missing tests?"

8. **Question 8/8:** 📝 Test structure preferences:
   - Ask: "Use test classes or standalone test functions?" (recommend classes for organization)
   - Ask: "Any specific test patterns to follow?" (AAA pattern, pytest fixtures, etc.)

## Generate Tests

Based on answers:

### 1. Create/Update Test File

**Location:** Based on Q5, create test file in correct location mirroring src/ structure.

**Structure:**
```python
"""Tests for {{module_name}}."""
import pytest
from {{import_path}} import {{classes_to_test}}

# Import fixtures from conftest if needed
# from conftest import mock_dependency


class Test{{ClassName}}:
    """Test suite for {{ClassName}}."""
    
    def test_{{method}}_happy_path(self, mock_dependency):
        """Test {{method}} with valid input."""
        # Arrange
        instance = {{ClassName}}(dependency=mock_dependency)
        
        # Act
        result = instance.method()
        
        # Assert
        assert result == expected_value
    
    def test_{{method}}_error_handling(self, mock_dependency):
        """Test {{method}} error handling."""
        # Arrange
        instance = {{ClassName}}(dependency=mock_dependency)
        
        # Act & Assert
        with pytest.raises(ExpectedException):
            instance.method(invalid_input)
    
    # Add more test cases for edge cases, boundary conditions, etc.
```

### 2. Create/Update Conftest.py

**Location:** Create or update conftest.py at appropriate level (hierarchical structure).

**Content:**
```python
"""Pytest configuration and fixtures."""
import pytest
from unittest.mock import Mock, MagicMock

# Mock fixtures for dependencies
@pytest.fixture
def mock_{{dependency_name}}():
    """Mock fixture for {{dependency_name}}."""
    return Mock({{dependency_name}})

# Add more fixtures as needed
```

### 3. Test Cases to Include

- **Happy path:** Test normal operation with valid inputs
- **Edge cases:** Test boundary conditions, empty inputs, None values
- **Error handling:** Test exception raising and error messages
- **Integration:** Test interactions between components (if integration tests)
- **E2E:** Test full workflows (if e2e tests)

### 4. Follow Patterns

- **Structure:** Mirror src/ structure in tests/
- **Naming:** `test_<module_name>.py`, `test_<function>_<scenario>_<expected>`
- **Mocking:** Use manual DI (optional params in constructors)
- **Fixtures:** Use pytest fixtures, place in hierarchical conftest.py
- **AAA Pattern:** Arrange, Act, Assert
- **Coverage:** Aim for 80% minimum, test public API, edge cases, errors

## Important Notes

- Always mirror src/ structure in tests/ (unit/integration/e2e folders)
- Use hierarchical conftest.py files (conftest.py at test folder levels)
- Follow initialization strategy: optional params in constructors for mocking
- Ensure 80% coverage minimum
- Write descriptive test names following pattern: `test_<function>_<scenario>_<expected_result>`
- Use AAA pattern (Arrange, Act, Assert)
- Mock external dependencies (APIs, databases, file system)
- Test public API, edge cases, and error handling
- Follow SOLID/DRY/KISS principles
- Use pytest fixtures for reusable test data/mocks
- Use type hints in test code
- Add docstrings to test classes and complex test functions

## Customization Based on Project Type

**IMPORTANT:** Customize the examples below based on the actual project structure and patterns.

### SDK Python
- Test components separately
- Mock external APIs (requests, httpx)
- Test public API exports from `__init__.py`
- Test component interactions
- Test exception hierarchy

### Hexagonal Python
- Test use cases in isolation (mock ports)
- Test domain entities (immutable, business logic)
- Test adapters separately (mock external services)
- Test error handling and custom exceptions
- Test FastAPI routes (mock use cases)
- Test CLI commands (mock use cases)

### Streamlit
- Mock Streamlit functions (`st.write`, `st.sidebar`, etc.)
- Test data processing functions
- Test UI component rendering
- Test user interaction flows

Start with question #1.