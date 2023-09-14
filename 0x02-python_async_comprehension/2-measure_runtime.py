#!/usr/bin/env python3
"""Execute async_comprehension four times in parallel using asyncio.gather"""

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This coroutine executes async_comprehension four times in parallel
    It measures the total runtime of the four executions and returns it.

    Returns: float: The total runtime in seconds
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
