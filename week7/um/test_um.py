from um import count

def test_basic():
    assert count("hello, um, world") == 1

def test_multiple_ums():
    assert count("Um, I think um, we should go.") == 2

def test_no_um():
    assert count("yummy, umbrella, dumb") == 0

def test_with_punctuation():
    assert count("um! Um. UM?") == 3
