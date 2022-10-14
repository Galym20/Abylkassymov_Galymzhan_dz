"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

import random
from timeit import timeit

nums = random.sample(range(1, 50), 30)


def sample_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def sample_2(nums):
    new_arr = []
    for index, value in enumerate(nums, start=0):
        if value % 2 == 0:
            new_arr.append(index)
    return new_arr


def sample_3(nums):
    new_arr = []
    for index, value in enumerate(nums, start=0):
        if not value % 2:
            new_arr.append(index)
    return new_arr


def sample_4(nums):
    return [i for i, elem in enumerate(nums) if elem % 2 == 0]


print(timeit('sample_1(nums)', 'from __main__ import sample_1, nums'))
print(timeit('sample_2(nums)', 'from __main__ import sample_2, nums'))
print(timeit('sample_3(nums)', 'from __main__ import sample_3, nums'))
print(timeit('sample_4(nums)', 'from __main__ import sample_4, nums'))

"""
Результаты:
sample_1 - 3.8659445 - самый медленный вариант
sample_2 - 3.8094249 - быстрее за счет использование enumerate
sample_3 - 3.3148851000000006 - быстрее за счет предыдущей оптимизации + использования условия if not
sample_4 - 2.9127194000000003 - быстрее за счет предыдущих оптимизаций + использования list comprehension
"""