"""
Python 101 - CI Academy 2022

Test Function exercises
"""
import pytest
import math
from exercises import Triangle, Equilateral



#-----Fixtures for various triangles-----#

@pytest.fixture
def Triangle_Equilatero():
    return Triangle(60,60,60)

@pytest.fixture
def Triangle_Isosceles():
    return Triangle(30,60,90)

@pytest.fixture
def Not_a_Triangle():
    return Triangle(90,90,90)

@pytest.fixture
def Equilateral_class():
    return Equilateral()

#-----Testes-----#

def test_number_of_sides(Triangle_Isosceles):
    assert Triangle_Isosceles.number_of_sides == 3

def test_check_angles(Triangle_Equilatero,Triangle_Isosceles):
    assert Triangle_Equilatero.check_angles() == True
    assert Triangle_Isosceles.check_angles() == True

def test_check_angles_Error(Not_a_Triangle):
    assert Not_a_Triangle.check_angles() == False

def test_length_of_sides(Triangle_Equilatero,Triangle_Isosceles):
    assert Triangle_Equilatero.length_of_sides(3) == [1,1,1]
    assert Triangle_Isosceles.length_of_sides(2.73) == [0.58,1,1.15]


def test_calculate_side_area():
    assert Equilateral_class.side_area(4) == 6.92


