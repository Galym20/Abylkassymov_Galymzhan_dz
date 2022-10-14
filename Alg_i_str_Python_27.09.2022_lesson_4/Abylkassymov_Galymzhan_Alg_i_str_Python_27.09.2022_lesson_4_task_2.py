"""
Задание 2.
Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.
Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?
Если у вас есть идеи, предложите вариант оптимизации.
"""

from random import randint
from timeit import timeit


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))


@memoize
def recursive_reverse_mem1(number):
    if number == 0:
        return ''
    return f'{number % 10}{recursive_reverse_mem1(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem1')
print(
    timeit(
        'recursive_reverse_mem1(num_100)',
        setup='from __main__ import recursive_reverse_mem1, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem1(num_1000)',
        setup='from __main__ import recursive_reverse_mem1, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem1(num_10000)',
        setup='from __main__ import recursive_reverse_mem1, num_10000',
        number=10000))

"""
1. мемоизация нужна, т.к. сильно сокращает время выполнения программы:
Не оптимизированная функция recursive_reverse
0.0324926
0.0402892
0.06583820000000001
Оптимизированная функция recursive_reverse_mem
0.002619199999999988
0.002562999999999982
0.0027580000000000104
2. возможная оптимизация - избавиться от приведения результата от деления с остатком к строке, 
т.к. функция f и так приводит число к строке, но выигрыш по времени не такой большой и критичный
Не оптимизированная функция recursive_reverse
0.03342932500000001
0.03864495400000001
0.068731559
Оптимизированная функция recursive_reverse_mem
0.0026628419999999986
0.0029004639999999915
0.0028723910000000297
Оптимизированная функция recursive_reverse_mem1
0.0027457000000000176
0.002615300000000015
0.002748399999999984
"""