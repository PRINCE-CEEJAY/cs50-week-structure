import pytest
from fuel import convert, gauge

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_empty_string():
    with pytest.raises(ValueError):
        convert("")

def test_empty_arg():
    with pytest.raises(TypeError):
        convert()

def test_negative_X():
    with pytest.raises(ValueError):
        convert("-1/2")

def test_negative_Y():
    with pytest.raises(ValueError):
        convert("1/-2")

def test_negative_XY():
    with pytest.raises(ValueError):
        convert("-1/-2")

def test_bigger_X():
    with pytest.raises(ValueError):
        convert("3/2")

def test_strings():
    with pytest.raises(ValueError):
        convert("cat")

def test_single_input():
    with pytest.raises(ValueError):
        convert("1")

def test_convert():
    assert convert("1/2") == 50

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
