# Python - Async

This repository contains Python code that demonstrates asynchronous programming concepts using the `async` and `await` syntax, as well as the `asyncio` module. It also covers the usage of concurrent coroutines, creating asyncio tasks, and utilizing the random module.

## Table of Contents

1. [The Basics of Async](#the-basics-of-async)
2. [Executing Multiple Coroutines Concurrently](#executing-multiple-coroutines-concurrently)
3. [Measuring Runtime](#measuring-runtime)
4. [Tasks](#tasks)

## The Basics of Async

In this section, we explore the fundamentals of async programming. The `0-basic_async_syntax.py` file contains an asynchronous coroutine called `wait_random`. It takes an optional integer argument `max_delay` (default value: 10) and waits for a random delay between 0 and `max_delay` (inclusive) seconds. The coroutine eventually returns the delay.

To execute and test the `wait_random` coroutine, use the provided `0-main.py` script. It imports `wait_random` and demonstrates its usage by calling it with different arguments.

```bash
$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
```

## Executing Multiple Coroutines Concurrently

In this section, we learn how to execute multiple coroutines concurrently using the `async` approach. The `1-concurrent_coroutines.py` file introduces an async routine called `wait_n`. It takes two integer arguments, `n` and `max_delay`, and spawns `wait_random` `n` times with the specified `max_delay`.

The `wait_n` routine returns a list of all the delays (float values) in ascending order without using the `sort()` function due to concurrency limitations.

To test the `wait_n` routine, use the provided `1-main.py` script. It imports `wait_n` and demonstrates its usage by calling it with different arguments.

```bash
$ ./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```

Please note that the output may vary slightly.

## Measuring Runtime

In this section, we demonstrate how to measure the runtime of a coroutine. The `2-measure_runtime.py` file imports `wait_n` from the previous section and defines a `measure_time` function. The function takes two integer arguments, `n` and `max_delay`, and measures the total execution time for `wait_n(n, max_delay)`. It returns the average time per execution as a float.

To measure the runtime, use the provided `2-main.py` script. It imports `measure_time` and demonstrates its usage by calling it with predefined values for `n` and `max_delay`.

```bash
$ ./2-main.py
1.759705400466919
```

## Tasks

In this section, we explore the creation of asyncio tasks using regular function syntax. The `3-tasks.py` file imports `wait_random` from `0-basic_async_syntax` and defines a function called `task_wait_random`. The function takes an integer `max_delay` as an argument and returns an `asyncio.Task`.

To test the `task_wait_random` function, use the provided `3-main.py` script. It demonstrates the creation and execution of an asyncio task by calling `task_wait_random` with a specified `max_delay`.

```bash
$ ./3-main.py
<class '_asyncio.Task'>
```

## Tasks with Multiple Coroutines

In this section, we modify the previous code to create a new function called `task_wait_n`. The `4-tasks.py` file defines the `task_wait_n` function, which is similar to `wait_n` from the second section. However, instead of calling `wait_random`, it creates asyncio tasks using `task_wait_random`.

To test the `task_wait_n` function, use the provided `4-main.py` script. It demonstrates the creation and execution of asyncio tasks by calling `task_wait_n` with specified values for `n` and `max_delay`.

```bash
$ ./4-main.py
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
```
