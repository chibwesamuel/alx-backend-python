#!/usr/bin/env python3
"""
Collect 10 random numbers using an async comprehensing
then return the 10 random numbers
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    This coroutine collects 10 random numbers
    Returns: List[float]: A list of 10 random numbers.
    """
    return [i async for i in async_generator()]