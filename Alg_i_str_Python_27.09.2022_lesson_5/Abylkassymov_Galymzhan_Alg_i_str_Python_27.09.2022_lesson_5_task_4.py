"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

import timeit
from collections import OrderedDict


def get_time(func):
    def wrapper(*args, **kwargs):
        start = timeit.timeit()
        res = func(*args, **kwargs)
        end = timeit.timeit()
        print(func.__name__, end - start)
        return res

    return wrapper


@get_time
def init_dist():
    default_dict = dict()
    for i in range(1000):
        default_dict[str(i)] = i
    return default_dict


@get_time
def init_ordered_dict():
    ordered_dict = OrderedDict()
    for i in range(1000):
        ordered_dict[str(i)] = i
    return ordered_dict


@get_time
def pop_from_default_dict(default_dict):
    for i in range(len(default_dict)):
        a = default_dict.popitem()


@get_time
def pop_from_ordered_dict(ordered_dict):
    for i in range(len(ordered_dict)):
        a = ordered_dict.popitem()


@get_time
def key_value_default_dict(default_dict):
    for key, value in default_dict.items():
        k = key
        v = value


@get_time
def key_value_ordered_dict(ordered_dict):
    for key, value in ordered_dict.items():
        k = key
        v = value


@get_time
def get_item_default_dict(default_dict):
    a = default_dict.get('900')


@get_time
def get_item_ordered_dict(ordered_dict):
    a = ordered_dict.get('900')


default_dict = init_dist()
ordered_dict = init_ordered_dict()
pop_from_default_dict(default_dict)
pop_from_ordered_dict(ordered_dict)
key_value_default_dict(default_dict)
key_value_ordered_dict(ordered_dict)
get_item_default_dict(default_dict)
get_item_ordered_dict(ordered_dict)

"""
довольно похожие по производительности коллекции, 
но OrderedDict в среднем чуть быстрее почти во всех операциях, чем обычный словарь
"""