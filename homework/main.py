import re

with open("Random Email Addresses.html", "r", encoding="utf-8") as file:
    html = file.read()

# Находим все email адреса на странице
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', html)

# Выводим найденные email адреса
for email in emails:
    print(email)
