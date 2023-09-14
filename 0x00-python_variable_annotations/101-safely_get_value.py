#!/usr/bin/env python3
"""
Add type annotations to the function
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]
        = None) -> Union[Any, T]:
    """Safely get the value from a dictionary.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to lookup in the dictionary.
        default (Union[T, None], optional): The default value to return if
        the key is not found.
        Defaults to None.

    Returns:
        Union[Any, T]: The value corresponding to the key in the dictionary,
        or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
