import re
import requests

# Получаем HTML-код страницы
url = 'https://developer.roman.grinyov.name/blog/9'
response = requests.get(url)
html = response.text

# Находим все email адреса на странице
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', html)

# Выводим найденные email адреса
for email in emails:
    print(email)