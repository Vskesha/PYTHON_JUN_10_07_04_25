# -----------------------------------
# Завдання 4.
# Напишіть функцію describe_trip, яка приймає три аргументи: 
# destination (позиційний), duration (іменований) та 
# transport (значення за замовчуванням - "car"). 
# Функція повинна виводити інформацію про поїздку у форматі 
# "I am going to [destination] for [duration] days by [transport].". 
# Викличте цю функцію з різними значеннями та виведіть результати.


def describe_trip(destination, duration, transport="car"):
    """
    Виводить інформацію про поїздку.
    """
    print(f"I am going to {destination} for {duration} days by {transport}.")


describe_trip("Paris", 5)
describe_trip("London", 3, transport="train")
describe_trip("New York", 10, transport="plane")
