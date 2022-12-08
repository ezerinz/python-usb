import tkinter as t

win = t.Tk()
win.title("Coba")
win.geometry("600x100")

def say_halo(nama):
    t.Label(win, text="Halo "+nama).pack()

def perintah():
    say_halo("Edwin")

t.Button(win, text="Click Me!", command = say_halo("Edwin")).pack()

win.mainloop()
