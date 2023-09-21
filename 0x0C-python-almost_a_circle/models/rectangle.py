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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
