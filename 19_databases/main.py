# 19_databases/main.py

# Пример 1: Использование SQLite
import sqlite3

# Создание базы данных и таблицы
connection = sqlite3.connect("example.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# Вставка данных
cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
connection.commit()

# Чтение данных
cursor.execute("SELECT * FROM users")
print("Пользователи:", cursor.fetchall())

connection.close()

# Пример 2: Ошибка из-за неправильного SQL-запроса
# cursor.execute("SELECT * FROM nonexistent_table")  # Ошибка: sqlite3.OperationalError
