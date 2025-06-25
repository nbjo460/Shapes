from Shape import Shape
class Square(Shape):
    def __init__(self, _length : int, _width : int, _name = "Square"):
        self.length = _length
        self.width = _width
        self.name = _name

    def get_area(self):
        return self.length * self.width

    def __sub__(self, other):
        return self.get_area() - other.get_area()

    def __add__(self, other):
        return other.get_area() + self.get_area()

    def __eq__(self, other):
        return other.get_area() == self.get_area()