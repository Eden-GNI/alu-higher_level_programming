#!/usr/bin/python3
"""Module that defines a class Square with a private size attribute."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size):
        """Initialize a new square with the given size."""
        self.__size = size
