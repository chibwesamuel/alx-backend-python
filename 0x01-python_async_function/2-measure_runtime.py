#!/usr/bin/env python3
import time
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and
    returns total_time / n.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay value in seconds for
        each wait_n call.

    Returns:
        float: The average execution time per call in seconds.
    """
    start_time = time.time()
    
    # Call wait_n function 'n' times
    for _ in range(n):
        wait_n(max_delay)
    
    end_time = time.time()

    total_time = end_time - start_time
    average_time = total_time / n

    return average_time

if __name__ == "__main__":
    n = 5
    max_delay = 9

    print("Approximate elapsed time falls within an acceptable range:",
            0 <= measure_time(n, max_delay) <= max_delay * 1.02)
