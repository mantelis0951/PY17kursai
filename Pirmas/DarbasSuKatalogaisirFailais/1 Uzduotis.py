import datetime

with open ("Tekstas.txt", "w", encoding="utf-8") as failas:
    failas. write("Beautiful is better than ugly\n")
    failas.seek(0)
    failas.write("Grazu yra geriau nei bjauru. \n")

laikas = datetime.datetime.now()
with open("Tekstas.txt", 'a', encoding="utf-8") as failas:

    failas.write("Zen of Python")
    failas.write(f" {laikas}\n")

with open("Tekstas.txt", 'r', encoding='utf - 8') as failas:
    for eilute in failas:
        print(eilute[::-1])

with open("Tekstas.txt", 'r+', encoding='utf - 8') as failas:
    eiluciu_kiekis = failas.readlines()
    failas.seek(0)
    eilutes_numeris = 1
    #print(eiluciu_kiekis)
    for eilute in eiluciu_kiekis:
        failas.write(f"{eilutes_numeris}. {eilute}")
        eilutes_numeris += 1


with open("Tekstas.txt", "r", encoding='utf - 8') as failas:
    uppercase = 0
    lowercase = 0

    visos_eilutes = failas.read()
    counting_words = len(visos_eilutes.split())
    counting_symbols = len(visos_eilutes)
    for symbol in visos_eilutes:
        if symbol.isupper():
            uppercase += 1
        elif symbol.islower():
            lowercase += 1

print(f"zodziu faile:{counting_words}")
print(f"simboliu faile:{counting_symbols}")
print(f"Didziuju raidziu faile:{uppercase}")
print(f"Mazuju raidziu faile:{lowercase} \n")

with open("Tekstas.txt", 'r', encoding='utf = 8') as failas:
    for eilute in failas:
        print(eilute.upper())
# with open("Tekstas.txt", 'r', encoding="utf-8") as failas:
#     linenumber = 1
#     for eilute in failas:
#         print(f"{linenumber}. {eilute}")
#         linenumber += 1
#     #
    # print(failas.readline())



