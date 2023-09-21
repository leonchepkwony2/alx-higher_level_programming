#!/usr/bin/python3
""" Module for the Base class"""


class Base:
    """ Base class for managing id attribute """


__nb_objects = 0


def __init__(self, id=None):
    """ Constructor method """

    # If id is provided, set it as the instance's id
    if id is not None:
        self.id = id
    else:
        # If id is not provided, increment the class attribute
        # __nb_objects and set it as the instance's id
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
