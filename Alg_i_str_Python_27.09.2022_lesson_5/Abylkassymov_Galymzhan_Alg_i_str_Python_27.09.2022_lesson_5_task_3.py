"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

import timeit
from collections import deque


def get_time(func):
    def wrapper(*args, **kwargs):
        start = timeit.timeit()
        res = func(*args, **kwargs)
        end = timeit.timeit()
        print(func.__name__, end - start)
        return res

    return wrapper


@get_time
def init_list():
    lst = []
    for i in range(1000):
        lst.append(i)
    return lst


@get_time
def init_deque():
    deq = deque()
    for i in range(1000):
        deq.append(i)
    return deq


@get_time
def append_to_list(lst):
    for i in range(len(lst), len(lst) + 1000):
        lst.append(i)


@get_time
def append_to_deque(deq):
    for i in range(1000, 2000):
        deq.append(i)


@get_time
def append_left_to_list(lst):
    lst.insert(0, 5)


@get_time
def append_left_to_deque(deq):
    deq.appendleft(5)


@get_time
def insert_to_list(lst):
    lst.insert(0, 30)


@get_time
def insert_to_deque(deq):
    deq.insert(0, 30)


@get_time
def pop_from_list(lst):
    return lst.pop()


@get_time
def pop_from_deque(deq):
    return deq.pop()


@get_time
def popleft_from_list(lst):
    return lst.pop(0)


@get_time
def popleft_from_deque(deq):
    return deq.popleft()


@get_time
def get_from_list_by_index(lst):
    return lst[10]


@get_time
def get_from_deque_by_index(deq):
    return deq[10]


@get_time
def extend_left_list(extend_lst):
    lst = []
    for el in extend_lst:
        lst.insert(0, el)


@get_time
def extend_left_deque(extend_lst):
    deq = deque()
    return deq.extendleft(extend_lst)


@get_time
def reverse_list(lst):
    lst.reverse()


@get_time
def reverse_deque(deq):
    deq.reverse()


list = init_list()
deq = init_deque()
append_to_list(list)
append_to_deque(deq)
append_left_to_list(list)
append_left_to_deque(deq)
insert_to_list(list)
insert_to_deque(deq)
extend_left_list(list)
extend_left_deque(list)
reverse_list(list)
reverse_deque(deq)
list_el = pop_from_list(list)
dict_el = pop_from_deque(deq)
list_el1 = popleft_from_list(list)
dict_el1 = popleft_from_deque(deq)
list_el_indexed = get_from_list_by_index(list)
dict_el_indexed = get_from_deque_by_index(deq)

"""
init_list -0.0038620999999999933
init_deque 0.001406400000000002
append_to_list -0.00032449999999999146
append_to_deque -7.690000000001862e-05
append_left_to_list -0.0003692999999999891
append_left_to_deque -9.730000000002237e-05
insert_to_list 1.6499999999974868e-05
insert_to_deque -2.389999999999337e-05
extend_left_list -9.30999999999571e-05
extend_left_deque 0.01871400000000001
reverse_list -0.0038656000000000246
reverse_deque 0.00016319999999997448
pop_from_list 0.00013180000000001524
pop_from_deque 0.001176699999999975
popleft_from_list -0.00018800000000002148
popleft_from_deque -8.319999999994998e-05
get_from_list_by_index 9.639999999999649e-05
get_from_deque_by_index 0.0002558999999999756
Как мы видим на примере, все операции с deque быстрее, чем операции с list, 
кроме операций append - они примерно одинаковы по времени.
Сильно выигрывают по времени операции по вставке/выборке элементов слева (appendleft/extendleft/popleft)
"""