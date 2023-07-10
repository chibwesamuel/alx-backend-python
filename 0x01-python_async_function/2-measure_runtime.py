#!/usr/bin/env python3
"""Measures the total execution time for wait_n, returns total_time/n"""
import time
from typing import Callable

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns total_time / n.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay value in seconds for each wait_n call.

    Returns:
        float: The average execution time per call in seconds.
    """
    start_time = time.time()
    wait_n(n, max_delay)
    end_time = time.time()

    total_time = end_time - start_time
    average_time = total_time / n

    return average_time

if __name__ == "__main__":
    wait_n = __import__('1-concurrent_coroutines').wait_n

    n = 5
    max_delay = 9

    print(measure_time(n, max_delay))
