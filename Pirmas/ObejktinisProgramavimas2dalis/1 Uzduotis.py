class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas, rudys):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        self.rudys = rudys

    def vaziuoti(self):
        print("Vaziuoja")

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self):
        print("Degalai ipilti")


automobilis = Automobilis(2000,"Leon", "Dyzelinas", "rudziu yra")
automobilis1 = Automobilis(2010, "F10","Dyzelinis","rudziu nera")

automobilis2 = Automobilis(1989, "190e", "Benzinas", "rudziu yra")

print(automobilis.metai, automobilis.modelis, automobilis.kuro_tipas, automobilis.rudys)

automobilis1.stoveti()
automobilis1.vaziuoti()
automobilis1.pildyti_degalu()

class Elektromobilis(Automobilis):
    def pildyti_degalu(self):
        print("Baterija ikrauta")

    def vaziuoti_autonomiskai(self):
        print("Vaziuoja autonomiskai")


elektromobilis = Elektromobilis(2018, "modelis: Tesla,","Kuro tipas: Baterija,", "rudziu nera")

print(elektromobilis.metai, elektromobilis.modelis, elektromobilis.kuro_tipas, elektromobilis.rudys)

elektromobilis.vaziuoti()
elektromobilis.stoveti()
elektromobilis.pildyti_degalu()
elektromobilis.vaziuoti_autonomiskai()
