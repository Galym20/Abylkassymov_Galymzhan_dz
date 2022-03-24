# Вариант 1
list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

my_list = []
for i in list:
    if i.isdigit():
        my_list.extend(['"', f'{int(i):02}', '"'])
    elif (i.startswith('+') or i.startswith('-')) and i[1:].isdigit():
        my_list.extend(['"', f'{i[0]}{int(i[1:]):02}', '""'])
    else:
        my_list.append(i)
total = ' '.join(my_list)
print(total)

symbol_id = []
for i, letter in enumerate(total):
    if letter == '"':
        symbol_id.append(i)

for i in range(len(symbol_id)):
    if i % 2 == 0:
        symbol_id[i] = symbol_id[i] + 1
    else:
        symbol_id[i] = symbol_id[i] - 1

for del_id in reversed(symbol_id):
    total = total[:del_id] + total[del_id + 1:]
print(total)




# Вариант 2 (используя функции)
# list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# print(" ".join(map(lambda x: '"%s"' % __import__('re').sub('\d+', lambda x: f' { x[0] } '.zfill(2), x) if any(map(str.isdigit, x)) else x, list)))





