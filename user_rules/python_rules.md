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

## Testing

- **Use pytest** - Standard testing framework
- **Use pytest fixtures** - For test setup and teardown
- **Mock external dependencies** - Use unittest.mock or pytest-mock
- **Test structure mirrors source** - Keep test organization aligned with source code structure
- **80% coverage minimum** - Enforce with pytest-cov

## Dependencies

- **Pin versions** - Use requirements.txt or pyproject.toml with version constraints
- **Use virtual environments** - Always work in isolated environments
- **Document dependencies** - Keep dependency lists up to date

## Project Structure

- **Use src/ layout** - Keep source code in `src/` directory
- **Separate concerns** - Domain, application, infrastructure layers
- **Use __init__.py** - Properly structure packages
- **Keep imports organized** - Standard library, third-party, local imports

## Performance

- **Profile before optimizing** - Use cProfile or line_profiler
- **Use generators** - For large datasets or streaming
- **Cache appropriately** - Use functools.lru_cache or caching libraries when needed
