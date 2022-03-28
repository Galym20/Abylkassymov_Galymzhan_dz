import random

words_1 = ["автомобиль", "лес", "огонь", "город", "дом"]
words_2 = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
words_3 = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(word):
    list = []
    for i in range(word):
        jokes_words_1 = random.choice(words_1)
        jokes_words_2 = random.choice(words_2)
        jokes_words_3 = random.choice(words_3)
        list.append(f'{jokes_words_1} {jokes_words_2} {jokes_words_3}')
    return list

print(get_jokes(1))



def get_jokes_adv(word, repeats=True):
    list = []

    if not repeats:
        if word > min(len(words_1), len(words_2), len(words_3)):
            return
        else:
            random.shuffle(words_1)
            random.shuffle(words_2)
            random.shuffle(words_3)
            for i in range(word):
                list.append(f'{words_1[i]} {words_2[i]} {words_3[i]}')

    else:
        for i in range(word):
            jokes_words_1 = random.choice(words_1)
            jokes_words_2 = random.choice(words_2)
            jokes_words_3 = random.choice(words_3)
            joke_list.append(f'{jokes_words_1} {jokes_words_2} {jokes_words_3}')
    return list

print(get_jokes_adv(5, False))
