#!/usr/bin/env python3
"""
Validates a piece of code and applies changes
"""
from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms in on the given tuple by repeating its elements by a specified factor.

    Args:
        lst (Tuple[int, ...]): The input tuple containing integer elements to
        be zoomed in on.
        factor (int, optional): The factor by which the elements in the tuple
        will be repeated. Default is 2.

    Returns:
        List[int]: A list containing the zoomed-in elements.

    Example:
        >>> array = (12, 72, 91)
        >>> zoom_2x = zoom_array(array)
        >>> print(zoom_2x)
        [12, 12, 72, 72, 91, 91]

    Note:
        This function takes a tuple of integers and repeats each element by
        the specified factor to create a new list.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

print(zoom_array.__annotations__)
