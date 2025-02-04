import sqlite3

# Создание базы данных и таблицы users
def create_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()

# Добавление пользователя
def add_user(name, age):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

# Чтение всех пользователей
def get_all_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

# Обновление имени пользователя
def update_user_name(user_id, new_name):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ? WHERE id = ?", (new_name, user_id))
    conn.commit()
    conn.close()

# Удаление пользователя
def delete_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

# Тестирование функций
if __name__ == "__main__":
    create_database()

    # Добавляем пользователей
    add_user("Алиса", 25)
    add_user("Боб", 30)

    # Вывод всех пользователей
    print("Пользователи до обновления:")
    print(get_all_users())

    # Обновляем имя пользователя
    update_user_name(1, "Анна")

    # Вывод после обновления
    print("Пользователи после обновления:")
    print(get_all_users())

    # Удаляем пользователя
    delete_user(2)

    # Вывод после удаления
    print("Пользователи после удаления:")
    print(get_all_users())
