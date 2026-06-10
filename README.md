# Python Unit Test Suite

Pytest unit test suite for a domain model covering a burger-ordering system.
Tests verify the business logic of the `Bun`, `Ingredient`, `Burger`, and `Database`
classes with 100% branch coverage.

## What is covered

- `Burger.get_receipt()` - price calculation with correct bun and ingredient costs
- `Burger.add_ingredient()` / `remove_ingredient()` - ingredient list management
- `Burger.set_buns()` - bun assignment and price reflection
- `Database` - available buns and ingredients retrieval
- All parametrized over multiple bun/ingredient combinations

## Tech stack

- Python 3.x
- pytest
- pytest-cov (coverage reporting)

## How to run

```bash
pip install -r requirements.txt
pytest -v
```

To generate an HTML coverage report:

```bash
pytest --cov=practicum --cov-report=html
```

## Project structure

```
pytest-unit-testing/
    practicum/       # source code under test
    tests/
        conftest.py  # shared fixtures
        test_burger.py
    requirements.txt
```
