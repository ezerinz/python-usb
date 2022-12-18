import mysql.connector as sql
from tkinter import *
from tkinter import messagebox as msg
#== memeriksa apakah database ada, jika tidak, maka dibuat ==
mydb = sql.connect(
  host="localhost",
  user="root",
  password="")

mydb.cursor().execute("CREATE DATABASE IF NOT EXISTS mahasiswa")
mydb.close()
# ==========================================================

# connect
db = sql.connect(host="localhost",
                 user="root",
                 password="",
                 database="mahasiswa")

cursor = db.cursor()
cursor.execute("SHOW TABLES LIKE 'biodata'")
if not cursor.fetchall():
    cursor.execute("CREATE TABLE biodata(nim VARCHAR(8) PRIMARY KEY, nama VARCHAR(255), nilai INT, angkatan VARCHAR(4))")
    cursor.execute("INSERT INTO biodata(nim, nama, nilai, angkatan) VALUES('D0000000', 'Default', 0, '2021')")
    db.commit()

def delete(a, i, win):
    perintah = f"DELETE FROM biodata WHERE nim='{a.get()}'"
    cursor.execute(perintah)
    db.commit()
    for label in win.grid_slaves():
        if int(label.grid_info()["row"]) == i:
            label.grid_forget()

def update(a, b, c, d, e, f):
    a = a.get()
    b = b.get()
    c = c.get()
    f = f.get()

    check = f"SELECT nim FROM biodata WHERE nim='{a}'"
    cursor.execute(check)
    tangkap = cursor.fetchone()
    #print(cursor.fetchone())
    if a == "" or b == "" or c == "" or f == "":
        msg.showwarning("!", "Isi Semua!")
        e.destroy()
        utama(data)
    elif not c.isdigit():
        msg.showwarning("!", "Isi Nilai dengan Angka!")
        e.destroy()
        utama(data)
    elif len(f) != 4:
        msg.showwarning("!", "Isi Tahun Masuk dengan Benar!")
        e.destroy()
        utama(data)
    elif len(a) != 8:
        msg.showwarning("!", "NIM harus 8 karakter!")
        e.destroy()
        utama(data)
    else: 
        if a == d or not tangkap:
            perintah1 = f"UPDATE biodata SET nim='{a}' WHERE nim='{d}'"
            perintah2 = f"UPDATE biodata SET nama='{b}' WHERE nim='{a}'"
            perintah3 = f"UPDATE biodata SET nilai={int(c)} WHERE nim='{a}'"
            perintah4 = f"UPDATE biodata SET angkatan='{f}' WHERE nim='{a}'"

            cursor.execute(perintah1)
            cursor.execute(perintah2)
            cursor.execute(perintah3)
            cursor.execute(perintah4)
            db.commit()
            msg.showinfo("", "DATA DIUPDATE!")
            e.destroy()
            utama(data)
        else:
            msg.showwarning("!", "NIM sudah ada!")
            e.destroy()
            utama(data)
def utama(data):
    root = Tk()
    root.geometry("800x400")
    d = data
    
    Label(root, text="NIM", font=('Arial',12,'bold')).grid(row=0, column=0)
    Label(root, text="Nama", font=('Arial',12,'bold')).grid(row=0, column=1)
    Label(root, text="Nilai", font=('Arial',12,'bold')).grid(row=0, column=2)
    Label(root, text="Tahun Masuk", font=('Arial',12,'bold')).grid(row=0, column=3)
    for i in range(len(d)):
        row = i+1
        eNim = Entry(root, width=12, font=('Arial',12,'bold'))
        eNim.grid(row=row, column=0, padx=5, pady=2)
        eNim.insert(END, d[i][0])

        eNama = Entry(root, width=35, font=('Arial',12,'bold'))
        eNama.grid(row=row, column=1, padx=5, pady=2)
        eNama.insert(END, d[i][1])
    
        eNilai = Entry(root, width=7, font=('Arial',12,'bold'))
        eNilai.grid(row=row, column=2, padx=5, pady=2)
        eNilai.insert(END, d[i][2])

        eTahun = Entry(root, width=10, font=('Arial',12,'bold'))
        eTahun.grid(row=row, column=3, padx=5, pady=2)
        eTahun.insert(END, d[i][3])

        #labl = Label(root, text=z[i][j])
        #labl.grid(row=i, column=j)
        btnDel = Button(root, text="Delete", command=lambda a=eNim, i=row: [delete(a, i,root)])
        btnDel.grid(row=row, column=4, padx=5, pady=2)
    
        btnUpd = Button(root, text="Update", command=lambda a=eNim, b=eNama, c=eNilai, d=eNim.get(), f=eTahun: update(a, b, c, d, root, f))
        btnUpd.grid(row=row, column=5, padx=5, pady=2)
    z = Button(root, text="Create", command=lambda: create(root))
    z.grid(row=1000, column=5, pady=40, padx=5)
    y = Button(root, text="Read", width=5, command=lambda: read(root))
    y.grid(row=1000, column=4, pady=40, padx=5)
    root.mainloop()


def setDisplay(*args):
    perintah = "SELECT * FROM biodata"
    #c.destroy()
    #utama()
     
    cursor.execute(perintah)
    data = cursor.fetchall()
    

    if args:
        a = args[0].lower()
        b = args[1].get()
        if a != "semua":
            if b == "":
                msg.showwarning("!", "Isi Inputan")
            else:
                if a == "nim":
                    perintah = f"SELECT * FROM biodata WHERE nim='{b}'"
                elif a == "nama":
                    perintah = f"SELECT * FROM biodata WHERE nama='{b}'"
                elif a == "nilai":
                    perintah = f"SELECT * FROM biodata WHERE nilai='{b}'"
                elif a == "tahun masuk":
                    perintah = f"SELECT * FROM biodata WHERE angkatan='{b}'"
                cursor.execute(perintah)
                data = cursor.fetchall()
                args[2].destroy()
                utama(data)
        else:
            args[2].destroy()
            utama(data)

    return data
       
def read(win):
    win.destroy()
    root = Tk()
    root.geometry("300x100")
    options= ["Semua", "NIM", "Nama", "Nilai", "Tahun Masuk"]
    clicked = StringVar()
    clicked.set(options[0])
    drop = OptionMenu(root, clicked, *options)
    drop.pack()
    ent = Entry(root)
    ent.pack()
    btn = Button(root, text="Konfirmasi", command=lambda: setDisplay(clicked.get(), ent, root))
    btn.pack()
    root.mainloop()

def create(win):
    win.destroy()
    ya = Tk()
    Label(ya, text="NIM").grid(row=0, column=0)
    Label(ya, text="Nama").grid(row=1, column=0)
    Label(ya, text="Nilai").grid(row=2, column=0)
    Label(ya, text="Tahun Masuk").grid(row=3, column=0)
    nim = Entry(ya)
    nim.grid(row=0, column=1)
    nama= Entry(ya)
    nama.grid(row=1, column=1)
    nilai= Entry(ya)
    nilai.grid(row=2, column=1)

    options= [*range(2015, 2023)]
    clicked = StringVar()
    clicked.set(options[-1])
    drop = OptionMenu(ya, clicked, *options)
    drop.grid(row=3, column=1)
    
    def z(a, b, c, d, e):
        check = f"SELECT nim FROM biodata WHERE nim='{a.get()}'"
        cursor.execute(check)
        get = cursor.fetchone()

        if a.get() == "" or b.get() == "" or c.get() == "":
            msg.showwarning("!", "Isi Semua!")
        else:
            if not c.get().isdigit():
                msg.showwarning("!", "ISI NILAI DENGAN ANGKA!")
            elif get:
                msg.showwarning("!", "NIM SUDAH ADA!")
            elif len(a.get()) != 8:
                msg.showwarning("!", "NIM HARUS 8 KARAKTER!")
            else:
                printah = f"INSERT INTO biodata(nim, nama, nilai, angkatan) VALUES('{a.get()}', '{b.get()}', {int(c.get())}, '{e}')"
                cursor.execute(printah)
                db.commit()
                d.destroy()
                utama(data)
        
    ey = Button(ya, text="Tambah", command=lambda: z(nim, nama, nilai, ya, clicked.get()))
    ey.grid(row=4, columnspan=2, pady=15)

    ya.mainloop()

data=setDisplay()
utama(data)
