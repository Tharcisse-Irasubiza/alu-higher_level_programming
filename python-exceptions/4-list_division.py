#!/usr/bin/python3
"""Module that defines list_division."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element 2 lists.

    Args:
        my_list_1 (list): first list, can contain any type.
        my_list_2 (list): second list, can contain any type.
        list_length (int): the length of the list to return. Can be
        bigger than the length of both lists.

    Returns:
        list: a new list of length list_length with the result of
        each division. If a division can't be performed (wrong
        type, division by 0, or index out of range), the result for
        that position is 0.
    """
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
