#!/usr/bin/python3
"""Module that defines a class Square with its own string description."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square defined by a private size."""

    def __init__(self, size):
        """Initialize a square after validating size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the description: [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
