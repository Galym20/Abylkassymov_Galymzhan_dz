"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def calc(n, number, result):
  if n == 0:
    return result
  else:
    new_number = (number / 2) * -1
    result += number
    return calc(n - 1, new_number, result)


try:
  number_from_input = int(input('Введите количество элементов:'))
  print(calc(number_from_input, 1, 0))
except ValueError:
  print('Вы ввели не число')