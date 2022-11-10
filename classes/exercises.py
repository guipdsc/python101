"""
Python 101 - CI Academy 2022

Class exercise
"""
import math
class Triangle:
    sides = 3

    def __init__(self,angle1,angle2,angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        if not self.check_angle():
            raise ValueError("Not a triangle!")

    def __str__(self):
        return [self.angle1,self.angle2,self.angle3]

    def check_angle(self):
        return self.angle1+self.angle2+self.angle3 == 180
    
    def calculate_triangle_sides(self,per):
        cal = math.sin(math.radians(self.angle1))+math.sin(math.radians(self.angle2))+math.sin(math.radians(self.angle3))
        res = per/cal
        a = round(math.sin(math.radians(self.angle1))*res,3)
        b = round(math.sin(math.radians(self.angle2))*res,3)
        c = round(math.sin(math.radians(self.angle3))*res,3)
        return(a,b,c)

class Equilateral(Triangle):
    def __init__(self):
        super().__init__(60,60,60)

    def area_calc(self,side):
        return round(((3**0.5)/4)*(side**2),3)
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
