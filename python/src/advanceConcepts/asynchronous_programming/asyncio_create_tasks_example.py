import asyncio
from time import sleep

async def background_task():
    print("call received to coroutine function #0")
    await asyncio.sleep(5)
    print("Background task completed #0")

async def background_task_1():
    print("call received to coroutine function #1")
    await asyncio.sleep(2)
    print("Background task completed #1")

async def background_task_2():
    print("call received to coroutine function #2")
    await asyncio.sleep(2)
    print("Background task completed #2")

async def main():
    task0 = asyncio.create_task(background_task())
    task1 = asyncio.create_task(background_task_1())
    task2 = asyncio.create_task(background_task_2())
    print("Main task in progress")
    sleep(1)
    print("after sleep #1")
    sleep(1)
    print("after sleep #2")
    sleep(1)
    print("after sleep #3")
    await task0  # Wait for the background task to complete
    print("after await task0")
    sleep(1)
    print("after sleep #4")
    await task1  # Wait for the background task to complete
    print("after await task1")    
    sleep(1)
    print("after sleep #5")
    await task2  # Wait for the background task to complete
    print("after await task2")
    sleep(1)
    print("after sleep #6")


if __name__ == "__main__":
    print("we are in main")
    asyncio.run(main())
    print("we are after running event loop")
