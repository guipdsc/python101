import pytest

from exercises import Triangle, Equilateral
    


@pytest.mark.parametrize(
    "angles,result", [([60, 60, 60], True), ([45, 60, 75], True), ([150, 20, 10], True)]
)
def test_check_angles(angles, result):
    triangle = Triangle(angles[0],angles[1],angles[2])
    assert triangle.check_angles() == result


@pytest.mark.parametrize(
    "perimeter,lengths,angles", [(3, (1,1,1), [60,60,60]), (7.5, (2.5, 2.5, 2.5), [60,60,60] ), (11, ((2.817394911310551, 0.9615905271914361, 7.221014561498014)), [75,25,80])]
)
def test_length_of_each_side(perimeter, lengths, angles):
    triangle = Triangle(angles[0], angles[1], angles[2])
    assert triangle.length_of_each_side(perimeter) == (lengths[0], lengths[1], lengths[2])


@pytest.mark.parametrize(
    "length, area", [(1, 0.21650635094610965), (10, 216.50635094610965)]
)
def test_area_of_triangle(length, area):
    triangle = Equilateral()
    assert triangle.area_of_triangle(length) == area
