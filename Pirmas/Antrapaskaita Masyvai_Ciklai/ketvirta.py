import random
numbers = []

for number in range(3):
    threenumbers = random.randint(1, 6)
    numbers.append(threenumbers)
for number in numbers:
    print(number)

if number != 5:
    print("Laimejai")
else:
    print("Pralaimejai")
