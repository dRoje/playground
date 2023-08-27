import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, "hello")
    print("first task is done")
    await say_after(2, "world")

    print(f"finished at {time.strftime('%X')}")


async def main_2():
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))

    print(f"started at {time.strftime('%X')}")

    # both tasks start at once
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
asyncio.run(main_2())
