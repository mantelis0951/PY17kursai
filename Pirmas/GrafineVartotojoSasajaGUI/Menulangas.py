from tkinter import *

langas = Tk()

def pirmas():
    print("pirmas!")

meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)
submeniu2 = Menu(meniu, tearoff = 0)
submeniu3 = Menu(meniu, tearoff = 0)

meniu.add_cascade(label = "meniu", menu = submeniu)
submeniu.add_command(label="pirmas", command=pirmas)
submeniu.add_separator()
submeniu.add_command(label="antras")

meniu.add_cascade(label = "meniu2", menu = submeniu2)
submeniu2.add_command(label="1", command=pirmas)
submeniu2.add_command(label="2")

meniu.add_cascade(label = "meniu3", menu = submeniu3)
submeniu3.add_command(label="naujas")

langas.mainloop()