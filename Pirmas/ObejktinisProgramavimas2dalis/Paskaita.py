class Gyvunas:
    def __init__(self, vardas, spalvas):
        self.vardas = vardas
        self.spalva = spalvas

    def begti(self):
        print("Begu")

class Kate(Gyvunas):
    def miaukseti(self):
        print("Miau")

class Suo(Gyvunas):
    def lojimas(self):
        print("Au")

class Vezlys(Gyvunas):
    def begti(self):
        print("Labai letai judu")


vezlys = Gyvunas("Vezlius", "zalias")
suo = Suo ("Murkis", "juodas")
kate = Kate("murkis", "juodas")
vezlys2 = Vezlys ("letunas", "zalias")

vezlys.begti()

suo.lojimas()
kate.begti()
kate.miaukseti()
vezlys2.begti()