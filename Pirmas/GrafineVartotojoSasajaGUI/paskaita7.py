from tkinter import *
from PIL import ImageTk, Image

langas = Tk()

img = ImageTk.PhotoImage(Image.open("Pirmoji.PNG"))

panel - Label(langas, image = img)
panel.pack(fill="both", expand="yes")

langas.mainloop()