# Diplom_1 - Unit Tests

Automated unit tests for a burger-ordering model written as part of the
Yandex Practicum QA Automation course.

## What is tested

Unit tests covering the `Bun`, `Burger`, `Ingredient`, and `Database` classes
in the `practicum` package. Test coverage is 100%.

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
├── practicum/       # source code under test
├── tests/
│   ├── conftest.py  # shared fixtures
│   └── test_burger.py
└── requirements.txt
```
