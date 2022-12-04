import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("CobaPlace")
window.geometry("600x100")

Button = Button(window, text="Place").place(x=10, y=10, height=35)

window.mainloop()
