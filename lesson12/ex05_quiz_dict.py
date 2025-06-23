# Який результат виведення цього коду?

person = {"name": "Vika", "age": 30}
print(person["name"])
# vika

inventory = {'pen': 10, 'pencil': 5}
print(inventory.get('eraser', 'Not in stock'))
# Not in stock

# inventory = {'pen': 10, 'pencil': 5}
# print(inventory['eraser'])
# # KeyError: 'eraser'

inventory = {'pen': 10, 'pencil': 5}
print(inventory['pencil'])
# 5

inventory = {'pen': 10, 'pencil': 5}
print(inventory.get('eraser', None))
# None

profile = {'username': 'Emma', 'visits': 8}
profile['visits'] += 2
print(profile)
# {'username': 'Emma', 'visits': 10}
