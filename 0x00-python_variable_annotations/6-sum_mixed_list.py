#!/usr/bin/env python3
"""
Takes a list mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculate the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The input list of integers
        and floats.

    Returns:
        float: The sum of the integers and floats.
    """
    return sum(mxd_lst)
