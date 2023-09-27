import datetime
import pandas as pd


class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo

    def _darbuotojasnudirbo(self):
        workedtime = end_date - start_date
        return workedtime.days

    def paskaiciuoti_atlyginima(self):
        pradirbtos_dienos = self._darbuotojasnudirbo()
        bendras_atlyginimas = pradirbtos_dienos * 8 * self.valandos_ikainis
        return bendras_atlyginimas

    def __str__(self):
        return f"Darbuotojo vardas: {self.vardas}, Atlyginimas: {self.paskaiciuoti_atlyginima()}, Darbuotojas nudirbo: {self._darbuotojasnudirbo()} Dienas"


class NormalusDarbuotojas(Darbuotojas):
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        super().__init__(vardas, valandos_ikainis, dirba_nuo)

    def _darbuotojasnudirbo(self):
        start_date = datetime.datetime.strptime(input_first_date, "%Y/%m/%d")
        end_date = datetime.datetime.strptime(input_second_date, "%Y/%m/%d")
        skaiciuoti_dienas = len(pd.bdate_range(start_date, end_date))
        return skaiciuoti_dienas

    def __str__(self):
        return f"Darbuotojo vardas: {self.vardas}, Atlyginimas: {self.paskaiciuoti_atlyginima()}, Darbuotojas nudirbo: {self._darbuotojasnudirbo()} Dienas"


input_first_date = input("iveskite pirma darbo diena, formatu - (2000/01/01) : ")
input_second_date = input("Iveskite paskutine darbo diena, formatu - (2000/01/01) : ")
start_date = datetime.datetime.strptime(input_first_date, "%Y/%m/%d")
end_date = datetime.datetime.strptime(input_second_date, "%Y/%m/%d")

darbuotojas = Darbuotojas("jonas", 12, 7)

normalusdarbuotojas = NormalusDarbuotojas("Edvinas", 3, 5)

darbuotojas.paskaiciuoti_atlyginima()
normalusdarbuotojas.paskaiciuoti_atlyginima()
print(darbuotojas)
print(normalusdarbuotojas)

