#!/usr/bin/python3
"""Defines a file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
