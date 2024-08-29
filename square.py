"""
Author: Emma Harel
Program name: square
Description: A square class that is a subclass of the class 'rectangle'
Date: 27/08/24
"""

from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, color, length):
        """
        object constructor
        :param color: the shape's color
        :type color: str
        :param length: the square's length
        :type length: float
        """
        super().__init__(color, length, length)

    def get_color(self):
        """
        :return: the square's color
        """
        return self.color

    def set_color(self, color):
        """
        a func that change's the square's color
        :param color: the color to change to
        :type color: str
        """
        self.color = color

    def calculate_area(self):
        """
        a func that calculates the square's area
        :return: the square's area
        """
        return super().calculate_area()

    def calculate_perimeter(self):
        """
        a func that calculates the square's perimeter
        :return: the square's perimeter
        """
        return super().calculate_perimeter()

    def __add__(self, rec):
        """
        a func the sums two rectangle objects (a square is a type of rectangle)
        :param rec: a rectangle object
        :type rec: Rectangle
        :return: a new rectangle object that is a sum of two rectangle objects
        """
        return super().__add__(rec)

    def __str__(self):
        """
        a func that dictates how to print square object.
        :return: the str to print
        """
        s = 'Shape type: Square \r\n' + 'Color: ' + self.color + '\r\n' + 'Length: ' + str(self.length)
        return s
