from datetime import datetime, timedelta

# Task 1
now = datetime.now()
print(now)

# Task 2
formated = now.strftime("%d.%m.%Y %H:%M:%S")
print(formated)

# Task 3
date_1 = datetime.now()
date_2 = datetime.now() - timedelta(days=1, hours=5)
print("Дата 1:", date_1)
print("Дата 2:", date_2)
result = date_1 - date_2
print("Разница между датами:", result)

# Task 4
days_of_week = {0: "Mon.", 1: "Tues.", 2: "Wed.", 3: "Thurs.", 4: "Fri.", 5: "Sat.", 6: "Sun.", }
now = datetime.now()
id_day = now.weekday()
print("Текущий день недели:", days_of_week[id_day])

# Task 5
now = datetime.now()
add_5_days = now + timedelta(days=5)
print("Через 5 дней будет:", add_5_days)
