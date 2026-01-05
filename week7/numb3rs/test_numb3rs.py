from numb3rs import validate

def test_valid_addresses():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("140.247.235.144") == True

def test_invalid_ranges():
    assert validate("256.0.0.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False
    assert validate("999.999.999.999") == False


def test_invalid_structure():
    assert validate("8.8.8") == False
    assert validate("10.10.10.10.10") == False
    assert validate("1..1.1") == False
    assert validate("cat") == False
    assert validate("2001:db8::1") == False
