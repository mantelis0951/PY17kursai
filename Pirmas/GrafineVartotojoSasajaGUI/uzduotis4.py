from tkinter import *

langas = Tk()
langas.geometry("300x100")


def spausdina():
    global last_input
    ivesta = laukas.get()
    output["text"] = "Labas, " + ivesta + "!"
    last_input = ivesta

    separator = Label(langas, text="------------------------------------------------------------")
    separator.grid(row=5, column=0, columnspan=4)

    sukurta_label = Label(langas, text="Sukurta")
    sukurta_label.grid(row=6, column=0, columnspan=4)
def isvalyti():
    output["text"] = " "

    separator = Label(langas, text="------------------------------------------------------------")
    separator.grid(row=5, column=0, columnspan=4)

    sukurta_label = Label(langas, text="Išvalyta")
    sukurta_label.grid(row=6, column=0, columnspan=4)


def close_program():
    langas.destroy()


def atkurti():
    output["text"] = "Labas, " + last_input + "!"

    separator = Label(langas, text="------------------------------------------------------------")
    separator.grid(row=5, column=0, columnspan=4)

    sukurta_label = Label(langas, text="Atkurta")
    sukurta_label.grid(row=6, column=0, columnspan=4)


meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)

meniu.add_cascade(label = "meniu", menu = submeniu)
submeniu.add_command(label="Išvalyti", command=isvalyti)
submeniu.add_command(label="Atkurti paskutinį", command=atkurti)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=close_program)


uzrasas = Label(langas, text = "Iveskite varda: ")
laukas = Entry(langas)
output = Label(langas, text="")
mygtukas = Button(langas, text = "Patvirtinti", command = spausdina, bg='grey')
mygtukas.bind("<Return>", spausdina)

uzrasas.grid(row = 0, column =0)
laukas.grid(row = 0, column = 1)
mygtukas.grid(row = 0, column = 3)
output.grid(row = 2, columnspan = 2)


langas.mainloop()