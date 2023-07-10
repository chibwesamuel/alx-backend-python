#!/usr/bin/env python3
"""akes an integer max_delay and returns a asyncio.Task."""

import asyncio

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
    wait_random = __import__('0-basic_async_syntax').wait_random

    max_delay = 5
    task = task_wait_random(max_delay)
    print(task.__class__)
