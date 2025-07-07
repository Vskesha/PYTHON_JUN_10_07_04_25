def get_min_max(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    return min_value, max_value

result = get_min_max([1, 2, 3, 4, 5])
print(result)

min_val, max_val = get_min_max([10, 20, 30, 40, 50])
print(f"Min: {min_val}, Max: {max_val}")
