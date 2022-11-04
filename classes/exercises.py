"""
Python 101 - CI Academy 2022

Class exercise
"""

import math
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

class Triangle(object):

    number_of_sides = 3

    def __init__(self, angle1, angle2,angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
            
        return sum([self.angle1,self.angle2,self.angle3]) == 180
            

    def get_side_lengths(self, perimeter):
        
        sum_sin = math.sin(math.radians(self.angle1)) + math.sin(math.radians(self.angle2)) + math.sin(math.radians(self.angle3))     
        k = perimeter/sum_sin
        list = [k*math.sin(math.radians(self.angle1)),k*math.sin(math.radians(self.angle2)),k*math.sin(math.radians(self.angle3))]

        return [round(item, 2) for item in list]

class Equilateral(Triangle):
      def __init__(self):
        super().__init__(60,60,60)

      def get_area(self,side):
        area = (math.sqrt(3)/4) * math.pow(side,2)
        return round(area,2)
