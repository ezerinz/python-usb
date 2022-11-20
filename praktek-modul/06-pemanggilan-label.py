import tkinter as tk 

win = tk.Tk()
win.title("CobaLabel")
win.geometry("600x300")

label1 = tk.Label(win, text="My First Text", font=15, bg="green", fg="white").pack()
label2 = tk.Label(win, text="Universitas Sulawesi Barat", font=15).pack()

win.mainloop()
