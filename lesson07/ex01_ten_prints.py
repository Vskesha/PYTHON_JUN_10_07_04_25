print("Hello, world!")
print("Hello, world!")
print("Hello, world!")
print("Hello, world!")
print("Hello, world!")
print("Hello, world!")
print("Hello, world!")
print("Hello, world!")
print("Hello, world!")
print("Hello, world!")

print("-" * 50)

for counter in range(1, 11):
    if counter == 5:
        continue
    if counter > 8:
        break
    print("Hello, world!", counter)

print("-" * 50)

counter = 1
while counter < 11:
    if counter > 8:
        break
    print("Hello, world!", counter)
    counter = counter + 1
