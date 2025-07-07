def greet(greet, *names, **kwargs):
    
    print("Тип args:", type(names))
    print("Тип kwargs:", type(kwargs))

    print(names)
    print(kwargs)
    print()

    for name in names:
        print(f"{greet}, {name}!", end="\n")
    print()

    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet("Bonjour", 'Alice', 'Bob', "Mike", age=25, city='New York', job='Engineer')
