#!/usr/bin/python3
"""Module for loading JSON files."""


import json


def load_from_json_file(filename):
    """Creates Python object from JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
