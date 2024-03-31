import asyncio
import time
from datetime import datetime
from functools import wraps

import httpx
from fastapi import FastAPI

app = FastAPI()

test_file_path = "/home/duje/PycharmProjects/playground/files/bigfile.txt"
url_list = [
    "https://reddit.com",
    "https://google.com",
    "https://wikipedia.org/",
    "https://www.youtube.com/",
    "https://www.facebook.com/",
    "https://www.instagram.com/",
    "https://www.twitch.tv/",
    "https://www.yahoo.com/",
    "https://www.amazon.com/",
    "https://reddit.com",
    "https://google.com",
    "https://wikipedia.org/",
    "https://www.youtube.com/",
    "https://www.facebook.com/",
    "https://www.instagram.com/",
    "https://www.twitch.tv/",
    "https://www.yahoo.com/",
    "https://www.amazon.com/",
]


async def send_request_through_httpx() -> float:
    """Non-blocking IO-bound function - sending network requests"""
    st = time.time()
    async with httpx.AsyncClient() as client:
        tasks = []
        for url in url_list:
            tasks.append(client.get(url))
        responses = await asyncio.gather(*tasks)
        for r in responses:
            print(r.status_code)

    fin = time.time() - st
    return fin


async def send_request_through_httpx_blocking() -> float:
    """Blocking IO-bound function - sending network requests"""
    st = time.time()
    async with httpx.AsyncClient() as client:
        for url in url_list:
            r = await client.get(url)
            print(r.status_code)

    fin = time.time() - st
    return fin


def send_request_through_requests_sync() -> float:
    """Blocking IO-bound function - sending network requests"""
    st = time.time()
    for url in url_list:
        r = httpx.get(url)  # same as requests.get(url)
        print(r.status_code)
    fin = time.time() - st
    return fin


async def send_request_async_but_should_be_sync() -> float:
    """Blocking IO-bound function - sending network requests"""
    st = time.time()
    for url in url_list:
        r = httpx.get(url)  # same as requests.get(url)
        print(r.status_code)
    fin = time.time() - st


def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


async def calculate_factorial_async(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


@app.get("/async_calculate")
async def async_calculate():
    start_time = time.time()
    # calculate_factorial(200000)  # blocks hello
    await calculate_factorial_async(200000)  # blocks hello
    end_time = time.time()
    duration = end_time - start_time
    return {
        "start_time": datetime.fromtimestamp(start_time).strftime("%H:%M:%S"),
        "end_time": datetime.fromtimestamp(end_time).strftime("%H:%M:%S"),
        "duration": round(duration, 2),
    }


@app.get("/sync_calculate")
def sync_calculate():  # does not block hello
    start_time = time.time()
    calculate_factorial(200000)
    end_time = time.time()
    duration = end_time - start_time
    return {
        "start_time": datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S"),
        "end_time": datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S"),
        "duration": duration,
    }


@app.get("/wrongly_used_async_send_request")
async def wrongly_used_async_send_request():
    """Using async word for sync function."""
    # very slow and blocks hello
    start_time = time.time()
    await send_request_async_but_should_be_sync()
    # blocks hello wait for the whole method to finish
    end_time = time.time()
    duration = end_time - start_time
    return {
        "start_time": datetime.fromtimestamp(start_time).strftime("%H:%M:%S"),
        "end_time": datetime.fromtimestamp(end_time).strftime("%H:%M:%S"),
        "duration": round(duration, 2),
    }


@app.get("/not_really_async_send_request")
async def not_really_async_send_request():
    """Doesn't use gather for tasks."""
    # slow but doesn't block hello
    start_time = time.time()
    await send_request_through_httpx_blocking()
    # this doesn't block hello because at least the http client is async,
    # so it gets released while waiting for the response
    end_time = time.time()
    duration = end_time - start_time
    return {
        "start_time": datetime.fromtimestamp(start_time).strftime("%H:%M:%S"),
        "end_time": datetime.fromtimestamp(end_time).strftime("%H:%M:%S"),
        "duration": round(duration, 2),
    }


@app.get("/truly_async_send_request")
async def truly_async_send_request():
    """Gathers task before execution."""
    # fast and doesn't block hellp
    start_time = time.time()
    await send_request_through_httpx()
    end_time = time.time()
    duration = end_time - start_time
    return {
        "start_time": datetime.fromtimestamp(start_time).strftime("%H:%M:%S"),
        "end_time": datetime.fromtimestamp(end_time).strftime("%H:%M:%S"),
        "duration": round(duration, 2),
    }


@app.get("/sync_send_request")
def sync_send_request():
    """Send a request synchronously."""
    # slow, but doesn't hello
    start_time = time.time()
    send_request_through_requests_sync()
    end_time = time.time()
    duration = end_time - start_time
    return {
        "start_time": datetime.fromtimestamp(start_time).strftime("%H:%M:%S"),
        "end_time": datetime.fromtimestamp(end_time).strftime("%H:%M:%S"),
        "duration": round(duration, 2),
    }


@app.get("/hello")
def hello():
    return {"message": "Hello World"}
