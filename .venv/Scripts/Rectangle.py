from Shape import Shape
class Rectangle (Shape):
    def __init__(self, _length: int, _width: int):
        self.length = _length
        self.width = _width
        self.name = "Rectangle"


    def get_area(self):
        return self.length * self.width


    def __sub__(self, other):
        return self.get_area() - other.get_area()


    def __add__(self, other):
        return other.get_area() + self.get_area()


    def __eq__(self, other):
        return other.get_area() == self.get_area()
