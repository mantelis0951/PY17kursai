class Irasas:
    def __init__(self, suma):
        self.suma = suma
    def __str__(self):
        return f"{self.suma}"

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija

class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
class Biudzetas:
    def __init__(self):
        self.zurnalas = []
    def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_informacija):
        pajamos = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(pajamos)
    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        islaidos = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(islaidos)
    def gauti_balansa(self):
        for x in self.zurnalas:
            if isinstance(x, PajamuIrasas):
                print(x.suma, "pajamos")
            elif isinstance(x, IslaiduIrasas):
                print(x.suma, "cia yra islaidos")
    def parodyti_ataskaita(self):
        for x in self.zurnalas:
            if isinstance(x, PajamuIrasas):
                print(x.suma, "pajamos")
            elif isinstance(x, IslaiduIrasas):
                print(f"Atsiskaitymo budas: {x.atsiskaitymo_budas}, suma: {x.suma}, isigyta prekes paslauga: {x.isigyta_preke_paslauga} ")


biudzetas = Biudzetas()
while True:
    pasirinkimas = int(input("1 - įvesti pajamas, \n2 - įvesti išlaidas, \n3 - gauti balansą, \n4 - parodyti ataskaitą, \n9 - išeiti iš programos"))
    if pasirinkimas == 1:
        suma = float(input("Įveskite pajamų sumą: "))
        siuntejas = input("Iveskite siuntėja: ")
        papildoma_informacija = input("Iveskite papildoma informacija ")
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, papildoma_informacija)
    if pasirinkimas == 2:
        suma = float(input("Įveskite išlaidų sumą: "))
        atsiskaitymo_budas = input("Iveskite atsiskaitymo buda ")
        isigyta_preke_paslauga = input("Iveskite isigytos prekes paslauga ")
        biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
    if pasirinkimas == 3:
        biudzetas.gauti_balansa()
    if pasirinkimas == 4:
        biudzetas.parodyti_ataskaita()
        input()
    if pasirinkimas == 9:
        print("Viso gero")
        break