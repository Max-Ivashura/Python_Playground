import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


def get_site(url):
    get_params = {"param1": "value1"}
    response = requests.get(url, get_params)
    return response.url


def task2():
    array = np.array([1, 2, 3])
    return array


def task3():
    # Читаем CSV-файл
    try:
        df = pd.read_csv('data.csv')
        print(df.head())
    except Exception as ex:
        print(ex)


def task4():
    # Генерируем данные
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Создаем график
    plt.plot(x, y, label='sin(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции sin(x)')
    plt.legend()
    plt.grid()

    # Показываем график
    plt.show()


def task5():
    # Получаем список файлов в текущей директории
    files = os.listdir('.')

    # Выводим список файлов
    for file in files:
        print(file)


if __name__ == '__main__':
    print(get_site("https://google.com"))
    print("Массив numpy:", task2())
    task3()
    task4()
    task5()
