import pytest
from calculateGrade import calculate_grade

def test_calculate_grade():
    assert calculate_grade(95) == "A"
    assert calculate_grade(85) == "B"
    assert calculate_grade(75) == "C"
    assert calculate_grade(65) == "D"
    assert calculate_grade(55) == "F"