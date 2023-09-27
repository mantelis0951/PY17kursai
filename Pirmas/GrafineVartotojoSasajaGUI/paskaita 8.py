from tkinter import *
from PIL import ImageTk, Image

langas = Tk()

kintamas = 10

def keisti():
    kintamas = 15

def spausdinti():
    print(kintamas)

mygtukas_k = Button(langas, text = "keisti", command=keisti)
mygtukas_s = Button(langas,text = "spausdinti", command=spausdinti)

mygtukas_k.pack()
mygtukas_s.pack()