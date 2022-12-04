import tkinter as tk

win = tk.Tk()
win.title("CobaEntry")
win.geometry("600x300")

Entry1 = tk.Entry(win, bg="green", fg="white").pack()
Entry2 = tk.Entry(win).pack()

win.mainloop()
