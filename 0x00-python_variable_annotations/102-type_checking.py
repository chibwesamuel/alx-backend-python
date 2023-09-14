#!/usr/bin/env python3
"""
Validates a piece of code and applies changes
"""
from typing import List


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Zooms in on the given list by repeating its elements by a specified factor

    Args:
        lst (List[int]): The input list containing integer elements to be
        zoomed in on.
        factor (int, optional): The factor by which the elements in the list
        will be repeated. Default is 2.

    Returns:
        List[int]: A list containing the zoomed-in elements.

    Example:
        >>> array = [12, 72, 91]
        >>> zoom_2x = zoom_array(array)
        >>> print(zoom_2x)
        [12, 12, 72, 72, 91, 91]

    Note:
        This function takes a list of integers and repeats each element by the
        specified factor to create a new list.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

print(zoom_array.__annotations__)
