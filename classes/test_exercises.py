"""
Python 101 - CI Academy 2022

Test Function exercises
"""
import pytest
from pytest import approx
from exercises import Triangle,Equilateral

equi_angles = (60,60,60)

@pytest.fixture
def equilateral_triangle():
    '''Returns a equilateral triangle'''
    return Equilateral()

@pytest.fixture
def isosceles_triangle():
    '''Returns a isosceles triangle'''
    return Triangle(72,72,36)

@pytest.fixture
def not_a_triangle():
    '''Returns a not trangle'''
    return Triangle(130,19,35)


def test_number_of_sides(isosceles_triangle,equilateral_triangle):
    assert isosceles_triangle.number_of_sides == 3
    assert equilateral_triangle.number_of_sides == 3
    

def test_check_angles(isosceles_triangle,equilateral_triangle):
    assert isosceles_triangle.check_angles() 
    assert equilateral_triangle.check_angles()

def test_check_angles_error(not_a_triangle):
    assert not_a_triangle.check_angles() != True

def test_get_side_lengths(isosceles_triangle,equilateral_triangle):
    assert isosceles_triangle.get_side_lengths(21.18) == [8.09,8.09,5]
    assert equilateral_triangle.get_side_lengths(9) == [3,3,3]

def test_is_equilateral(equilateral_triangle):
    assert [equilateral_triangle.angle1,equilateral_triangle.angle2,equilateral_triangle.angle3] == [60,60,60]

@pytest.mark.parametrize(
    "side,result",
    [(3, 3.9), (5, 10.83), (9,35.07)],
)
def test_get_area(equilateral_triangle,side,result):
    assert equilateral_triangle.get_area(side) == approx(result)





