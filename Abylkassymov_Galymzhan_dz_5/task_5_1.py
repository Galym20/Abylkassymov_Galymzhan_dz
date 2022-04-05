def odd_to_15(odd_nums):
    for i in odd_nums:
        if i % 2 != 0:
            yield i

list_of_nums = range(16)

for i in odd_to_15(list_of_nums):
    print('Next odd_to_15', i, )
