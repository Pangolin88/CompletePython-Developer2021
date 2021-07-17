"""
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return self.radius ** 2 * 3.1416


circle1 = Circle(4)
print(circle1.compute_area())
