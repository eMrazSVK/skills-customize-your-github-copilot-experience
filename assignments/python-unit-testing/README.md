# 📘 Assignment: Python Unit Testing Fundamentals

## 🎯 Objective

Learn how to verify Python code quality by writing and running unit tests with the built-in `unittest` module. You will practice creating reliable test cases, checking expected behavior, and validating edge cases.

## 📝 Tasks

### 🛠️	Write and Run Basic Unit Tests

#### Description
Create a small Python module with simple functions and add a test file that verifies correct outputs using `unittest` assertions.

#### Requirements
Completed program should:

- Include at least two functions in `starter-code.py` (for example: `add(a, b)` and `is_even(n)`).
- Include a separate test file named `test_starter_code.py`.
- Use `unittest.TestCase` with at least four assertions.
- Run successfully with `python -m unittest`.


### 🛠️	Test Edge Cases and Failures

#### Description
Expand your test suite to cover edge cases and invalid inputs so the code behaves predictably in less common scenarios.

#### Requirements
Completed program should:

- Add tests for at least two edge cases (for example: zero, negative numbers, or empty strings).
- Add at least one test that validates error handling (such as using `assertRaises`).
- Keep test names clear and descriptive.
- Ensure all tests pass after updates.
