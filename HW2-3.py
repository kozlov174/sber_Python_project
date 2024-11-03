# ### Задание 3. Извлечение данных о книгах.
# 1. Перейдите на сайт http://books.toscrape.com/ и отправьте запрос с помощью библиотеки requests.
# 2. Используйте регулярные выражения для извлечения:
# - Названий всех книг на главной странице.
# - Стоимости каждой книги (значение внутри тега `<p class="price_color">`).
# 3. Выведите данные в формате: "Название книги" - Цена.

import re
import requests

if __name__ == '__main__':
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    name_pattern = r'<a.*?title="(.*?)">'
    price_pattern = r'<p.*?class="price_color">(.*?)</p?'
    names = re.findall(name_pattern, response.text)
    prices = re.findall(price_pattern, response.text)
    for name, price in zip(names, prices):
        print(name, price)