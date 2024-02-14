class Circle:
    def __init__(self,*,radius=1):
        if radius <=0:
            raise ValueError('Circle Radius cannot be zero or Negative')
        self.radius = radius
c = Circle(radius=10)
print(vars(c))