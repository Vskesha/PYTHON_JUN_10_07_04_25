# Доступ за ключем
inventory = {
    "apples": 5,
    "oranges": 3,
    "bananas": 4,
}

print("Кількість яблук", inventory["apples"])

# print("Кількість груш", inventory["pears"])

number_of_pears = 0
if "pears" in inventory:
    number_of_pears = inventory["pears"]  
print("Кількість груш", number_of_pears)


print("Кількість груш", inventory.get("pears", 0))
