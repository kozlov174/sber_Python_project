# ### Задание1. Извлечение цитат и авторов с сайта.
# 1. Отправьте запрос на страницу http://quotes.toscrape.com/ и с помощью регулярных выражений извлеките:
#  - Все цитаты (все, что внутри тега `<span class="text">`).
#  - Все авторов (все, что внутри тега `<small class="author">`).
# 2. Выведите цитаты и их авторов в формате: "Цитата" - Автор.

import requests
import re

if __name__ == '__main__':
    url = "http://quotes.toscrape.com/"
    responce = requests.get(url)
    # print(responce.text)
    quotes_pattern = r'<span.*?class="text".*?>(.*?)</span>'
    quotes = re.findall(quotes_pattern, responce.text)
    authors_pattern = r'<small.*?class="author".*?>(.*?)</small>'
    authors = re.findall(authors_pattern, responce.text)
    for author, quote in zip(authors, quotes):
        print(quote, author)