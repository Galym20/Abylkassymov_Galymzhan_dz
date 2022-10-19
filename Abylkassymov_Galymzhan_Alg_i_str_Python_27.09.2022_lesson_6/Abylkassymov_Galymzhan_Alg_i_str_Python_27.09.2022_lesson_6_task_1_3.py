
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


@get_time
def add_to_list(lst):
    for i in range(200000, 300000):
        lst.append(i)


@get_time
def add_to_list_extend(lst, ext_lst):
    lst.extend(ext_lst)


@get_time
def add_to_dict(dict):
    for i in range(200000, 300000):
        dict[i] = i


list = init_list()
list2 = init_list_gen()
dict = init_dict()
add_to_list(list)
add_to_list_extend(list2, extend_list)
add_to_dict(dict)

"""
Напоследок, расширение словаря элементами
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    54    102.6 MiB    102.6 MiB           1   @profile
    55                                         def add_to_dict(dict):
    56    105.7 MiB      0.0 MiB      100001       for i in range(200000, 300000):
    57    105.7 MiB      3.1 MiB      100000           dict[i] = i

Общие данные полученные с помощью декоратора, 
по которым видна разница по использованию памяти при создании массива обычным способом(for + append) и генератором

method => init_list
	time => 0.24001860618591309 sec, memory => 7.71875
method => init_list_gen
	time => 0.20200037956237793 sec, memory => 0.046875
method => init_dict
	time => 0.2513711452484131 sec, memory => 16.1875
method => add_to_list
	time => 0.22054719924926758 sec, memory => 3.89453125
method => add_to_list_extend
	time => 0.2026350498199463 sec, memory => 0.9296875
method => add_to_dict
	time => 0.21421313285827637 sec, memory => 3.0703125

Process finished with exit code 0


"""