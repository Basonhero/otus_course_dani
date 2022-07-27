import pytest

from homework.src.Square import Square
from homework.src.Triangle import Triangle


def test_egypt_triangle():
    egypt_triangle = Triangle(3, 4, 5)

    area = egypt_triangle.area()
    expected_area = 6

    perimeter = egypt_triangle.perimeter()
    expected_perimeter = 12

    assert area == expected_area, f'Area {area} should be equals to {expected_area}'
    assert perimeter == expected_perimeter, f'Perimeter {perimeter} should be equals to {expected_perimeter}'


def test_rectangle_triangle():
    rect_triangle = Triangle(29, 21, 20)

    area = rect_triangle.area()
    expected_area = 210

    perimeter = rect_triangle.perimeter()
    expected_perimeter = 70

    assert area == expected_area, f'Area {area} should be equals to {expected_area}'
    assert perimeter == expected_perimeter, f'Perimeter {perimeter} should be equals to {expected_perimeter}'


def test_equal_side_triangle():
    eq_triangle = Triangle(1, 1, 1)

    area = eq_triangle.area()
    expected_area = (3 ** 0.5) / 4

    perimeter = eq_triangle.perimeter()
    expected_perimeter = 3

    assert area == expected_area, f'Area {area} should be equals to {expected_area}'
    assert perimeter == expected_perimeter, f'Perimeter {perimeter} should be equals to {expected_perimeter}'


def test_invalid_sides_triangle():
    with pytest.raises(ValueError):
        invalid = Triangle(1, 2, 3)


def test_invalid_side_triangle():
    with pytest.raises(ValueError):
        invalid = Triangle(1, 2, 0)


def test_area_addition_triangle():
    egypt_triangle = Triangle(3, 4, 5)
    square = Square(2)

    expected_area = egypt_triangle.area() + square.area()
    area = egypt_triangle.add_area(square)

    assert area == expected_area, f"Area {area} should be {expected_area}"
