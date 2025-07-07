# Іменовані аргументи
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Bob")

# Позиційні аргументи
def add(a, b):
    return a + b

result = add(2, 3)
print(result)

# Значення за замовчуванням
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")
greet("Bob", "Hi")
