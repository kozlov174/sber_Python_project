# Задание 2. Поиск всех ссылок на странице.
# Напишите регулярное выражение, которое извлекает все ссылки на странице http://quotes.toscrape.com/ (все теги ).
# Выведите список всех найденных URL.

import re
import requests

if __name__ == '__main__':
    url = "http://quotes.toscrape.com/"
    request = requests.get(url)
    pattern = r'https?://[^\s"\'<>]+'
    urls = re.findall(pattern, request.text)
    for url in urls:
        print(url)