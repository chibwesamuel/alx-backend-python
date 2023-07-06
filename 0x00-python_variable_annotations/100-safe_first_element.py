#!/usr/bin/env python3

from typing import Sequence, Any, Union, Optional

def safe_first_element(lst: Sequence[Any]) -> Union[Any, Optional[None]]:
    """Return the first element of a list safely.

    Args:
        lst (Sequence[Any]): The input list.

    Returns:
        Union[Any, Optional[None]]: The first element of the list, or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

