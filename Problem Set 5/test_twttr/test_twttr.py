from twttr import shorten

def test_words():
    assert("") == ""
    assert shorten("twitter") == "twttr"
    assert shorten("twItter") == "twttr"
    assert shorten("TwittER") == "TwttR"

def test_numbers():
    assert shorten("1") == "1"
    assert shorten("100") == "100"
    assert shorten("0") == "0"

def test_punctuation():
    assert shorten(".") == "."
