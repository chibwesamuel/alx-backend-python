#!/usr/bin/env python3
"""Coroutine loops 10 times then yields a random number between 0 and 10"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generate random numbers asynchronously.
    
    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
