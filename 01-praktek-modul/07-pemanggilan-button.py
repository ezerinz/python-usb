import tkinter as tk

win = tk.Tk()
win.title("CobaButton")
win.geometry("600x300")

tombol1 = tk.Button(win, text="Home").pack()
tombol2 = tk.Button(win, text="Informasi").pack()

win.mainloop()
