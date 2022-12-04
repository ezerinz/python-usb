import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("CobaGrid")
window.geometry("600x300")

Label1 = Label(window, text="Nama").grid(row=0)
Label2 = Label(window, text="Alamat").grid(row=1)
Entry1 = Entry(window, width=16).grid(row=0, column=1)
Entry2 = Entry(window, width=16).grid(row=1, column=1)

window.mainloop()
