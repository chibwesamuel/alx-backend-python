#!/usr/bin/env python3
"""Alter it into a new function task_wait_n."""

import asyncio
from typing import List

# Import task_wait_random function
from my_module import task_wait_random


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates and returns a list of asyncio.Tasks that execute task_wait_random
    with the specified max_delay.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay value in seconds for
        task_wait_random.

    Returns:
        List[float]: The list of delays (float values) in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return asyncio.run(asyncio.gather(*tasks))


if __name__ == "__main__":
    # Import task_wait_random function
    from my_module import task_wait_random

    n = 5
    max_delay = 6
    print(task_wait_n(n, max_delay))

