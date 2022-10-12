"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

import random


def guess_num(number, n):
    if n == 10:
        print(f'Вы проиграли. Загаданное число: {number}')
        return
    else:
        try:
            user_number = int(input('Введите число:'))
            if number > user_number:
                print(f'Ваше число {user_number} меньше загаданного')
                guess_num(number, n + 1)
            elif number < user_number:
                print(f'Ваше число {user_number} больше загаданного')
                guess_num(number, n + 1)
            else:
                print(f'Вы угадали число! {number}')
                return
        except ValueError:
            print('Вы ввели не число! Попробуйте еще раз')
            guess_num(number, n)


rand_number = random.randint(0, 100)
guess_num(rand_number, 1)