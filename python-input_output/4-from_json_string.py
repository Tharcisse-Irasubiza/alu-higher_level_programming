#!/usr/bin/python3
"""Module for converting JSON strings to objects."""


import json


def from_json_string(my_str):
    """Returns Python object represented by JSON string."""
    return json.loads(my_str)
