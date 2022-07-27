import math

import pytest

from homework.src.Circle import Circle
from homework.src.Square import Square

radius = 2.777


def test_circle_first():
    radius = 2.777
    circle = Circle(radius)

    area = circle.area()
    expected_area = math.pi * radius ** 2

    perimeter = circle.perimeter()
    expected_perimeter = 2 * math.pi * radius

    assert area == expected_area, f'Area {area} should be equals to {expected_area}'
    assert perimeter == expected_perimeter, f'Perimeter {perimeter} should be equals to {expected_perimeter}'


def test_circle_second():
    circle = Circle(10)

    area = circle.area()
    expected_area = 314.1592653589793

    perimeter = circle.perimeter()
    expected_perimeter = 62.83185307179586

    assert area == expected_area, f'Area {area} should be equals to {expected_area}'
    assert perimeter == expected_perimeter, f'Perimeter {perimeter} should be equals to {expected_perimeter}'


def test_circle():
    circle = Circle(10)

    area = circle.area()
    expected_area = math.pi * 100

    perimeter = circle.perimeter()
    expected_perimeter = 2 * math.pi * 10

    assert area == expected_area, f'Area {area} should be equals to {expected_area}'
    assert perimeter == expected_perimeter, f'Area {perimeter} should be equals to {expected_perimeter}'


def test_invalid_circle():
    with pytest.raises(ValueError):
        invalid = Circle(-1)


def test_invalid_circle_zero():
    with pytest.raises(ValueError):
        invalid = Circle(0)
        assert invalid.area() == 0, "Point should have area equals to 0"
        assert invalid.perimeter() == 0, "Point should have perimeter equals to 0"


def test_area_addition_rectangle():
    circle = Circle(2.34)
    square = Square(10)

    expected_area = square.area() + circle.area()
    area = square.add_area(circle)

    assert area == expected_area, f"Area {area} should be {expected_area}"
