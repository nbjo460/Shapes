import math

from Shape import Shape
class Hexagon(Shape):
    def __init__(self, _side : float):
        super().__init__()
        self.side = _side
        self.name = "Hexagon"

    def get_area(self):
        return self.side ** 2 * 3 * math.sqrt(3) * 0.5

    def __sub__(self, other):
        return self.get_area() - other.get_area()

    def __add__(self, other):
        return other.get_area() + self.get_area()

    def __eq__(self, other):
        return other.get_area() == self.get_area()
