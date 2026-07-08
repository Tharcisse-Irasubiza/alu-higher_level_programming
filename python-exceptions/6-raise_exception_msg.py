#!/usr/bin/python3
"""Module that defines raise_exception_msg."""


def raise_exception_msg(message=""):
    """Raise a NameError exception with a message.

    Args:
        message (str): the message to attach to the exception.
    """
    raise NameError(message)
