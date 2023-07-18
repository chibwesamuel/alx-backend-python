#!/usr/bin/env python3
"""Makes an integer max_delay and returns an asyncio.Task."""

import asyncio
# Import wait_random function
from my_module import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that executes wait_random with the specified max_delay.

    Args:
        max_delay (int): The maximum delay value in seconds for wait_random.

    Returns:
        asyncio.Task: The created asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))

if __name__ == "__main__":
    # Import wait_random function
    from my_module import wait_random

    max_delay = 5
    task = task_wait_random(max_delay)
    print(task.__class__)

