#!/usr/bin/python3
""" Module for the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize  a Rectangle instance"""

        # Call the super class with id
        super().__init__(id)

        # private instance attributes
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, num):
        """Setter for width"""
        if not isinstance(num, int):
            raise TypeError("width must be an integer")
        if num <= 0:
            raise ValueError("width must be > 0")
        self.__width = num

    @property
    def height(self):
        """Getter for the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, num):
        """Setter for height"""
        if not isinstance(num, int):
            raise TypeError("height must be an integer")
        if num <= 0:
            raise ValueError("height must be > 0")
        self.__height = num

    @property
    def x(self):
        """Getter for the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, num):
        """Setter for x"""
        if not isinstance(num, int):
            raise TypeError("x must be an integer")
        if num < 0:
            raise ValueError("x must be >= 0")
        self.__x = num

    @property
    def y(self):
        """Getter for the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, num):
        """Setter for y"""
        if not isinstance(num, int):
            raise TypeError("y must be an integer")
        if num < 0:
            raise ValueError("y must be >= 0")
        self.__y = num

    def area(self):
        """Calculate and return the area of the rectangle. """
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
