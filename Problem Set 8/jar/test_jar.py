import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

def test_withdraw_not_enough_cookies():
    jar = Jar()
    with pytest.raises(ValueError, match="Not enough cookies in the jar."):
        jar.withdraw(2)

def test_deposit_capacity_exceeded():
    jar = Jar(capacity=3)
    with pytest.raises(ValueError, match="Cookie jar capacity exceeded."):
        jar.deposit(5)
