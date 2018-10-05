"""#Point class representing a point on the asteroids map"""


class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __mul__(self, modifier: float):
        x = self.x * modifier
        y = self.y * modifier
        return Point(x, y)

    '# X is a float between 0 and 1'
    def set_x(self, x):
        if x <= 1 & x >= 0:
            self.x = float(x)

    '# Y is a float between 0 and 1'
    def set_y(self, y):
        if y <= 1 & y >= 0:
            self.y = float(y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
