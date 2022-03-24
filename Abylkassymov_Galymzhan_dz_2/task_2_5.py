prices = [57.8, 46.51, 97, 101, 87.12, 26.7, 4, 7777, 14.55]
for i in prices:
    rub = int(i)
    kk = (i - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')

prices = [57.8, 46.51, 97, 101, 87.12, 26.7, 4, 7777, 14.55]
print(id(prices))
prices.sort()
print(id(prices))
for i in prices:
    rub = int(i)
    kk = (i - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')

prices = [57.8, 46.51, 97, 101, 87.12, 26.7, 4, 7777, 14.55]
for i in sorted(prices)[::-1][:5]:
    rub = int(i)
    kk = (i - int(i)) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')
