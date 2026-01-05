from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        Jar(-5)


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(3)
    assert jar.size == 3


def test_withdraw():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(6)
