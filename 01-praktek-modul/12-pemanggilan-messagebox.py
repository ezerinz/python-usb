from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("CobaMessageBox")
win.geometry("600x300")

def clicked():
    messagebox.showinfo("CobaMessage", "Terima kasih")

btn = Button(win, text="Tekan", command=clicked).pack()

win.mainloop()
