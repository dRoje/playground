import asyncio
import time
from datetime import datetime

from fastapi import FastAPI

app = FastAPI()


async def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


@app.get("/async_blocking")
async def async_blocking():
    start_time = time.time()
    await asyncio.sleep(5)  # doesn't block
    # time.sleep(5)  # blocks
    # await calculate_factorial(200000) # blocks
    end_time = time.time()
    duration = end_time - start_time
    return {
        "start_time": datetime.fromtimestamp(start_time).strftime("%H:%M:%S"),
        "end_time": datetime.fromtimestamp(end_time).strftime("%H:%M:%S"),
        "duration": round(duration, 2),
    }


@app.get("/sync_blocking")
def sync_blocking():
    start_time = time.time()
    time.sleep(5)  # doesn't block
    # await calculate_factorial(200000) # blocks
    end_time = time.time()
    duration = end_time - start_time
    return {
        "start_time": datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S"),
        "end_time": datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S"),
        "duration": duration,
    }
