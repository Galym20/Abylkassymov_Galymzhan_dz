list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(list):
    if list[i].isdigit():
        list.insert(i, '"')
        list[i + 1] = f'{int(list[i + 1]):02}'
        list.insert(i + 2, '"')
        i += 2

    elif (list[i].startswith('+') or list[i].startswith('-')) and list[i][1:].isdigit():
        list.insert(i, '"')
        list[i + 1] = f'{list[i + 1][0]}{int(list[i + 1]):02}'
        list.insert(i + 2, '"')
        i += 2
    i += 1

total = ' '.join(list)

print(total)