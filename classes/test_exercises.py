import pytest
from pytest import approx
import exercises

ex_tri = (60,60,60)
tri_error = (12,24,36)
ex_tri2 = (60,90,30)
ex_tri3 = (40,80,60)

@pytest.mark.parametrize(
    "angle1,angle2,angle3,result", [(*ex_tri,[60,60,60]),(*tri_error,False)]
)
def test_create_triangles(angle1,angle2,angle3,result):
    if not result:
        with pytest.raises(ValueError,match=r"Not a triangle!"):
            exercises.Triangle(angle1,angle2,angle3)
    else:
        trianglo = exercises.Triangle(angle1,angle2,angle3)
        assert [trianglo.angle1,trianglo.angle2,trianglo.angle3] == result

@pytest.mark.parametrize(
    "triangle",[exercises.Triangle(*ex_tri)]
)
def test_tri_sides(triangle):
    assert triangle.sides == 3

@pytest.mark.parametrize(
    "triangle,result",[(exercises.Triangle(*ex_tri),True)]
)
def test_tri_check_angles(triangle,result):
    assert triangle.check_angle() == result

@pytest.mark.parametrize(
    "triangle,per,result",[(exercises.Triangle(*ex_tri),3,[1,1,1]),(exercises.Triangle(*ex_tri2),4.73205,[1.732,2,1]),(exercises.Triangle(*ex_tri3),2.87939,[0.742,1.137,1])]
)
def test_calc_tri(triangle,per,result):
    assert triangle.calculate_triangle_sides(per) == approx(result)


def test_equi_tri():
    trianglo = exercises.Equilateral()
    assert [trianglo.angle1,trianglo.angle2,trianglo.angle3] == [60,60,60]

@pytest.mark.parametrize(
    "side,result",[(1,0.433),(2,1.732),(3,3.897)]
)
def test_equi_area_calc(side,result):
    assert exercises.Equilateral().area_calc(side) == approx(result)