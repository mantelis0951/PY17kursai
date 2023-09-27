from tkinter import *

langas = Tk()

langas.geometry("500x900")

uzrasas = Label(langas,text = "Tiesiog tekstas")

virsutinis = Frame(langas)
apatinis = Frame(langas)

mygtukas1 = Button(virsutinis, text = "1 mygtukas")
mygtukas2 = Button(virsutinis, text = "2 mygtukas")
mygtukas3 = Button(virsutinis, text = "3 mygtukas")
mygtukas4 = Button(apatinis, text = "4 mygtukas")

virsutinis.pack()
apatinis.pack(side = BOTTOM)
mygtukas1.pack(side = LEFT)
mygtukas2.pack(side = LEFT)
mygtukas3.pack(side = LEFT)
mygtukas4.pack()
uzrasas.pack()

langas.mainloop()