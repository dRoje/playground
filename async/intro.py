import asyncio

"""
A coroutine is a special type of function that allows you to pause its execution at a certain point and later 
resume it from where it left off. When a coroutine is paused using await, it gives control back to the event loop, 
allowing other tasks to run in the meantime. Event loop manages the execution of coroutines and ensures proper 
scheduling.

In this example, the my_coroutine function is a coroutine that pauses execution for 2 seconds using 
await asyncio.sleep(2). While waiting, the event loop can handle other tasks concurrently. 
"""


async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(2)  # Pause execution for 2 seconds
    print("Coroutine resumed after pause")


async def main():
    print("Main function started")
    await my_coroutine()
    print("Main function finished")


asyncio.run(main())
