class Point:
    def __init__(self,*coords):
        self.coordinates = coords
        print(f'Dimension: {len(coords)}')

p1 = Point(1,2,3,4,5)
print(f'Coordinates Values:{p1.coordinates}')