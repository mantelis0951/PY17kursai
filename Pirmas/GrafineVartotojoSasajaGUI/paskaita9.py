from tkinter import *

langas = Tk()

class Demo1:
    def __init__(self,master):
        self.master = master
        self.frame = Frame(self.master)
        self.button = Button(self.master, text="new window", width=25, command=self.new_window)
        self.button.pack()
        self.frame.pack()

    def new_window(self):
        self.window = Toplevel(self.master)
        self.window2 = Demo2(self.window)

class Demo2:
    def __init__(self,master):
        self.master = master
        self.frame = Frame(self.master)
        self.button = Button(self.master, text="Quit", width=25, command=self.close_window)
        self.button.pack()
        self.frame.pack()

    def close_window(self):
        self.master.destroy()

Demo1(langas)

langas.mainloop()