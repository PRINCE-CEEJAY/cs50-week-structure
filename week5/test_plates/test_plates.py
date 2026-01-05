import pytest
from plates import main
from plates import is_valid

def test_alphabets():
    assert is_valid("CS") == True
    assert is_valid("CSCSCS") == True
    assert is_valid("CS05") == False

def test_length():
    assert is_valid("C") == False
    assert is_valid("CS50") == True
    assert is_valid("FFDT01") == False
    assert is_valid("FFGO44FF") == False

def test_symbols():
    assert is_valid("%*AA") == False
    assert is_valid("!@#$%^") == False
    assert is_valid("!@FF33") == False
    assert is_valid("FF%*55") == False

def test_all_digits_invalid():
    assert is_valid("123456") == False
    assert is_valid("") == False

def test_number_placement():
    assert is_valid("CS50") == True
    assert is_valid("AB12C") == False
    assert is_valid("AA1A") == False
