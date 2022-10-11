"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

# №1 O(n)
def authorization_f(users, user_name, user_password):
    for key, value in users.items():
        if key == user_name:
            if value['password'] == user_password and value['activation']:
                return "Welcome! Access is allowed"
            elif value['password'] == user_password \
                    and not value['activation']:
                return "Account is not active! Get activated!"
            elif value['password'] != user_password:
                return "Try again"

    return "User does not exist"


# №2 O(1)
def authorization_s(users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password \
                and users[user_name]['activation']:
            return "Welcome! Access is allowed"
        elif users[user_name]['password'] == user_password \
                and not users[user_name]['activation']:
            return "Account is not active! Get activated!"
        elif users[user_name]['password'] != user_password:
            return "Try again"
    else:
        return "User does not exist"


"""
Вторая реализация будет намного эффективнее, 
так как в ней не используется цикл, 
поиск в словаре по ключу имеет сложность - O(1)
"""


my_users = {'user1': {'password': 'aaa', 'activation': True},
            'user2': {'password': 'bbb', 'activation': False},
            'user3': {'password': 'ccc', 'activation': True},
            'user4': {'password': 'ddd', 'activation': False}
            }

print(authorization_s(my_users, 'user5', 'eee'))
print(authorization_f(my_users, 'user5', 'fff'))
