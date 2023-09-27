class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return f"{self.vardas} {self.amzius}"


human1 = Zmogus("Mantas", 30)
human2 = Zmogus("Stasys", 33)
human3 = Zmogus("Jonas", 40)

humans = [human1, human2, human3]


def rusiavimas(darbuotojas):
    return darbuotojas.vardas


sort1 = sorted(humans, key=rusiavimas)
print(sort1)
sort11 = sorted(humans, key=rusiavimas, reverse=True)
print(sort11)

sort2 = sorted(humans, key=lambda e: e.amzius)
print(sort2)
sort22 = sorted(humans, key=lambda e: e.amzius, reverse=True)
print(sort22)
