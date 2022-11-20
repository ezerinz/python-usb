import tkinter as t

win = t.Tk()
win.title("Coba")
win.geometry("600x100")

def say_halo():
    t.Label(win, text="Halo!").pack()

t.Button(win, text="Click Me!", command=say_halo).pack()

win.mainloop()
