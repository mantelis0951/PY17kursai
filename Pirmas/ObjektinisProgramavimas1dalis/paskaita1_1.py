class Kate:
    def __init__(self, spalva="juoda", kojos=4):
        self.spalva = spalva
        self.kojos = kojos

    def miaukseti(self):
        print("Miau")

    def _judinti_kojas(self):
        print("Judinu kojas")

    def _ziureti_kur_begi(self):
        pass ## galima pakeisti i print("judinu kojas") rasai pass kai dar nezinai ka daro

    def begti(self):
        self._judinti_kojas()
        self._ziureti_kur_begi()
        print(self.kojos)
        print("begu")

    def __str__(self):
        return f"koju skaiciu: {self.kojos}, kaciuko spalva: {self.spalva}"


    def __repr__(self):
        return f"koju skaiciu: {self.kojos}, kaciuko spalva: {self.spalva}"
# kate1 = Kate()
# kate2 = Kate("juoda", 5)
# kate3 = Kate("zalia", 3)

# kates = []
#
# kates.append(kate1)
# kates.append(kate2)
# kates.append(kate3)
#
#
# for kate in kates:
#     print(kate.spalva)

kates = []

while True:
    pasirinkimas = int(input("1 - Iveskite kate\n2 - perziureti visas kates \n3 - iseiti is programos"))
    if pasirinkimas == 1:
        spalva = input("Iveskite kates spalva: ")
        kojos = int(input("Iveskite koju skaiciu: "))
        kate = Kate(spalva, kojos)
        kates.append(kate)
    if pasirinkimas == 2:
        for kate in kates:
            print(f"kates spalva: {kate.spalva}, koju skaicius: {kate.kojos}")

    if pasirinkimas == 3:
        print("viso gero")
        break

print(kates)