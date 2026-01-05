import pytest
from bank import value

def test_lower_case():
    assert value("hello") == 0
    assert value("hey what's up") == 20
    assert value("what's up ?") == 100


def test_upper_case():
    assert value("HELLO") == 0
    assert value("HEY WHATS UP") == 20
    assert value("WHAT'S YOUR NAME") == 100


