from Biudzetas import *

while True:
    pasirinkimas = int(input("1 - įvesti pajamas, \n2 - įvesti išlaidas,"
                             " \n3 - gauti balansą, \n4 - parodyti ataskaitą, \n9 - išeiti iš programos"))
    if pasirinkimas == 1:
        suma = float(input("Įveskite pajamų sumą: "))
        siuntejas = input("Iveskite siunteja: ")
        papildoma_informacija = input("Iveskite papildoma informacija: ")
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, papildoma_informacija)
    if pasirinkimas == 2:
        suma = float(input("Įveskite išlaidų sumą: "))
        atsiskaitymo_budas = input("Iveskite atsiskaitymo buda: ")
        isigyta_preke_paslauga = input("Iveskite isigyta preke: ")
        biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
    if pasirinkimas == 3:
        biudzetas.gauti_balansa()
    if pasirinkimas == 4:
        biudzetas.parodyti_ataskaita()
    if pasirinkimas == 9:
        print("Viso gero")
        break
