class Figure:

    def __init__(self, name):
        self.name = name

    def perimeter(self):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError
        return self.area() + figure.area()
