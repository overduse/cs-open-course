from bank import value

"""
File: test_bank.py

Test File used by command line:
pytest ./test_bank.py

"""

def test_value_hello():
    assert value("hello, world") == 0
    assert value("Hello, world") == 0

def test_value_hey():
    assert value("hey!") == 20

def test_value_other():
    assert value("balabala!") == 100
