import random

quick_picks = int(input("How many quick picks? "))
for i in range(quick_picks):
    numbers = []
    for y in range(6):
        number = random.randint(1,45)
        while number in numbers:
            number = random.randint(1,45)
        numbers.append(number)
    print(" ".join(str(number) for number in numbers))
