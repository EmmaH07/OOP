"""
Author: Emma Harel
Program name: shape
Description: A superclass by the name 'shape'
Date: 27/08/24
"""


class Shape:
    def __init__(self, color):
        """
        object constructor
        :param color: the shape's color
        :type color: str
        """
        self.color = color

    def get_color(self):
        """
        :return: the shape's color
        """
        return self.color

    def set_color(self, color):
        """
        a func that change's the shape's color
        :param color: the color to change to
        :type color: str
        """
        self.color = color

    def calculate_area(self):
        """
        the func gets the needed shape properties and calculates its area. this is an abstract func to indicate that
        each shape subclass has this function.
        """
        pass

    def calculate_perimeter(self):
        """
        the func gets the needed shape properties and calculates its perimeter. this is an abstract func to indicate that
        each shape subclass has this function.
        """
        pass
