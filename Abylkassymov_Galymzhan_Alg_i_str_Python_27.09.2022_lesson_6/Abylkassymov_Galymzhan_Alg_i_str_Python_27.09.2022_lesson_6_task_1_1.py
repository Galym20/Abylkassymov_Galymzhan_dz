"""
Задание 1.
Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python
На каждый скрипт нужно два решения - исходное и оптимизированное.
Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler
Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler
Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.
ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.
Это файл для первого скрипта
"""

import time
from memory_profiler import memory_usage

extend_list = [el for el in range(100000)]


def get_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        m_start = memory_usage()
        res = func(*args, **kwargs)
        m_end = memory_usage()
        end = time.time()
        print(f'method => {func.__name__}\n\ttime => {end - start} sec, memory => {m_end[0] - m_start[0]}')
        return res

    return wrapper


@get_time
def init_list():
    lst = []
    for i in range(200000):
        lst.append(i)
    return lst


@get_time
def init_list_gen():
    return [el for el in range(20000)]


@get_time
def init_dict():
    dict = {}
    for i in range(200000):
        dict[i] = i
    return dict



list = init_list()
list2 = init_list_gen()


"""
Для начала посмотрим на варианты заполнения списка через метод append или через генератор
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    22     56.7 MiB     56.7 MiB           1   @profile
    23                                         def init_list():
    24     56.7 MiB      0.0 MiB           1       lst = []
    25     64.4 MiB      0.0 MiB      200001       for i in range(200000):
    26     64.4 MiB      7.7 MiB      200000           lst.append(i)
    27     64.4 MiB      0.0 MiB           1       return lst
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    30     64.4 MiB     64.4 MiB           1   @profile
    31                                         def init_list_gen():
    32     72.2 MiB      7.7 MiB      200003       return [el for el in range(200000)]

Видим что потребление примерно на одном и том же уровне
Инициализация словаря такого же размера требует значительно больше памяти, т.к. требуется место для хранения хешей
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     72.2 MiB     72.2 MiB           1   @profile
    36                                         def init_dict():
    37     72.2 MiB      0.0 MiB           1       dict = {}
    38     97.2 MiB      0.0 MiB      200001       for i in range(200000):
    39     97.2 MiB     25.0 MiB      200000           dict[i] = i
    40     97.2 MiB      0.0 MiB           1       return dict

method => init_list
	time => 0.23336267471313477 sec, memory => 7.7265625
method => init_list_gen
	time => 0.20180797576904297 sec, memory => 0.625
"""