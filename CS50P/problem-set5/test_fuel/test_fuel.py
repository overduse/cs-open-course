from fuel import convert, gauge
import pytest

"""
File: fuel.py
Check(corner cases):
  - returning incorrect ints in convert
  - not raising ValueError in convert
  - not raising ZeroDivisionError in convert
  - not labeling 1% as E in gauge
  - not printing % in gauge
  - not labeling 99% as F in gauge

"""

def test_convert():
    assert convert("3/4") == 75

def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("4/3")

def test_gauge_small():
    assert gauge(1) == 'E'

def test_gauge_large():
    assert gauge(1) == 'F'

def test_gauge_normal():
    assert gauge(80) == "80%"
