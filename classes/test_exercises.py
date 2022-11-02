import pytest
import exercises

@pytest.fixture
def triangle1():
    return exercises.Triangle(30,60,90)

@pytest.fixture
def triangle2():
    return exercises.Triangle(90,90,90)

@pytest.fixture
def triangle3():
    return exercises.Triangle(60,60,60)

@pytest.fixture
def triangle4():
    return exercises.Triangle(72,72,36)

@pytest.fixture
def equi_triangle1():
    return exercises.Equilateral()

def test_number_of_sides(triangle1):
    assert triangle1.number_of_sides == 3

def test_check_angles(triangle1,triangle2,triangle3,triangle4):
    assert triangle1.check_angles()
    assert triangle2.check_angles() == False
    assert triangle3.check_angles()
    assert triangle4.check_angles()

def test_check_calc_lengths(triangle1,triangle3,triangle4):
    assert triangle1.calc_side_lengths(4.73) == {1,2,1.73}
    assert triangle3.calc_side_lengths(12) == {4,4,4}
    assert triangle4.calc_side_lengths(21.18) == {8.09,8.09,5}

def test_equilateral_angles(equi_triangle1):
    assert [equi_triangle1.ang1,equi_triangle1.ang2,equi_triangle1.ang3] == [60,60,60]

def test_equilateral_get_area(equi_triangle1):
    assert equi_triangle1.get_area(1) == 0.43
    assert equi_triangle1.get_area(3) == 3.90
    assert equi_triangle1.get_area(6) == 15.59






