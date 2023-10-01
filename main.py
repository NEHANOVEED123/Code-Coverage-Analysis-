import pytest
from calculateGrade import calculate_grade
from test_grade import test_calculate_grade

if __name__ == '__main__':
    grade = calculate_grade(47)
    print("Grade:", grade)
    grade = calculate_grade(67)
    print("Grade:", grade)
    grade = calculate_grade(97)
    print("Grade:", grade)
