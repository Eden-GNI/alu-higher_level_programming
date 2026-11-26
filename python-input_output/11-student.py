#!/usr/bin/python3
"""Module that defines a class Student with JSON save and reload methods."""


class Student:
    """A class that defines a student by name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student with a first name, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary description of the student instance.

        If attrs is a list of strings, only those attributes are returned.
        """
        if (isinstance(attrs, list) and
                all(isinstance(a, str) for a in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the student with those in the dict."""
        for key, value in json.items():
            setattr(self, key, value)
