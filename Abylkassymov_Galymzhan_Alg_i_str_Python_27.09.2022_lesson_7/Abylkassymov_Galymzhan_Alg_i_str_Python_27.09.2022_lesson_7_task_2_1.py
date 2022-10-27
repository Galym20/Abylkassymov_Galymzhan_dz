"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

"""
вариант с использованием гномьей сортировки
"""

import random

def gnome_sort(orig_list):
    i = 1
    j = 2
    while i < len(orig_list):
        if orig_list[i - 1] < orig_list[i]:
            i = j
            j += 1
        else:
            orig_list[i], orig_list[i - 1] = orig_list[i - 1], orig_list[i]
            i -= 1
            if i == 0:
                i = j
                j += 1
    return orig_list

m = 5
orig_list = [random.randint(0, 50) for _ in range(2 * m + 1)]
sorted_list = gnome_sort(orig_list)
print(f'Оригинальный массив: {orig_list}\n\tОтсортированный массив: {sorted_list}')
if sorted_list[m - 1] <= sorted_list[m] <= sorted_list[m + 1]:
    print(f'Медиана ====> {sorted_list[m]}')