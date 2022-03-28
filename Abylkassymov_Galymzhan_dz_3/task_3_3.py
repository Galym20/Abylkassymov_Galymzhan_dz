def thesaurus(*names):
    list = dict()
    for i in names:
        list.setdefault(i[0], [])
        list[i[0]].append(i)
    return list

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Jack", "James", "Leo", "Max"))