#!/usr/bin/env python3
"""Test file for printing the correct output of the wait_n coroutine"""
import asyncio
from typing import List
from random import random
import datetime


async def wait_random(max_delay: int) -> float:
    """
    Asynchronous routine that waits for a random delay between 0 and max_delay.

    Args:
        max_delay (int): The maximum delay value in seconds.

    Returns:
        float: The random delay value.
    """
    delay = random() * max_delay
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with
    the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay value in seconds for each
        wait_random call.

    Returns:
        List[float]: The list of delays (float values) in ascending order.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)


if __name__ == "__main__":
    asyncio.run(wait_n(5, 5))
    asyncio.run(wait_n(10, 7))
    asyncio.run(wait_n(10, 0))

