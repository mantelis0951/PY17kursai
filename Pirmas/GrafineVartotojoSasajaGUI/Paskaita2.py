from tkinter import *

langas = Tk()

uzrasas1 = Label(langas, text = "Vardas")
laukas1 = Entry(langas)
uzrasas2 = Label(langas, text = "Pavarde")
laukas2 = Entry(langas)
varnele = Checkbutton(langas, text= "Pazymekite varnele")

uzrasas1.grid(row= 0, column =0, sticky = E)
laukas1.grid(row = 0, column = 1)
uzrasas2.grid(row = 1,column = 0)
laukas2.grid(row = 1, column = 1)
varnele.grid(row = 3, columnspan = 2)


langas.mainloop()