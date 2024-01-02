import pytest
from seasons import get_time, num_to_word

def test_time():
    assert get_time("2022-12-27") == 525600
    assert get_time("2021-12-27") == 1051200
    # with pytest.raises(ValueError):
    #     get_time("Jan 1, 2022")
    with pytest.raises(SystemExit):
        get_time("Jan 1, 2022")
    with pytest.raises(SystemExit):
        get_time("No Date")
    with pytest.raises(SystemExit):
        get_time("12-12-2020")
    with pytest.raises(SystemExit):
        get_time("0")

def test_word():
    assert num_to_word(525600) == "Five hundred twenty-five thousand, six hundred"
    assert num_to_word(1051200) == "One million, fifty-one thousand, two hundred"



# from seasons import convert

# def test_date():
#     assert convert(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
#     assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
