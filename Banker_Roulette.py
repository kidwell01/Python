import random

size = len(names)
print(size)
random_number = random.randint(0, size - 1)
print(random_number)

person_to_buy = names[random_number]
print(f"{person_to_buy} is going to buy the meal today!")