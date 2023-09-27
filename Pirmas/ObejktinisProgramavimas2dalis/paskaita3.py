class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    pass

class IslaiduIrasas(Irasas):
    pass

biudzetas = []

irasas = PajamuIrasas(200)
irasas2 = IslaiduIrasas(300)

biudzetas.append(irasas)
biudzetas.append(irasas2)

for x in biudzetas:
    if isinstance(x, PajamuIrasas):
        print(x.suma, "pajamos")
    elif isinstance(x, IslaiduIrasas):
        print(x.suma, "cia yra islaidos")