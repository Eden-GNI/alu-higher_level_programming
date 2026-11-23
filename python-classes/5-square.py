#!/usr/bin/python3
"""Module that defines a class Square that can print itself with #."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a new square with the given size."""
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating its type and value."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #, or an empty line if 0."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
