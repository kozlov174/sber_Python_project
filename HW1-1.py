from abc import abstractmethod
import math


class Shape:
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius ^ 2) * math.pi


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

if __name__ == '__main__':
    circle = Circle(10)
    print(circle.area())
    rectangle = Rectangle(10, 5)
    print(rectangle.area())
