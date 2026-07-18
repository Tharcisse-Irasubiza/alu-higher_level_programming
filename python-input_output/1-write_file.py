#!/usr/bin/python3
"""Module for writing text files."""


def write_file(filename="", text=""):
    """Writes text to a file and returns number of characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
