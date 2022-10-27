"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""

import random
import timeit


def bubble_sort_default(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_fast(lst_obj):
    n = 1
    while n < len(lst_obj):
        flag = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = True
        if not flag:
            break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
sorted_list = bubble_sort_fast(orig_list.copy())
print(f'Оригинальный массив\n{orig_list}')
print(f'Отсортированный массив\n{sorted_list}')

# замеры 10
orig_list1 = [random.randint(-100, 100) for _ in range(10)]
print("Начальный вариант: 10 эл => ", timeit.timeit("bubble_sort_default(orig_list1[:])", \
                                                    setup="from __main__ import bubble_sort_default, orig_list1",
                                                    number=100))
orig_list2 = [random.randint(-100, 100) for _ in range(10)]
print("Доработка: 10 эл => ", timeit.timeit("bubble_sort_fast(orig_list2[:])", \
                                            setup="from __main__ import bubble_sort_fast, orig_list2",
                                            number=100))

# замеры 100
orig_list3 = [random.randint(-100, 100) for _ in range(100)]
print("Начальный вариант: 100 эл => ", timeit.timeit("bubble_sort_default(orig_list3[:])", \
                                                     setup="from __main__ import bubble_sort_default, orig_list3",
                                                     number=100))
orig_list4 = [random.randint(-100, 100) for _ in range(100)]
print("Доработка: 100 эл => ", timeit.timeit("bubble_sort_fast(orig_list4[:])", \
                                             setup="from __main__ import bubble_sort_fast, orig_list4",
                                             number=100))

# замеры 1000
orig_list5 = [random.randint(-100, 100) for _ in range(1000)]
print("Начальный вариант: 1000 эл => ", timeit.timeit("bubble_sort_default(orig_list5[:])", \
                                                      setup="from __main__ import bubble_sort_default, orig_list5",
                                                      number=100))
orig_list6 = [random.randint(-100, 100) for _ in range(1000)]
print("Доработка: 1000 эл => ", timeit.timeit("bubble_sort_fast(orig_list6[:])", \
                                              setup="from __main__ import bubble_sort_fast, orig_list6",
                                              number=100))

"""
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Замеры:
Оригинальный массив
[-14, 81, 38, -7, -60, 73, 82, -59, -78, -70]
Отсортированный массив
[82, 81, 73, 38, -7, -14, -59, -60, -70, -78]
Начальный вариант: 10 эл =>  0.0018530000000000005
Доработка: 10 эл =>  0.0013306000000000012
Начальный вариант: 100 эл =>  0.11896259999999999
Доработка: 100 эл =>  0.13537300000000002
Начальный вариант: 1000 эл =>  12.10671
Доработка: 1000 эл =>  12.5096746

Вывод: доработка не влияет критично на время выполнения функции. Результат по времени почти такой же.
"""