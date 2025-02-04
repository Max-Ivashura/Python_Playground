# Task 1
import re

text = """
Пример текста с email-адресами: user@example.com, another.email@domain.org, 
а также invalid-email@ и @missing-domain.com.
"""

# Регулярное выражение для поиска email-адресов
email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# Поиск всех совпадений
emails = re.findall(email_pattern, text)

print("Найденные email-адреса:")
for email in emails:
    print(email)

# Task 2
import re

text = "В 2023 году я планирую посетить 5 стран и прочитать 12 книг."

# Регулярное выражение для поиска цифр
digit_pattern = r'\d'

# Замена всех цифр на *
result = re.sub(digit_pattern, '*', text)

print("Текст после замены:")
print(result)

# Task 3
import re

def is_valid_phone_number(phone):
    # Регулярное выражение для проверки номера телефона
    phone_pattern = r'^\+7-\d{3}-\d{3}-\d{2}-\d{2}$'
    return re.match(phone_pattern, phone) is not None

# Примеры номеров
phone1 = "+7-123-456-78-90"
phone2 = "8-123-456-78-90"
phone3 = "+7-123-456-789"

print(f"{phone1} валиден? {is_valid_phone_number(phone1)}")
print(f"{phone2} валиден? {is_valid_phone_number(phone2)}")
print(f"{phone3} валиден? {is_valid_phone_number(phone3)}")

# Task 4
import re

text = "Апельсин, банан, ананас, яблоко, арбуз."

# Регулярное выражение для поиска слов, начинающихся с "А"
word_pattern = r'\b[Аа]\w*\b'

# Поиск всех совпадений
words = re.findall(word_pattern, text)

print("Слова, начинающиеся с 'А':")
for word in words:
    print(word)

# Task 5
import re

text = "Привет! Как дела? Это пример текста. Он содержит несколько предложений."

# Регулярное выражение для разделения текста на предложения
sentence_pattern = r'[.!?]'

# Разделение текста
sentences = re.split(sentence_pattern, text)

# Удаление пустых строк
sentences = [s.strip() for s in sentences if s.strip()]

print("Предложения:")
for sentence in sentences:
    print(sentence)