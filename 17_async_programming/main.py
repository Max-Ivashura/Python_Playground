# 17_async_programming/main.py

# Пример 1: Асинхронная функция
import asyncio


async def say_hello():
    print("Привет!")
    await asyncio.sleep(1)
    print("Мир!")


asyncio.run(say_hello())

# Пример 2: Ошибка из-за отсутствия await
# async def say_hi():
#     print("Привет!")
#     asyncio.sleep(1)  # Ошибка: функция не будет ждать
#     print("Мир!")
# asyncio.run(say_hi())
