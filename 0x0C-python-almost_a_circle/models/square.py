#!/usr/bin/python3
""" Module for the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance"""

        # Call the super class with id, x, y, width, and height
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size of the Square."""
        return self.width

    @size.setter
    def size(self, size):
        """Setter for size, which also updates width and height."""
        self.width = size
        self.height = size

    def __str__(self):
        """Return a string representation of the Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
