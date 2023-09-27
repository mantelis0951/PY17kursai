class Tevas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde


class Vaikas(Tevas):
    def __init__(self,vardas, pavarde, mokymosi_istaiga):
        super().__init__(vardas, pavarde)
        self.mokymosi_istaiga = mokymosi_istaiga

tevas = Tevas("jonas", "jonaitis")
vaikas = Vaikas("petras", "petraitis", "mokykla")

print(vaikas.mokymosi_istaiga)