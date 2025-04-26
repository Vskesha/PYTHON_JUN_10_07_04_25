# "Введіть ваше повне ім'я: "
# "Який ваш улюблений колір? "
# "Привіт, {0}! Твій улюблений колір {1}? Чудовий вибір!"

user_input = input("Введіть ваше повне ім'я: ")
favorite_color = input("Який ваш улюблений колір? ")
formatted_name = user_input.title()

message = "Привіт, {0}! Твій улюблений колір {1}? Чудовий вибір!".format(formatted_name, favorite_color.lower())
print(message)

message = f"Привіт, {formatted_name}! Твій улюблений колір {favorite_color}? Чудовий вибір!"
print(message)
