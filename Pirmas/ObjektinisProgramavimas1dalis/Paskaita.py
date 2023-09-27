class Kate:
    def __init__(self, spalva, kojos):
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


kate1 = Kate("pilka", 4)
kate2 = Kate("Juoda" , 5)

print(kate1.kojos)
print(kate2.spalva)

kate2.spalva = "Zalia"
print(kate2.spalva)

kate1.miaukseti()
kate1.begti()