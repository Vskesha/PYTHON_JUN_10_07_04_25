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
    word_list = list(word)
    random.shuffle(word_list)
    return " ".join(word_list)


def choice_category():
    categories = ", ".join(words_by_category.keys())
    category = input(f"Введіть категорію ({categories}): ")
    while category not in words_by_category:
        category = input(f"Введіть категорію. Будь ласка, введіть одну із цих категорій ({categories}): ")
    return category


def choice_level():
    category_dict = words_by_category[category]
    
    max_level = max(category_dict.keys())
    if max_level == 1:
        return 1
    
    level = int(input(f"Введіть номер рівня гри (1-{max_level}): "))
    while level not in category_dict:
        level = int(input(f"Введіть номер рівня гри. Будь ласка, введіть число від 1 до {max_level}: "))
    return level


category = choice_category()
level = choice_level()
word = random.choice(words_by_category[category][level])
shuffled = shuffle_word(word)

print("Вгадай слово! Ось його перемішані літери:", shuffled)

attempts = 3
while attempts > 0:
    guess = input("Введи слово: ").lower()
    if guess == word:
        print("Правильно! Ти відгадав слово!")
        break 
    else:
        attempts -= 1
        print(f"Неправильно! Залишилося спроб: {attempts}")
        if attempts == 2:
            print(f"Підказка: перша літера - {word[0]}, остання - {word[-1]}")
else:
    print(f"Гру закінчено. Правильне слово було: {word}")
