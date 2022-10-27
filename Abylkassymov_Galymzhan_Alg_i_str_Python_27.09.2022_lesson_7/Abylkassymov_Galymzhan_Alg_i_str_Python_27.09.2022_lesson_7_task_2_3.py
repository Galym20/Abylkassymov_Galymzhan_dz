"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
3) с помощью встроенной функции поиска медианы
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

import random
import statistics

m = 5
orig_list = [random.randint(0, 50) for _ in range(2 * m + 1)]
print(f'Оригинальный массив: {orig_list}')

for i in range(len(orig_list)):
    left = []
    right = []
    for k in range(len(orig_list)):
        if i == k:
            continue
        if orig_list[k] < orig_list[i]:
            left.append(orig_list[k])
        elif orig_list[k] > orig_list[i]:
            right.insert(0, orig_list[k])
        else:
            if len(left) > len(right):
                right.append(orig_list[k])
            else:
                left.insert(0, orig_list[k])
    print(f'Итерация: {i + 1}\n\tЛевая часть:  {(left)}\n\tПравая часть: {(right)}\n\n')
    if len(left) == len(right) == m:
        print(f'Медиана ====> {statistics.median(orig_list)}')
        break
    left.clear()
    right.clear()