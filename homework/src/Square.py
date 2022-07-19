from homework.src.Figure import Figure


class Square(Figure):

    def __init__(self, side):
        if side <= 0:
            raise ValueError
        super().__init__(name="Square")
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2
