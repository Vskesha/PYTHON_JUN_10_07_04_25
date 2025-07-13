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
