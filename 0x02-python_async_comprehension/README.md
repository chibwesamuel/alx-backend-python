# Python - Async Comprehension

This repository contains Python code demonstrating the usage of async comprehensions and asynchronous generators in a Python back-end application.

## Contents

1. [Async Generator](#async-generator)
2. [Async Comprehensions](#async-comprehensions)
3. [Run Time for Four Parallel Comprehensions](#run-time-for-four-parallel-comprehensions)

## Async Generator

The async_generator module provides a coroutine called `async_generator` that loops 10 times, asynchronously waits for 1 second each time, and yields a random number between 0 and 10. The `random` module is used for generating the random numbers.

Usage example:

```python
import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
```

Output:
```
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]
```

## Async Comprehensions

The async_comprehension module provides a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension over the `async_generator`. It returns the list of 10 random numbers.

Usage example:

```python
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def main():
    print(await async_comprehension())

asyncio.run(main())
```

Output:
```
[9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575, 0.5524750922145316, 8.084266576021555, 8.387128918690468, 1.5486451376520916, 7.713335177885325, 7.673533267041574]
```

## Run Time for Four Parallel Comprehensions

The measure_runtime module imports `async_comprehension` and provides a coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`. It measures the total runtime and returns it.

Usage example:

```python
import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main():
    return await measure_runtime()

print(asyncio.run(main()))
```

Output:
```
10.021936893463135
```

The total runtime is roughly 10 seconds because each invocation of `async_comprehension` takes approximately 1 second, and all four invocations are executed in parallel using `asyncio.gather`.
