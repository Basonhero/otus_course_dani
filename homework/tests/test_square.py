import pytest

from homework.src.Rectangle import Rectangle
from homework.src.Square import Square


def test_square():
    square = Square(4)

    area = square.area()
    expected_area = 16

    perimeter = square.perimeter()
    expected_perimeter = 16

    assert area == expected_area, f'Area {area} should be equals to {expected_area}'
    assert perimeter == expected_perimeter, f'Perimeter {perimeter} should be equals to {expected_perimeter}'


def test_rectangle_sum():
    square = Square(6)

    area = square.area()
    expected_area = 6 ** 2

    perimeter = square.perimeter()
    expected_perimeter = 6 * 4

    assert area == expected_area, f'Area {area} should be equals to {expected_area}'
    assert perimeter == expected_perimeter, f'Perimeter {perimeter} should be equals to {expected_perimeter}'


def test_two_rect_like_square():
    rect = Rectangle(10, 10)
    square = Square(10)

    assert rect.area() == square.area(), 'Rectangle and square with the same sides should have same area'
    assert rect.perimeter() == square.perimeter(), 'Rectangle and square with the same sides should have same perimeter'


def test_invalid_square():
    with pytest.raises(ValueError):
        invalid = Square(0)
