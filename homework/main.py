import re
import requests
from requests_html import HTMLSession

# Получаем HTML-код страницы
#session = HTMLSession()
#url = 'https://www.randomlists.com/email-addresses'
#EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
#r = session.get(url)
#r.html.render()
#for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
#    print(re_match.group())



#response = requests.get(url)
#html = response.text

with open("Random Email Addresses.html", "r", encoding="utf-8") as file:
    html = file.read()

# Находим все email адреса на странице
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', html)

# Выводим найденные email адреса
for email in emails:
    print(email)
