"""
Define a class named Rectangle which can be constructed by a length and width.
The Rectangle class has a method which can compute the area.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def compute_area(self):
        return self.width * self.height


rec1 = Rectangle(4, 7)
print(rec1.compute_area())
