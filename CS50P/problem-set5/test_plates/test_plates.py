from plates import is_valid

"""
File: test_plates.py

Catches corner cases:
    - without beginning alphabetical checks
    - without length checks
    - without checks for number placement
    - without checks for zero placement
    - without checks for alphanumeric characters

"""

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("cs50") == True

def test_empty():
    assert is_valid("") == False

def test_start():
    assert is_valid("123456") == False
    assert is_valid("50CS") == False
    assert is_valid("12") == False

def test_short():
    assert is_valid("CS4") == True
    assert is_valid("C4") == False
    assert is_valid("A") == False

def test_long():
    assert is_valid("ABCDEFG") == False

def test_num():
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False
    assert is_valid("CS!@50") == False
