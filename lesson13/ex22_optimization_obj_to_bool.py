# Before optimization
text = ""

while text != "stop":
    text = input("Введи слово (для завершення введи stop): ")
    print("Ви ввели:", text)

print("Ви завершили введення слів.")


# After optimization
while True:
    word = input("Введи слово (для завершення натисни Enter): ")
    # if word:
    #     print("Ви ввели:", word)
    # else:
    #     break
    if not word:
        break
    print("Ви ввели:", word)

print("Ви завершили введення слів.")
