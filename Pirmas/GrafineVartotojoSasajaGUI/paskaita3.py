from tkinter import *

langas = Tk()
langas.geometry("400x500")

def spausdinti():
    print("Paspaustas kairys")

def spausdinti2(event):
    print("Paspaustas Desinys")

def spausdinti3(event):
    print("Paspaustas Enter")

mygtukas = Button(langas, text="Spausdinti")
mygtukas.pack()

mygtukas.bind("<Button-1>", spausdinti)
mygtukas.bind("<Button-3>", spausdinti2)
mygtukas.bind("<Return>", spausdinti3)

langas.mainloop()