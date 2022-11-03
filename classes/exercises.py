"""
Python 101 - CI Academy 2022

Class exercise
"""
from math import sin

class Triangle:

    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        return False

    def side_lenght(self, perimeter):
        k = perimeter / (sin(self.angle1) + sin(self.angle2) + sin(self.angle3))
        return ( k * sin(self.angle1), k * sin(self.angle2), k * sin(self.angle3))


class Equilateral(Triangle):

    def __init__(self):
        self.angle1 = 60
        self.angle2 = 60
        self.angle3 = 60

    def area(self, side):
        return side*side/2


# 1.1. Create a class, `Triangle`.
#
#    Its __init__() method should take `self`, `angle1`, `angle2`, and `angle3` as arguments.
#    Make sure to set these appropriately in the body of the `__init__()` method.

# 1.2. Create a `Triangle` class variable named `number_of_sides` and set it equal to 3.

# 1.3. Create a `Triangle` class method named `check_angles`
#
#    The sum of a triangle's three angles is It should return True if the sum of
#    `self.angle1`, `self.angle2`, and `self.angle3` is equal 180, and False otherwise.

# 1.5. Create a `Triangle` class method that receives the perimeter and calculates the length of each side
#      The side lengths should be returned in a set.

# 2. Create an `Equilateral` class that inherits from `Triangle`
#
#    This class doesn't need to receive any angle __init__,
#    because we already know that all of them should be 60.

# 2.1. Create a `Equilateral` class method that receives a side length and calculates the triangle area.
