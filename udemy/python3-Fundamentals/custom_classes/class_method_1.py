from math import pi


class Circle:
    def __init__(self, *, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


c = Circle(radius=1)
print(f'Area of the Circle: {c.area()}')
