class Darbuotojas:
    def __init__(self,vardas,pavarde,atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.__atlyginimas = atlyginimas

    @property
    def atlyginimas(self):
        return self.__atlyginimas

    def set_atlyginimas(self, naujas_atlyginimas):
        if naujas_atlyginimas <0:
            print("atlyginimas neglai but neigiamas")
        else:
            self.__atlyginimas = naujas_atlyginimas

    def get_atlyginimas(self):
        return self.__atlyginimas



domas = Darbuotojas("Domas", "Rutkauskas",1200)
# domas.atlyginimas = -1500
print(domas.atlyginimas)
domas.set_atlyginimas(1500)
print(domas.get_atlyginimas())
