# -----------------------------------
# Завдання 2.
# Застосувати знижку 10% на ціни, що перевищують 100.
# Створити і вивести новий список зі зниженими цінами.

prices = [85, 150, 120, 50, 200]

discounted_prices = []

for price in prices:
    if price > 100:
        new_price = price - price * 10 / 100
        discounted_prices.append(new_price)
    else:
        discounted_prices.append(price)

print(discounted_prices)
