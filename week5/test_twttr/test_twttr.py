import pytest
from twttr import shorten

# test lower case
def test_lower_case():
    assert shorten("programming under stress") == "prgrmmng ndr strss"

# test upper case
def test_upper_case():
    assert shorten("CAPITALIZE") == "CPTLZ"

# test digits
def test_digits():
    assert shorten("13412") == "13412"

# test empty string
def test_empty_str():
    assert shorten("") == ""

def test_symbols():
    assert shorten("!@$%^&*") == "!@$%^&*"
