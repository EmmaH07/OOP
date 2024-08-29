"""
Author: Emma Harel
Program name: main
Description: the main program
Date: 27/08/24
"""

from container import Container
from rectangle import Rectangle
from square import Square
from circle import Circle


def check_main():
    check_container = Container()
    check_container.generate(20)
    assert check_container.sum_areas() > 0
    assert check_container.sum_perimeters() > 0
    color_dict = check_container.count_colors()
    for count in color_dict.values():
        assert count >= 0


def check_rectangle():
    rec = Rectangle('Red', 4, 7)
    assert rec.calculate_area() > 0
    assert rec.calculate_perimeter() > 0
    rec.set_color('Blue')
    assert rec.get_color() == 'Blue'


def check_square():
    s = Square('Pink', 8)
    assert s.calculate_perimeter() > 0
    assert s.calculate_area() > 0
    s.set_color('Purple')
    assert s.get_color() == 'Purple'


def check_circle():
    circ = Circle('Yellow', 3)
    assert circ.calculate_area() > 0
    assert circ.calculate_perimeter() > 0
    circ.set_color('Orange')
    assert circ.get_color() == 'Orange'


def main():
    my_container = Container()
    my_container.generate(100)
    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_perimeters())
    print("colors:", my_container.count_colors())


if __name__ == '__main__':
    check_main()
    check_rectangle()
    check_circle()
    check_square()
    main()
