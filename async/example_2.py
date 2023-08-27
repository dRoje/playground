import asyncio
import functools
import time
from datetime import datetime


def log_async_function_execution(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        start_time_str = datetime.fromtimestamp(start_time).strftime("%H:%M:%S.%f")[:-3]
        print(f"[{start_time_str}] {func.__name__} START")

        result = await func(*args, **kwargs)

        end_time = time.time()
        end_time_str = datetime.fromtimestamp(end_time).strftime("%H:%M:%S.%f")[:-3]
        duration = end_time - start_time
        print(
            f"[{end_time_str}] {func.__name__} END (Duration: {duration:.2f} seconds)"
        )
        return result

    return wrapper


@log_async_function_execution
async def async_calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


@log_async_function_execution
async def async_connect():
    await asyncio.sleep(2)


@log_async_function_execution
async def async_send_request():
    await asyncio.sleep(2)


@log_async_function_execution
async def async_main():
    """
    If you don't use asyncio.gather and instead use individual await statements to await each async task sequentially,
    the tasks will be executed one after the other, effectively blocking the execution of subsequent tasks until the
    previous one completes. This approach eliminates the concurrency benefits that async code provides.
    """

    # await async_connect()
    # await async_send_request()
    # await async_calculate_factorial(120000)

    await asyncio.gather(
        async_connect(), async_send_request(), async_calculate_factorial(120000)
    )


if __name__ == "__main__":
    asyncio.run(async_main())
