from homework.src.Figure import Figure


class Triangle(Figure):

    def __init__(self, first, second, third):
        if first <= 0:
            raise ValueError
        if second <= 0:
            raise ValueError
        if third <= 0:
            raise ValueError

        if first >= second + third:
            raise ValueError
        if second >= first + third:
            raise ValueError
        if third >= second + first:
            raise ValueError

        super().__init__(name="Triangle")
        self.first = first
        self.second = second
        self.third = third

    def perimeter(self):
        return self.first + self.second + self.third

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.first) * (p - self.second) * (p - self.third)) ** 0.5
