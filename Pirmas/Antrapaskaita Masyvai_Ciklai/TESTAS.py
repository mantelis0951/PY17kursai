list = []

while True:
    input_number = int(input("Iveskite skaiciu"))
    if input_number > 0:
        list.append(input_number)
    else:
        break
        print("skaicius neigiamas")

if list:
    suma = sum(list)
    print(suma)