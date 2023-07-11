#!/usr/bin/python3
"""Module containing the function append_write"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and returns the number
    of characters added."""
    with open(filename, 'a', encoding="utf-8") as f:
        """This method returns the number of characters appended to a file."""
        return f.write(text)
