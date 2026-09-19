Парсинг – практики и примеры использования

1. JSON - встроенный парсер (предпочтителен ручному разбору)

```Python
import json

raw = '{"name": "Igor", "age": 30, "skills": ["Python", "Django"]}'

data = json.loads(raw) 
print(repr(data))  # {'name': 'Igor', 'age': 30, 'skills': ['Python', 'Django']}
print(type(data))  # str -> dict

# И обратно
text = json.dumps(data, ensure_ascii=False, indent=2)  # ensure_ascii отвечает за кодировку не-ascii-символов (False оставит кириллицу, True заменит на escape-последовательности)
print(repr(text))  # '{"name": "Igor", "age": 30, "skills": ["Python", "Django"]}'
print(type(text))  # dict -> str
```

2. Строковые методы – для простых форматов

```Python
import csv
from io import StringIO

raw = 'name,city\n"Ivanov, P.", "Moscow"\nPetrova,SPb'

for row in csv.DictReader(StringIO(raw)):
  print(row)  # {'name': 'Ivanov, P.', 'city': 'Moscow'}
```

3. Регулярные выражения - структурированные тексты (логи, даты)

```Python
import re

# Парсинг строки лога: 2026-09-19 12:33:01 ERROR disk full

log_pattern = re.compile(  # Компилирует регулярное выражение в объект паттерна для многократного использования для поиска/матчинга
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<time>\d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>INFO|WARN|ERROR)\s+"
    r"(?P<message>.+)"
)

match = log_pattern.match("2026-09-19 12:33:01 ERROR disk full")

if match:
    print(match.group("level"))  # ERROR  (group возвращает часть строки, совпадающую с группой в регулярном выражении)
    print(match.group("message"))  # disk full  (group возвращает часть строки, совпадающую с группой в регулярном выражении)
    print(match.groupdict())  # {'date': '2026-09-19', 'time': '12:33:01', 'level': 'ERROR', 'message': 'disk full'}  (groupdict() возвращает словарь для всех именованных групп)
  
# Извлечение всех email из текста
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", "a@x.ru, b@y.org")  # поиск и возврат всех непересекающихся совпадений
print(emails)  # ['a@x.ru', 'b@y.org']
```

Правила работы с regexp: 

* Компилируем шаблон (re.compile) для много кратного использования (при необходимости)
* Использовать именованные группы `(?P<name>...)` для повышения читаемости
* Не пытаться парсить regex-ом вложенные структуры (HTML, JSON)

4. HTML – BeautifulSoup (веб-парсинг)

```Python
# pip install beautifulsoup4 requests
from bs4 import BeautifulSoup
import requests

html = """
<html>
    <body>
        <h1 class="title">Title</h1>
        <ul>
            <li>Item-1</li>
            <li>Item-2</li>
        </ul>
        <a href="https://example.com/page">Link</a>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

h1 = soup.find(h1, class_="title")  # Title
items = [li.text for li in soup.find_all('li')]  # ["Item-1", "Item-2"]
link = soup.select_one("a[href]")  # https://example.com/page

# Реальный сайт
resp = requests.get("https://example.com", timeout=10)
soup = BeatifulSoup(resp.text, "lxml")
```
