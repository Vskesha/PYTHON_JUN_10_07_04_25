import random


words_by_level = {
    1: ["кіт", "дім", "мак", "ліс", "мед"],
    2: ["яблуко", "банан", "дерево", "мавпа", "літо"],
    3: ["виноград", "апельсин", "ананас", "бібліотека", "телескоп"]
}


def shuffle_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return " ".join(word_list)


def choice_level():
    level = int(input("Введіть номер рівня гри (1-3): "))
    while level not in words_by_level:
        level = int(input("Введіть номер рівня гри. Будь ласка, введіть число від 1 до 3: "))
    return level


level = choice_level()
word = random.choice(words_by_level[level])
shuffled = shuffle_word(word)

print("Вгадай слово! Ось його перемішані літери:", shuffled)
print(f"Підказка: перша літера - {word[0]}, остання - {word[-1]}")

attempts = 3
while attempts > 0:
    guess = input("Введи слово: ").lower()
    if guess == word:
        print("Правильно! Ти відгадав слово!")
        break 
    else:
        attempts -= 1
        print(f"Неправильно! Залишилося спроб: {attempts}")

print(f"Гру закінчено. Правильне слово було: {word}")
