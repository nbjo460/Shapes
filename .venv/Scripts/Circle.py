from Shape import Shape
class Circle(Shape):
    Pi = 3.14
    def __init__(self, _radius : float):
        super().__init__()
        self.radius = _radius
        self.name = "Circle"

    def get_area(self):
        return self.radius**2 * Circle.Pi

    def __sub__(self, other):
        return self.get_area() - other.get_area()

    def __add__(self, other):
        return other.get_area() + self.get_area()

    def __eq__(self, other):
        return other.get_area() == self.get_area()