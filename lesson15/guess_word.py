import random


words = ["яблуко", "банан", "виноград", "апельсин", "ананас"]


def shuffle_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return " ".join(word_list)


word = words[0]
print(shuffle_word(word))
