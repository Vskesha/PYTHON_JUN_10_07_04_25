# Завдання 2

# Створіть список з датами днів народжень ваших друзів у форматі "ММ-ДД" 
# (наприклад, "04-21" для 21 квітня). Ви їдете відпочивати на море 
# у липні та серпні, тому не зможете бути на деяких днях народження.
# Створіть новий список дат, в якому не буде дат з липня та серпня і відсортуйте його.

date_list = ["11-25", "07-30", "08-15", "10-10", "07-22", "12-24", "09-01", "07-03", "04-06"]
# Видалити дати з липня та серпня

new_date_list = []
for date in date_list:
    if date.startswith(("07", "08")):
        continue
    new_date_list.append(date)

new_date_list.sort()
print(new_date_list)
