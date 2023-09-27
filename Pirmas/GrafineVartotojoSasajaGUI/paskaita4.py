from tkinter import *

langas = Tk()

def spausdina():
    ivesta = laukas.get()
    output["text"] = ivesta

uzrasas = Label(langas, text = "Ivestas zodis")
laukas = Entry(langas)
output = Label(langas, text="")
mygtukas = Button(langas,text = "ivesti", command = spausdina)

uzrasas.grid(row = 0, column =0)
laukas.grid(row = 0, column = 1)
mygtukas.grid(row = 1, columnspan = 2)
output.grid(row = 2, columnspan = 2)

langas.mainloop()