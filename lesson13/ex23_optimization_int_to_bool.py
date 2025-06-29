# Before optimization
numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10]

for number in numbers:
    if number % 2 != 0:
        print(number)


print("-" * 30)
# After optimization
for number in numbers:
    if number % 2:
        print(number)
