list = []
for i in range(1, 1001, 2):
    i **= 3
    list.append(i)

summ = 0
for i in list:
    for num in str(i):
        summ += int(num)
    if summ % 7 ==0:
        summ += i
print(summ)

final_summ = 0
for num in list:
    num += 17
    summ = 0
    for final_num in str(num):
        summ += int(final_num)
    if summ % 7 == 0:
        final_summ += num
print(final_summ)