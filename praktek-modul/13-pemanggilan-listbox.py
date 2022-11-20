from tkinter import *
from typing import List

win = Tk()
win.title("CobaListbox")
win.geometry("600x100")

ListB = Listbox(win)
ListB.insert(1, "Python")
ListB.insert(2, "PHP")
ListB.insert(3, "Java")
ListB.insert(4, "C")
ListB.insert(5, "C++")
ListB.insert(6, "Lua")
ListB.pack()

win.mainloop()
