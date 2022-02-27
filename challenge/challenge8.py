from cmath import pi
from turtle import circle


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius * pi

circle1 = Circle(7)
print(circle1.area())

class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.height = h

    def area(self):
        return self.bottom * self.height * 0.5

tri = Triangle(5, 8)
print(tri.area())

class Hexagon:
    def __init__(self, l):
        self.line = l

    def area(self):
        return self.line * 6

hex = Hexagon(4)
print(hex.area())