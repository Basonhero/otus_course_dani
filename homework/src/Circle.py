import math

from homework.src.Figure import Figure


class Circle(Figure):

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError
        super().__init__(name="Circle")
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return self.radius ** 2 * math.pi
