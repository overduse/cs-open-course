from jar import Jar
import pytest

"""
file: test_jar.py
Decription:
    Contains unit tests for the `Jar` class from the `jar.py` module.

Key tests:
    - `test_init()`: Verifies that the  initialization.
    - `test_print()`: Tests the `__str__` method.
    - `test_deposit()`: Tests the deposit functionality.
    - `test_withdraw()`: Tests the withdraw functionality.

"""


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar = Jar(3)
    assert jar.capacity == 3
    assert jar.size == 0

def test_print():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(11)

def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    assert str(jar)== "🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar)== "🍪"
    with pytest.raises(ValueError):
        jar.withdraw(2)



if __name__ == '__main__':
    test_print()
