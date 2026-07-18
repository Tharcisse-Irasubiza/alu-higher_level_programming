#!/usr/bin/python3
"""Module for saving objects as JSON files."""


import json


def save_to_json_file(my_obj, filename):
    """Writes JSON representation of object to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
