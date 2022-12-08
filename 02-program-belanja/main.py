# Gui untuk menghitung total bayar
from tkinter import *
from tkinter import messagebox

barang = ['Mie Ayam', 'Bakso Urat']
harga = [15000, 10000]

window = Tk()
window.title("Program Belanja")
window.geometry('253x210')

teks1 = Label(window, text="Pilih Makanan yang akan Dibeli").pack()

frameHarga = Frame(window)
frameHarga.pack()

garis = Label(window, text="-"*50).pack()

frameBeli = Frame(window)
frameBeli.pack()

def spinbox():
    return Spinbox(frameBeli, from_=0, to =1000)

def tambahmenu(z):
    return Label(frameBeli, text=barang[z])

def panggil(x, y, z):
    x.grid(row=y, column=z)


for i in range(len(barang)):
    teks = barang[i] + " - " + str(harga[i])
    brg = Label(frameHarga, text=teks).grid(row=i)

spinbox1 = spinbox()
spinbox2 = spinbox()

# lambda/anonymous function dipakai karena func (def) dengan parameter akan langsung dieksesuksi,
# sementara Tkinter cuma butuh nama func tanpa tanda "()" dan argumentnya.
tmbh1 = Button(frameHarga, text=" + ", command = lambda : [panggil(tambahmenu(0), 1, 0), panggil(spinbox1, 1, 1)])
tmbh2 = Button(frameHarga, text=" + ", command = lambda : [panggil(tambahmenu(1), 2, 0), panggil(spinbox2, 2, 1)])

tmbh1.grid(row=0, column=1)
tmbh2.grid(row=1, column=1)

def hitung():
    mi = int(spinbox1.get())
    bakso = int(spinbox2.get())

    hasil = (harga[0] * mi) + (harga[1] * bakso)
    teks = "Rp"+str(hasil)
    messagebox.showinfo('Total Bayar', teks)

z = Button(window, text="Beli", command = hitung).pack(side=BOTTOM)
window.mainloop()
