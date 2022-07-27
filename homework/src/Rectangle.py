from homework.src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, first, second):
        if first <= 0:
            raise ValueError
        if second <= 0:
            raise ValueError
        super().__init__(name="Rectangle")
        self.first = first
        self.second = second

    def perimeter(self):
        return 2 * (self.first + self.second)

    def area(self):
        return self.first * self.second
