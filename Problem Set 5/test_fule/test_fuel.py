from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0

    with pytest.raises(ValueError):
        convert('a/b')
    with pytest.raises(ZeroDivisionError):
        convert('2/0')

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"

    assert gauge(99) == "F"
    assert gauge(99.2) == "F"
    assert gauge(100) == "F"

    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(0.5) == "E"
