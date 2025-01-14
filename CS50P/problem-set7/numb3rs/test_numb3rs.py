from numb3rs import validate
import pytest

"""
File: test_numb3rs.py
Description:
    This script contains unit tests for the 'validate'
    function in the 'numb3rs' module, which is used to
    validate the correctness of IPv4 addresses.

"""

def test_validate_first():
    assert validate("255.0.0.0") == True
    assert validate("274.0.0.0") == False
    assert validate("-1.0.0.0") == False

def test_validate_second():
    assert validate("255.255.255.0") == True
    assert validate("255.275.255.0") == False
    assert validate("255.-1.255.0") == False


def test_validate_third():
    assert validate("255.255.255.0") == True
    assert validate("255.255.-1.0") == False
    assert validate("255.255.275.0") == False

def test_validate_forth():
    assert validate("255.255.255.0") == True
    assert validate("255.255.255.256") == False
    assert validate("255.255.255.-2") ==  False
