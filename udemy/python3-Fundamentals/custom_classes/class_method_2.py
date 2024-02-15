from math import pi


class Circle:
    def __init__(self, *, center_x, center_y, radius):
        self.center = center_x, center_y
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def translate(self, *, x, y):
        self.center = (self.center[0] + x, self.center[1] + y)
        return self.__dict__

    def scale(self, *, factor):
        self.radius = self.radius * factor
        return vars(self)


c = Circle(center_x=1,center_y=1,radius=1)
print(f'Center attribute: {vars(c)}')
print(f'Area of the Circle: {c.area()}')

print(f'Translate: {c.translate(x=2,y=2)}')
print(f'Scaled: {c.scale(factor=5)}')


print(f'Center attribute: {c.__dict__}')
print(f'Area of the circle: {c.area()}')
