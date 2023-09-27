def equal():
    input_number = input("iveskite skaiciu: ")
    input_numbers_digits_sum = 0

    for digit in input_number:
        if digit.isdigit():
            input_numbers_digits_sum += int(digit)

    if input_numbers_digits_sum % 2 == 0:
        first_half = input_number[0:len(input_number) // 2]
        second_half = input_number[-(len(input_number) // 2):]
        if first_half == second_half:
            return True
        else:
            return False
    else:
        print("Ivesto skaiciaus skaitmenu suma nera lygine")
result = equal()
print(result)

# def nextnum():
#     input_number = int(input("iveskite skaiciu: "))