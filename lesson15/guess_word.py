import random


words = ["яблуко", "банан", "виноград", "апельсин", "ананас"]


def shuffle_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return " ".join(word_list)


word = random.choice(words)
shuffled = shuffle_word(word)

print("Вгадай слово! Ось його перемішані літери:", shuffled)
print(f"Підказка: перша літера - {word[0]}, остання - {word[-1]}")

