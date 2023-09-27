from tkinter import *
langas = Tk()

def callBack(url):
    webbrowser.open_new(url)

link1 = Label(langas, text="Google", fg="blue", cursor="hand2")
link2 = Label(langas, text="Delfi", fg="blue", cursor="hand2")

link1.bind("<Button-1>", lambda e: callBack("www.google.lt"))
link2.bind("<Button-1>", lambda e: callBack("www.delfi.lt"))
link1.pack()
link2.pack()

langas.mainloop()