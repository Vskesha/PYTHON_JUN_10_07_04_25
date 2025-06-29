# Before optimization
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number > 3:
        print(number)


# After optimization
numbers = [4, 5]

for number in numbers:
    print(number)
