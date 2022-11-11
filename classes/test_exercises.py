"""
Python 101 - CI Academy 2022

Test Function exercises
"""
import pytest

import exercises

@pytest.mark.parametrize(
    'numbers,result', [([50, 60, 70],True),([60,60,70],False)]
)
def test_check_angles(numbers, result):
    t = exercises.Triangle(numbers[0], numbers[1], numbers[2])
    assert t.check_angles() == result
#pytest test_exercises.py::test_check_angles

@pytest.mark.parametrize(
    'perimeter,angle,result', [(3,[60, 60, 60],(1, 1, 1))]
)
def test_side_lenght(perimeter, angle, result):
    t = exercises.Triangle(angle[0], angle[1], angle[2])
    assert t.side_lenght(perimeter) == result

@pytest.mark.parametrize(
    'result', [(3,[60, 60, 60],(1, 1, 1))]
)
def test_equilateral():
    print()