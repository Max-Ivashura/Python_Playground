# 20_advanced_topics/main.py

# Пример 1: Метапрограммирование (создание класса на лету)
MyClass = type("MyClass", (), {"x": 10})
obj = MyClass()
print("Значение x:", obj.x)

# Пример 2: Многопоточность
import threading


def worker():
    print("Поток запущен")


thread = threading.Thread(target=worker)
thread.start()
thread.join()

# Пример 3: Ошибка из-за гонки потоков
# x = 0
# def increment():
#     global x
#     for _ in range(100000):
#         x += 1
# threads = [threading.Thread(target=increment) for _ in range(10)]
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
# print("x =", x)  # Результат может быть непредсказуемым
