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

h1 = soup.find("h1", class_="title")
print(h1.text)  # Title

items = [li.text for li in soup.find_all("li")]
print(items)  # ['Item-1', 'Item-2']

link = soup.select_one("a[href]")  # поиск по css-селектору
print(link["href"])  # https://example.com/page


# Реальный сайт (обязательно нужно проверять robots.txt и условия использования)
resp = requests.get("https://example.com", timeout=10)
soup = BeautifulSoup(resp.text, "lxml")


