
import numpy as np
from pympler import asizeof

class DefaultObject:
    def __init__(self, name, sum, avg_sum):
        self.name = name
        self.sum = sum
        self.avg_sum = avg_sum


class SlotsObject:
    __slots__ = ('name', 'sum', 'avg_sum')

    def __init__(self, name, sum, avg_sum):
        self.name = name
        self.sum = sum
        self.avg_sum = avg_sum


d1 = DefaultObject("Roga", 2566584, "17584")
d2 = DefaultObject("Kopyta", 365426, "20125")
s1 = SlotsObject("Roga", 2566584, "17584")
s2 = SlotsObject("Kopyta", 365426, "17584")


"""
использование numpy для работы с массивами
"""
lst = [el for el in range(1000)]
arr = np.array([el for el in range(1000)])
print(f'default list => {asizeof.asizeof(lst)}')
print(f'numpy array => {asizeof.asizeof(arr)}')
"""
Видим, что массив в numpy занимает сильно меньше памяти
default list => 41008
numpy array => 4128
"""