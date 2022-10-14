"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


number = 4856947531

print(
    timeit(
        "revers(number)",
        setup='from __main__ import revers, number',
        number=10000))
print(
    timeit(
        "revers_2(number)",
        setup='from __main__ import revers_2, number',
        number=10000))
print(
    timeit(
        "revers_3(number)",
        setup='from __main__ import revers_3, number',
        number=10000))


def main():
    number = 4856947531
    revers(number)
    revers_2(number)
    revers_3(number)



"""
Результаты timeit:
0.041288899999999996
0.02638560000000001
0.004628499999999994


Выводы:
первый метод медленный, т.к. использует рекурсию
второй вариант быстрее первого, т.к. работает через цикл
третий вариант быстрее, т.к. работает с переворотом строки вместо арифметических операций
"""