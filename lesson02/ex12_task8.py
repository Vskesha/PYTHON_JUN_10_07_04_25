dollars = 1500

dollar_price = 41.4733
euro_price = 43.0327

exchange_rate = dollar_price / euro_price
euros = round(dollars * exchange_rate, 2)

print(dollars, "доларів =", euros, "євро")
