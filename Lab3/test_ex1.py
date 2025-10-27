import pytest
from ex1 import Solution

"""
Outsource:
- tests (Grok)
"""

def test_creation_valid():
    s = Solution("NaCl", 5.0, 15.0)
    assert s.name == "NaCl"
    assert s.concentration == 5.0
    assert s.volume == 15.0

def test_creation_invalid_concentration():
    with pytest.raises(ValueError, match="Concentration must be greater than 0"):
        Solution("NaCl", 0, 10)

def test_creation_invalid_volume():
    with pytest.raises(ValueError, match="Volume must be greater than 0"):
        Solution("NaCl", 5, 0)

def test_add_different_substance():
    s1 = Solution("NaCl", 5.0, 20.0)
    s2 = Solution("HCl", 1.0, 15.0)
    with pytest.raises(ValueError, match="Cannot mix different substances!"):
        s1.add(s2)

def test_dilute_invalid():
    s = Solution("NaCl", 4.0, 20.0)
    with pytest.raises(ValueError, match="Dilution factor must be greater than 0"):
        s.dilute(0)        

def test_add_same_substance():
    s1 = Solution("NaCl", 5.0, 20.0)
    s2 = Solution("NaCl", 1.0, 15.0)
    s1.add(s2)
    assert s1.volume == 35.0
    assert pytest.approx(s1.concentration, 0.0001) == 3.2857142857

def test_dilute_valid():
    s = Solution("NaCl", 4.0, 20.0)
    s.dilute(2)
    assert pytest.approx(s.concentration, 0.0001) == 2.0

def test_equality_true():
    s1 = Solution("NaCl", 3.0, 10.0)
    s2 = Solution("NaCl", 3.0, 5.0)
    assert s1 == s2

def test_equality_false_name():
    s1 = Solution("NaCl", 4.0, 5.0)
    s2 = Solution("HCl", 4.0, 5.0)
    assert s1 != s2

def test_equality_false_concentration():
    s1 = Solution("NaCl", 4.0, 10.0)
    s2 = Solution("NaCl", 5.0, 10.0)
    assert s1 != s2
