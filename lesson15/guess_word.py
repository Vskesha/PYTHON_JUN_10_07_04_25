import random

words_by_category = {
    "фрукти": {
        1: ["ківі", "мак", "лічі"],
        2: ["яблуко", "банан", "груша"],
        3: ["виноград", "апельсин", "ананас"]
    },
    "овочі": {
        1: ["кріп", "буряк", "ріпа"],
        2: ["морква", "цибуля", "гарбуз"],
        3: ["баклажан", "картопля", "кабачок"]
    },
    "природа": {
        1: ["ліс", "море", "сніг"],
        2: ["озеро", "пісок", "вітер"],
        3: ["водоспад", "джерело", "полуострів"]
    }
}


def shuffle_word(word):
    letters = list(word.upper())
    random.shuffle(letters)
    return " ".join(letters)


def choice_level():
    level = int(input("Введи номер рівня гри (1 - 3): "))
    while level not in words_by_category[category]:
        level = int(input("Введи номер рівня гри повторно (1 - 3): "))
    return level


def choice_category():
    category = input("Введи категорію (фрукти, овочі, природа): ")
    while category not in words_by_category:
        category = input("Введи категорію повторно (фрукти, овочі, природа): ")
    return category


category = choice_category()
level = choice_level()
word = random.choice(words_by_category[category][level])
shuffled = shuffle_word(word)

print("Вгадай слово, ось літери: ", shuffled)
print(f"Підказка: Перша літера - {word[0]}, Остання літера - {word[-1]}" )

attempts = 3
while attempts > 0:
    guess = input("Вгадай слово: ").lower()
    if guess == word:
        print("Ти вгадав!!!")
        break
    else:
        attempts -= 1
        print(f"Неправильно! Залишилось спроб: {attempts}")
    if attempts == 0:
        print(f"Гру закінчено. Правильне слово було: {word}")
