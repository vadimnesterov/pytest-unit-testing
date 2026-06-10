import pytest
from practicum.burger import Burger


@pytest.fixture
def burger():
    """Return a fresh Burger instance before each test so tests do not affect each other."""
    return Burger()
