from tkinter import *

win = Tk()
win.title("CobaSpinbox")
win.geometry("600x300")

spin = Spinbox(win, from_=0, to=50).pack()

win.mainloop()
