#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, num):
        if not isinstance(num, int):
            raise TypeError("width must be an integer")
        if num < 0:
            raise ValueError("width must be >= 0")
        self.__width = num

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, num):
        if not isinstance(num, int):
            raise TypeError("height must be an integer")
        if num < 0:
            raise ValueError("height must be >= 0")
        self.__height = num

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = ['#' * self.__width for _ in range(self.__height)]
        return ("\n".join(rectangle))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return (f"Rectangle({self.__width}, {self.__height})")
