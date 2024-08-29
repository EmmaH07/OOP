"""
Author: Emma Harel
Program name: circle
Description: A circle class that is a subclass of the class 'shape'
Date: 27/08/24
"""

from shape import Shape
import math


class Circle(Shape):
    def __init__(self, color, r):
        """
        object constructor
        :param color: the shape's color
        :type color: str
        :param r: the shape's radius
        :type r: float
        """
        super().__init__(color)
        self.r = r

    def get_color(self):
        """
        :return: the circle's color
        """
        return self.color

    def set_color(self, color):
        """
        a func that change's the circle's color
        :param color: the color to change to
        :type color: str
        """
        self.color = color

    def calculate_area(self):
        """
        a func that calculates the circle's area
        :return: the circle's area
        """
        return math.pi * self.r * self.r

    def calculate_perimeter(self):
        """
        a func that calculates the circle's perimeter
        :return: the circle's perimeter
        """
        return 2 * math.pi * self.r

    def __str__(self):
        """
        a func that dictates how to print a circle object.
        :return: the str to print
        """
        s = 'Shape type: Circle \r\n' + 'Color: ' + self.color + '\r\n' + 'Radius: ' + str(self.r)
        return s
