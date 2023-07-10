#!/usr/bin/env python3
"""Test file for printing the correct output of the wait_n coroutine"""
import asyncio
from typing import List

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay value in seconds for each wait_random call.

    Returns:
        List[float]: The list of delays (float values) in ascending order.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)

if __name__ == "__main__":
    wait_random = __import__('0-basic_async_syntax').wait_random

    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
