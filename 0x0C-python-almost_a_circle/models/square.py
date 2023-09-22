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

    def update(self, *args, **kwargs):
        """Update the Square's attributes
        based on arguments and keyword arguments."""

        if args:
            # Check if there are arguments and assign them accordingly
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            # If no *args, use **kwargs if provided
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def __str__(self):
        """Return a string representation of the Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """Return a dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
