from datetime import datetime, date
from seasons import get_minutes, convert_to_words

def test_get_minutes_known_date():
    dob = datetime(2023, 1, 1)
    # computing expected minuts manually
    today = date.today()
    expected_days = (today - dob.date()).days
    expected_minutes = expected_days * 1440
    assert get_minutes(dob) == expected_minutes

def test_get_minutes_today():
    dob = datetime.today()
    assert get_minutes(dob) == 0


#tests fr convert_to_words

def test_convert_to_words_basic():
    assert convert_to_words(1) == "One minute"
    assert convert_to_words(60) == "Sixty minutes"
    assert convert_to_words(1440) == "One thousand, four hundred forty minutes"

def test_convert_to_words_large_number():
    minutes = 123456
    words = convert_to_words(minutes)
    assert "minutes" in words
    #Ensuring that the first letter is capitalized
    assert words[0].isupper()
