"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import hashlib
from uuid import uuid4

salt = uuid4().hex
cache = {}


def add_to_cache(url):
    if url not in cache:
        cache[url] = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
        print(f'url {url} добавлен в кеш')
    else:
        print(f'url {url} есть в кеше')


urls = [
    'www.amazon.com',
    'www.amazon.com/test',
    'www.amazon.com/test',
]

for url in urls:
    add_to_cache(url)

print(cache)