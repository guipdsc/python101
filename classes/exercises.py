"""
Python 101 - CI Academy 2022

Class exercise
"""
import numpy as np

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
class Triangle:
    def __init__(self, ang1,ang2, ang3):
        self.ang1 = ang1
        self.ang2 = ang2
        self.ang3 = ang3
        self.number_of_sides = 3
    
    def check_angles(self):
        if self.ang1 + self.ang2 + self.ang3 == 180:
            return True
        return False
    
    def calc_side_lengths(self, perimiter):
        den = np.sin(np.deg2rad(self.ang1)) + np.sin(np.deg2rad(self.ang2)) + np.sin(np.deg2rad(self.ang3))
        k = perimiter/den
        sides = [k*np.sin(np.deg2rad(self.ang1)),k*np.sin(np.deg2rad(self.ang2)),k*np.sin(np.deg2rad(self.ang3))]
        return {round(s,2) for s in sides}


class Equilateral(Triangle):
    def __init__(self):
        self.ang1 = 60
        self.ang2 = 60
        self.ang3 = 60

    def get_area(self, side):
        return round((side**2 * np.sqrt(3)) / 4, 2)
