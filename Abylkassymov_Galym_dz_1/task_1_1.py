duration = int(input('Введите число: '))
min = 60
hour = 3600
day = 86400
if duration < min:
    print('duration = ', duration, 'сек')
elif duration < hour:
    print('duration = ', duration // min, 'мин', duration % min, 'сек')
elif duration < day:
    print('duration = ', duration // hour, 'час', duration % hour // min, 'мин', duration % min, 'сек')
else:
    print('duration = ', duration // day, 'день', duration % day // hour, 'час', duration % hour // min, 'мин', duration % min, 'сек')