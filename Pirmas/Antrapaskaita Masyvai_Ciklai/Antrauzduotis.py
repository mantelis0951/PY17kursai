numbers  = []

while True:
    input_number = int(input("iveskite skaiciu " ))
    if input_number > 0:
        numbers.append(input_number)
    else:
        break

if numbers:
    total_sum = sum(numbers)
    print(f"Ivestu skaiciu suma yra: {total_sum}")
else:
    print("Neivestas teigamas skaicius ")