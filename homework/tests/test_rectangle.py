import pytest

from homework.src.Circle import Circle
from homework.src.Rectangle import Rectangle


def test_rectangle_horizontal():
    rectangle = Rectangle(2, 4)

    area = rectangle.area()
    expected_area = 8

    perimeter = rectangle.perimeter()
    expected_perimeter = 12

    assert area == expected_area, f'Area {area} should be equals to {expected_area}'
    assert perimeter == expected_perimeter, f'Perimeter {perimeter} should be equals to {expected_perimeter}'


def test_rectangle_vertical():
    rectangle = Rectangle(6, 2)

    area = rectangle.area()
    expected_area = 12

    perimeter = rectangle.perimeter()
    expected_perimeter = 16

    assert area == expected_area, f'Area {area} should be equals to {expected_area}'
    assert perimeter == expected_perimeter, f'Perimeter {perimeter} should be equals to {expected_perimeter}'


def test_rectangle_square():
    rectangle = Rectangle(6, 6)

    area = rectangle.area()
    expected_area = 36

    perimeter = rectangle.perimeter()
    expected_perimeter = 24

    assert area == expected_area, f'Area {area} should be equals to {expected_area}'
    assert perimeter == expected_perimeter, f'Perimeter {perimeter} should be equals to {expected_perimeter}'


def test_rectangle_vertical_sum():
    rectangle = Rectangle(6, 2)

    area = rectangle.area()
    expected_area = 6 * 2

    perimeter = rectangle.perimeter()
    expected_perimeter = (6 + 2) * 2

    assert area == expected_area, f'Area {area} should be equals to {expected_area}'
    assert perimeter == expected_perimeter, f'Perimeter {perimeter} should be equals to {expected_perimeter}'


def test_invalid_rectangle_zero_vertical():
    with pytest.raises(ValueError):
        invalid = Rectangle(0, 4)


def test_invalid_rectangle_zero_horizontal():
    with pytest.raises(ValueError):
        invalid = Rectangle(4, 0)


def test_area_addition_rectangle():
    rect = Rectangle(3, 4)
    circle = Circle(2)

    expected_area = rect.area() + circle.area()
    area = rect.add_area(circle)

    assert area == expected_area, f"Area {area} should be {expected_area}"
