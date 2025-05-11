answer = input("Enter your answer (так, ні, yes, no): ")

if answer.lower() == "так":
    print("Ви відповіли 'так'.")
elif answer.lower() == "ні":
    print("Ви відповіли 'ні'.")
elif answer.lower() == "yes":
    print("Ви відповіли 'так'.")
elif answer.lower() == "no":
    print("Ви відповіли 'ні'.")
else:
    print("Нерозпізнана відповідь.")
