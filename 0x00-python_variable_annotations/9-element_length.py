#!/usr/bin/env python3
"""
Return values with the appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each element in a list.

    Args:
        lst (Iterable[Sequence]): The input list.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
                                    the element from the input list and its
                                    length.
    """
    return [(i, len(i)) for i in lst]
