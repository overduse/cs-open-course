from um import count
import pytest

"""
file: test_um.py
Description:
  Unit tests for the `count` function in `um.py`.

"""


def test_count_um():
    # Single "um"
    assert count("um") == 1

def test_count_umm():
    # "umm" should not be counted
    assert count("umm") == 0

def test_count_umend1():
    # "um" followed by non-word characters
    assert count("umm..") == 0

def test_count_umend2():
    # "um" followed by ellipsis
    assert count("um...") == 1

def test_count_uncase():
    # Case-insensitive matching
    assert count("Um") == 1
    assert count("UMM") == 0

def test_count_multiple():
    # Multiple occurrences of "um"
    assert count("um, um, um.") == 3

def test_count_empty():
    # Empty input
    assert count("") == 0

def test_count_unrelated():
    # Unrelated input
    assert count("hello world") == 0


def test_count_sentence():
    # "um" in a sentence with other words
    assert count("Um, I was thinking... um, maybe.") == 2
