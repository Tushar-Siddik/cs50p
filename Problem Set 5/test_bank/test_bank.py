from bank import value

def test_hello():
    assert value("hello") == int(0)
    assert value("Hello") == int(0)
    assert value("Hello, world!") == int(0)
    assert value(" Hello ") == int(0)


def test_hi():
    assert value("hi") == int(20)
    assert value("How you doing?") == int(20)

def test_others():
    assert value("good morning") == int(100)
    assert value("") == int(100)
    assert value("2") == int(100)
    assert value(".") == int(100)
    assert value("What's happening?") == int(100)
    assert value("What's up?") == int(100)
