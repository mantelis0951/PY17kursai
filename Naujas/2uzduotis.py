years_from = int(input("Iveskite metus nuo: "))
years_to = int(input("Iveskite metus iki: "))

for x in range(years_from, years_to):
    if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0):
        print(f"Keliamieji metai: {x}")
    else:
        print(f"Nekeliamieji metai: {x}")

input()