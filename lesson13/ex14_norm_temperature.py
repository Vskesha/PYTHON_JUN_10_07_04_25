import random
import time

temperature = 55

while temperature > 32 and temperature < 90:
    print("Температура в нормі:", temperature, end="\r")
    temperature += random.randint(-5, 5)
    time.sleep(0.2)

print("Температура вийшла за межі норми!", temperature)
