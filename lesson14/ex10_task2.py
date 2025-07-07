# -----------------------------------
# Завдання 2. 
# Напишіть функцію introduce_person, яка приймає 
# іменовані аргументи: name, age та city, і 
# виводить інформацію про людину у форматі 
# "My name is [name], I am [age] years old and I 
# live in [city]". Викличте цю функцію 3 рази з 
# різними значеннями та виведіть результати.


def introduce_person(name, age, city):
    print(f"My name is {name}, I am {age} years old and I live in {city}.")


introduce_person("Alice", 30, "New York")
introduce_person(name="Bob", age=25, city="London")
introduce_person(name="Charlie", age=35, city="Paris")
