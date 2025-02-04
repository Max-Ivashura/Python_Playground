import asyncio

import aiohttp


async def hello(name):
    print("Hello,", name)
    await asyncio.sleep(1)


import asyncio


async def task1():
    await asyncio.sleep(2)
    print("Задача 1 выполнена")


async def task2():
    await asyncio.sleep(1)
    print("Задача 2 выполнена")


async def main_task2():
    await asyncio.gather(task1(), task2())


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main_task3():
    url = "https://www.example.com"
    content = await fetch(url)
    print("Содержимое страницы:", content[:200])  # Выводим первые 200 символов


async def timer(seconds):
    print(f"Таймер запущен на {seconds} секунд...")
    await asyncio.sleep(seconds)
    print("Таймер завершен!")


async def main_task4():
    await timer(5)


async def worker(name, delay):
    print(f"{name} начал работу")
    await asyncio.sleep(delay)
    print(f"{name} завершил работу через {delay} секунд")

async def main_task5():
    tasks = [
        worker("Задача 1", 3),
        worker("Задача 2", 2),
        worker("Задача 3", 1)
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(hello("Max"))
    asyncio.run(main_task2())
    asyncio.run(main_task3())
    asyncio.run(main_task4())
    asyncio.run(main_task5())
