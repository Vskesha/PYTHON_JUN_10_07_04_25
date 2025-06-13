nums = [1, 17, 3, 10, 4, 20, 5, 8, 13]

# Довжина списку
list_length = len(nums)
print("Довжина списку:", list_length)

# Максимальне число в списку
max_value = max(nums)
print("Максимальне число:", max_value)

# Мінімальне число в списку
min_value = min(nums)
print("Мінімальне число:", min_value)

# Сума всіх чисел в списку
sum_of_numbers = sum(nums)
print("Сума всіх чисел:", sum_of_numbers)

# Середнє значення чисел в списку
average_value = sum_of_numbers / list_length
print("Середнє значення :", average_value)

# Обернений список
print("Оригінальний список:", nums)
nums.reverse()
print("Обернений список:", nums)
