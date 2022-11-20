from tkinter import *

win = Tk()
win.title("CobaRadioButton")
win.geometry("600x300")

RadioB1 = Radiobutton(win, text="Teknik Informatika", value=1).pack()
RadioB2 = Radiobutton(win, text="Sistem Informasi", value=2).pack()

win.mainloop()
