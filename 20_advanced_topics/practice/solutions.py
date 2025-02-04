import threading
import multiprocessing
import time

# 1. Создание класса на лету с помощью type
DynamicClass = type("DynamicClass", (object,), {"hello": lambda self: "Привет от DynamicClass!"})
dynamic_instance = DynamicClass()
print(dynamic_instance.hello())

# 2. Многопоточность
def thread_task(name):
    print(f"Поток {name} запущен")
    time.sleep(2)
    print(f"Поток {name} завершен")

thread1 = threading.Thread(target=thread_task, args=("A",))
thread2 = threading.Thread(target=thread_task, args=("B",))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Многопоточность завершена")

# 3. Многопроцессорность
def process_task(name):
    print(f"Процесс {name} запущен")
    time.sleep(2)
    print(f"Процесс {name} завершен")

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=process_task, args=("1",))
    process2 = multiprocessing.Process(target=process_task, args=("2",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Многопроцессорность завершена")

    # 4. Использование метакласса
    class MetaClass(type):
        def __new__(cls, name, bases, dct):
            dct["meta_attribute"] = "Добавлено через метакласс"
            return super().__new__(cls, name, bases, dct)

    class CustomClass(metaclass=MetaClass):
        pass

    custom_instance = CustomClass()
    print(custom_instance.meta_attribute)

    # 5. Дескрипторы для управления доступом
    class Descriptor:
        def __init__(self, name):
            self.name = "_" + name

        def __get__(self, instance, owner):
            return getattr(instance, self.name, None)

        def __set__(self, instance, value):
            if isinstance(value, str) and len(value) > 2:
                setattr(instance, self.name, value)
            else:
                raise ValueError("Имя должно быть строкой длиннее 2 символов")

    class Person:
        name = Descriptor("name")

        def __init__(self, name):
            self.name = name

    person = Person("Алиса")
    print(person.name)

    try:
        person.name = "X"
    except ValueError as e:
        print(e)
