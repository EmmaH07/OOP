from rectangle import Rectangle
from square import Square
from circle import Circle
import random


COLOR_LST = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']
MIN_LENGTH = 1
MAX_LENGTH = 20


class Container:
    def __init__(self):
        """
        Container constructor - creates an empty list
        """
        self.shape_lst = []

    def generate(self, x):
        """
        generates x amount of shapes. the shapes are either a circle, a square, or a rectangle
        :param x: the amount of shapes to add to the list
        :type x: int
        """
        for i in range(x):
            color_index = random.randint(0, 5)
            num = random.randint(0, 3)

            if num == 0:
                length = random.randint(MIN_LENGTH, MAX_LENGTH + 1)
                width = random.randint(MIN_LENGTH, MAX_LENGTH + 1)
                while width == length:
                    width = random.randint(MIN_LENGTH, MAX_LENGTH + 1)
                new_shape = Rectangle(COLOR_LST[color_index], length, width)
                self.shape_lst.append(new_shape)

            elif num == 1:
                length = random.randint(MIN_LENGTH, MAX_LENGTH + 1)
                new_shape = Square(COLOR_LST[color_index], length)
                self.shape_lst.append(new_shape)

            else:
                r = random.randint(MIN_LENGTH, MAX_LENGTH + 1)
                new_shape = Circle(COLOR_LST[color_index], r)
                self.shape_lst.append(new_shape)

    def sum_areas(self):
        """
        a func that calculates the sum of the shape areas in the container
        :return: the sum of the shape areas in the container
        """
        area_sum = 0
        for i in range(len(self.shape_lst)):
            area_sum += self.shape_lst[i].calculate_area()
        return area_sum

    def sum_perimeters(self):
        """
        a func that calculates the sum of the shape perimeters in the container
        :return: the sum of the shape perimeters in the container
        """
        perimeter_sum = 0
        for i in range(len(self.shape_lst)):
            perimeter_sum += self.shape_lst[i].calculate_perimeter()
        return perimeter_sum

    def count_colors(self):
        """
        a func that counts how many times each color appears and saves the counts in a dictionary.
        :return: a dictionary with colors as keys and the amount of times each color appears as values.
        """
        count_dict = {'Red': 0, 'Orange': 0, 'Yellow': 0, 'Green': 0, 'Blue': 0, 'Purple': 0}
        for i in range(len(self.shape_lst)):
            color = str(self.shape_lst[i].get_color())
            if color in count_dict.keys():
                count_dict[color] += 1
        return count_dict
