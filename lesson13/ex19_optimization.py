# Before optimization
age = 25

if age >= 18 and age <= 65:
    print("Вік у допустимому діапазоні")


# After optimization
age = 25

if 18 <= age <= 65:
    print("Вік у допустимому діапазоні")
