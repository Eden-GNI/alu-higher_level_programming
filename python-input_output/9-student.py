#!/usr/bin/python3
"""Module that defines a class Student."""


class Student:
    """A class that defines a student by name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student with a first name, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary description of the student instance."""
        return self.__dict__
