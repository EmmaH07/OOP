"""
Author: Emma Harel
Program name: rectangle
Description: A rectangle class that is a subclass of the class 'shape'
Date: 27/08/24
"""

from shape import Shape
import random


class Rectangle(Shape):
    def __init__(self, color, length, width):
        """
        object constructor
        :param color: the shape's color
        :type color: str
        :param length: the rectangle's length
        :type length: float
        :param width: the rectangle's width
        :type width: float
        """
        super().__init__(color)
        self.length = length
        self.width = width

    def get_color(self):
        """
        :return: the rectangle's color
        """
        return self.color

    def set_color(self, color):
        """
        a func that change's the rectangle's color
        :param color: the color to change to
        :type color: str
        """
        self.color = color

    def calculate_area(self):
        """
        a func that calculates the rectangle's area
        :return: the rectangle's area
        """
        return self.length * self.width

    def calculate_perimeter(self):
        """
        a func that calculates the rectangle's perimeter
        :return: the rectangle's perimeter
        """
        return self.length * 2 + self.width * 2

    def __add__(self, rec):
        """
        a func the sums two rectangle objects (a square is a type of rectangle)
        :param rec: a rectangle object
        :type rec: Rectangle
        :return: a new rectangle object that is a sum of two rectangle objects
        """
        new_length = self.length + rec.length
        new_width = self.width + rec.width
        if random.randint(0, 2) == 1:
            new_color = self.color
        else:
            new_color = rec.color
        return Rectangle(new_color, new_length, new_width)

    def __str__(self):
        """
        a func that dictates how to print a rectangle object.
        :return: the str to print
        """
        s = 'Shape type: Rectangle \r\n' + 'Color: ' + self.color + '\r\n' + 'Length: ' + str(
            self.length) + '\r\n' + 'Width: ' + str(self.width)
        return s
