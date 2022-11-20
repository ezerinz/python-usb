from tkinter import *

win = Tk()
win.title("CobaScale")
win.geometry("600x300")

Sc = Scale(length=100, from_=0, to=10)
Sc.pack()

win.mainloop()
