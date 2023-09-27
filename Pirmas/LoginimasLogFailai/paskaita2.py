import logging
import paskaita
#logging.basicConfig(level=logging.DEBUG, filename="aritmetika.log", format="%(asctime)s:%(levelname)s:%(message)s")

class Asmuo:
    def __init__(self,vardas,pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        logging.info(f"sukurtas darbuotojas: {self.vardas} {self.pavarde}")

tadas = Asmuo("Tadas", "tadukas")
petras = Asmuo("Jonas", "Jonukas")