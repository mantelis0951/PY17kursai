from tkinter import *

langas = Tk()
langas.geometry("300x100")
def spausdina():
    ivesta = laukas.get()
    output["text"] = "Labas, " + ivesta + "!"
def spausdinti3(event):
    ivesta = laukas.get()
    output["text"] = ivesta

uzrasas = Label(langas, text = "Iveskite varda: ")
laukas = Entry(langas)
output = Label(langas, text="")
mygtukas = Button(langas, text = "Patvirtinti", command = spausdina, bg='grey')
mygtukas.bind("<Return>", spausdinti3)

uzrasas.grid(row = 0, column =0)
laukas.grid(row = 0, column = 1)
mygtukas.grid(row = 0, column = 3)
output.grid(row = 2, columnspan = 2)

langas.mainloop()