# 5! = 1 * 2 * 3 * 4 * 5 = 4! * 5
# 4! = 3! * 4
# 3! = 2! * 3
# 2! = 1! * 2
# 1! = 0! * 1
# 0! = 1

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(8))
print(factorial(10))
