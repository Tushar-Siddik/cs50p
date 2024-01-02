from plates import is_valid

def test_normal():
    assert is_valid("CS50") == bool(True)
    assert is_valid("OUTA10") == bool(True)

def test_cs05():
    assert is_valid("CS05") == bool(False)
    assert is_valid("CS50P") == bool(False)

def test_pi314():
    assert is_valid("PI3.14") == bool(False)

def test_H():
    assert is_valid("H") == bool(False)

def test_otattime():
    assert is_valid("OUTATTIME") == bool(False)

def test_notalpha():
    assert is_valid("12fgji") == bool(False)


def test_starts_with_two_letters():
    assert is_valid('AA') == True
    assert is_valid('1A') == False
    assert is_valid('!A') == False
    assert is_valid('A3') == False
    assert is_valid('98') == False
