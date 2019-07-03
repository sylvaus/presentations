"""
Exercise 1

Create a class Rectangle which will be constructed with two values width and height
that the class will store internally.

This class should let the user get the width and the height without being able to set them
Also add a property area that gives the area of the rectangle
"""


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height
