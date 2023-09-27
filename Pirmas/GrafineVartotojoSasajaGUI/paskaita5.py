from tkinter import *

langas = Tk()

def spausdinti():
    pasirinkta = sarasas[boksas.curselection()[0]]
    labelis1["text"] = pasirinkta

scrollbaras = Scrollbar(langas)
boksas = Listbox(langas, yscrollcommand=scrollbaras.set)
scrollbaras.config(command=boksas.yview)
sarasas = range(1,201)
boksas.insert(END, *sarasas)
mygtukas = Button(langas,text = "spausdinti", command=spausdinti)
labelis1 = Label(langas, text="")



boksas.pack(side=LEFT)
mygtukas.pack()
labelis1.pack()
scrollbaras.pack(side=RIGHT, fill = Y)
langas.mainloop()