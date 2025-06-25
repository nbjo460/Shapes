from Square import Square
class Triangle(Square):
    def __init__(self, _length : int, _width : int):
        super().__init__(_length, _width)
        self.length = _length
        self.width = _width
        self.name = "Triangle"

    def get_area(self):
        return super().get_area() / 2

    def __sub__(self, other):
        return self.get_area() - other.get_area()

    def __add__(self, other):
        return other.get_area() + self.get_area()

    def __eq__(self, other):
        return other.get_area() == self.get_area()