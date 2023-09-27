years: int = int(input("Iveskite metus: "))

if years % 4 == 0 and (years % 100 != 0 or years % 400 == 0):
    print("Keliamieji metai")
else:
    print("Nekeliamieji metai")
