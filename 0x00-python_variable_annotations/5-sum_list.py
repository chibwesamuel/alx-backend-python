#!/usr/bin/env python3
"""
Takes a list input_list of floats as argument and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): The input list of floats.

    Returns:
        float: The sum of the floats.
    """
    return sum(input_list)
