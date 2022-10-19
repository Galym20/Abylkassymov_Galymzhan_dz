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
def add_to_list(lst):
    for i in range(200000, 300000):
        lst.append(i)

@get_time
def add_to_list_extend(lst, ext_lst):
    lst.extend(ext_lst)


list = init_list()
add_to_list(list)
add_to_list_extend(list, extend_list)


"""   
Далее посмотрим на расширение списка двумя способами - добавление элементов в цикле или использование метода extend
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    43     97.2 MiB     97.2 MiB           1   @profile
    44                                         def add_to_list(lst):
    45    100.3 MiB      0.0 MiB      100001       for i in range(200000, 300000):
    46    100.3 MiB      3.1 MiB      100000           lst.append(i)
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    49    100.3 MiB    100.3 MiB           1   @profile
    50                                         def add_to_list_extend(lst, ext_lst):
    51    102.6 MiB      2.3 MiB           1       lst.extend(ext_lst)

Видим, что метод extend потребляет меньше памяти

method => init_list
	time => 0.23583745956420898 sec, memory => 8.453125
method => add_to_list
	time => 0.22395825386047363 sec, memory => 3.88671875
method => add_to_list_extend
	time => 0.20476269721984863 sec, memory => 0.765625
"""