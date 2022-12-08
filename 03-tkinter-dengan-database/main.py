import sqlite3 as sql
import tkinter as tk
import tkinter.messagebox as mb

""" ======================= COLOR ======================== """
# 0 - label(default), 1 - frame, 2 - label alert, 3 - entry & button, 4 - radiobutton
def dark(widget, type=0):
    widget['background'] = "#282a34" if type == 3 else "#191920" 
    if type != 1:
        widget['foreground'] = "#D0342C" if type == 2 else "#ffffff" 
        widget['highlightbackground'] = "#282a34" if type == 3 else "#191920" 
        widget['relief'] = "flat"
        if type == 4:
            widget['selectcolor'] = "#282c34"

""" ======================= COLOR ======================== """

""" ====================================================== """

""" ======================= SQL ======================== """
class Database:
    def __init__(self, dbname):
        self.dbname = dbname
        self.con = sql.connect(self.dbname)
        self.cur = self.con.cursor()

    def close(self):
        self.con.close()

def checkLogin(u, p, f):
    db = Database("data.db")

    #check table
    checkTable = db.cur.execute("SELECT name FROM sqlite_master WHERE name='dataUser'")
    
    if checkTable.fetchone() is None:
        db.cur.execute("CREATE TABLE dataUser(noid INTEGER PRIMARY KEY, nama varchar, umur int, alamat varchar, username varchar, password varchar, saldo varchar)")
    
    username = u.get().lower()
    password = p.get() #no encrypt/decrypt

    statement = f"SELECT nama, noid FROM dataUser WHERE username='{username}' AND password='{password}';"
    eks = db.cur.execute(statement)
    get = eks.fetchone()
    global loginName
    global noID
    if not get:
        tulis = tk.Label(f, text="Password atau Username Salah", font=("Noto Sans", 8, "bold"))
        tulis['background'] = "#191920"
        tulis['foreground'] = "#D0342C"
        tulis.place(x=0, y=155)
    else:
        loginName = get[0]
        noID = get[1]
        loginSucces(f)

    db.con.close()


def getSaldo():
    db = Database("data.db")

    eks = db.cur.execute(f"SELECT saldo FROM dataUser WHERE noid='{noID}'")
    tangkap = eks.fetchone()
    db.con.close()
    return tangkap[0]

def tarik(z, y, f1, f2, f3):
    jumlah=0
    noPilih = True if z == "0" else False
    getJ = y.get()
    noDigit = True if getJ.isdigit() != True else False
    z = int(z)
    if z == 1:
        jumlah = 50000
    elif z == 2:
        jumlah = 100000
    elif z == 3:
        jumlah = 200000
    elif z == 4 and noDigit == False:
        jumlah = float(getJ)
    
    sld = float(getSaldo())
    
    if noPilih == True:
        mb.showwarning("!", "Pilih Salah Satu!")
    elif z == 4 and noDigit == True:
        mb.showwarning("!","Input Dengan Benar!")
    else:
        if sld > jumlah:
            sisa = sld - jumlah
            sisa = str(sisa)
            db = Database("data.db")

            e = db.cur.execute(f"UPDATE dataUser SET saldo = '{sisa}' WHERE noid='{str(noID)}'")
            db.con.commit()

            check = db.cur.execute(f"SELECT saldo FROM dataUser WHERE noid='{str(noID)}'")
            fetch = check.fetchone()
            
            #utk konfirmasi
            if fetch[0] == sisa:
                mb.showinfo("", "Berhasil!")
                backtoMenu(f1, f2, f3)
        else:
            mb.showwarning("","Saldo Tidak Cukup!")

def setor(x, y, z):    
    tambah = x.get()
    if tambah.isdigit() != True:
        mb.showwarning("", "Input Dengan Benar!")
    else:
        saldo = float(getSaldo())
        tambah = float(tambah)
        db = Database("data.db")
    
        jumlah = saldo + tambah
        jumlah = str(jumlah)
        e = db.cur.execute(f"UPDATE dataUser SET saldo = '{jumlah}' WHERE noid='{str(noID)}'")
        db.con.commit()

        check = db.cur.execute(f"SELECT saldo FROM dataUser WHERE noid='{str(noID)}'")
        fetch = check.fetchone()

        if fetch[0] == jumlah:
            mb.showinfo("", "Berhasil!")
            backtoMenu(y, y, z)
        else:
            mb.showwarning("", "Terjadi Masalah")
 
def pin(x, y, z, w):
    db = Database("data.db")
    
    check = db.cur.execute(f"SELECT password FROM dataUser WHERE noid='{str(noID)}'")
    fetch = check.fetchone()[0]
    
    oldPin = x.get()
    newPin = y.get()
    if oldPin == fetch:
        if len(newPin) != 6:
            mb.showwarning("", "Pin Harus 6 Karakter!")
        else:
            e = db.cur.execute(f"UPDATE dataUser SET password = '{newPin}' WHERE noid='{str(noID)}'")
            db.con.commit()

            check = db.cur.execute(f"SELECT password FROM dataUser WHERE noid='{str(noID)}'")
            fetch = check.fetchone()

            if fetch[0] == newPin:
                mb.showinfo("", "Berhasil!")
                logOut(z, w)
    else:
        mb.showwarning("", "Pin Salah!")

    db.con.close()


""" ======================= SQL ======================== """

""" ==================================================== """
def loginSucces(frame):
    frame.destroy()
    Menu()

def backtoMenu(frame1, frame2, frame3):
    frame1.destroy()
    frame2.destroy()
    frame3.destroy()
    Menu()

def pindah(frame, frame2, pilih):
    frame.destroy()
    frame2.destroy()

    if pilih == 1:
        TarikTunai()
    elif pilih == 2:
        SetorTunai() 
    elif pilih == 3:
        GantiPin()

def TarikTunai():
    frame = tk.Frame(window)
    frame.place(x=95, y=170)
    dark(frame, 1)
 
    frameKembali = tk.Frame(window)
    frameKembali.place(x=10, y=10)
    dark(frameKembali, 1)
  
    frameLagi=tk.Frame(frame)
    frameLagi.grid(row=2, column=1)
    dark(frameLagi, 1)
 
    text1 = tk.Label(frame, text="Tarik Tunai",  font=("Noto Sans", 15, "bold"))
    text1.grid(row=0, columnspan=2, pady=10)
    dark(text1)
     
    rbutton = {}
    terpilih = tk.StringVar()
    terpilih.set("0")

    rbutton['1'] = tk.Radiobutton(frame, text="Rp50000", variable=terpilih, value=1, command=lambda: terpilih.get())
    rbutton['2'] = tk.Radiobutton(frame, text="Rp100000", variable=terpilih, value=2, command=lambda: terpilih.get())
    rbutton['3'] = tk.Radiobutton(frame, text="Rp200000", variable=terpilih, value=3, command=lambda: terpilih.get())    
    rbutton['4'] = tk.Radiobutton(frameLagi, variable=terpilih, value=4, command=lambda: terpilih.get())
    
    rbutton['1'].grid(row=1, column=0, padx=7, sticky="W")
    rbutton['2'].grid(row=2, column=0, padx=7, sticky="W")
    rbutton['3'].grid(row=1, column=1, sticky="W") 
    rbutton['4'].grid(row=0, column=0)
    
    for y in rbutton:
        rbutton[y].config(font=("Noto Sans", 10, "bold"))
        dark(rbutton[y], 4)

    btnEnt = {}
    btnEnt['1'] = tk.Button(frameKembali, text="Kembali", font=("Noto Sans", 9, "bold"), command=lambda: backtoMenu(frame, frameLagi, frameKembali))
    btnEnt['2'] = tk.Entry(frameLagi, width=8)
    btnEnt['3'] = tk.Button(frame, text="Konfirmasi", font=("Noto Sans", 10, "bold"), command=lambda: tarik(terpilih.get(), btnEnt['2'], frame, frameKembali, frameLagi))
    btnEnt['1'].grid()
    btnEnt['2'].grid(row=0, column=1)
    btnEnt['3'].grid(row=3, columnspan=2, pady=20)

    for z in btnEnt:
        dark(btnEnt[z], 3)
  
def SetorTunai():
    frame = tk.Frame(window)
    frame.place(x=95, y=170)
    dark(frame, 1)
  
    frameKembali = tk.Frame(window)
    frameKembali.place(x=10, y=10)
    dark(frameKembali, 1)
    
    btnEnt = {}
    btnEnt['1'] = tk.Button(frameKembali, text="Kembali", font=("Noto Sans", 9, "bold"), command=lambda: backtoMenu(frame, frame, frameKembali))
    btnEnt['2'] = tk.Entry(frame)
    btnEnt['3'] = tk.Button(frame, text="Konfirmasi", font=("Noto Sans", 10, "bold"), command=lambda: setor(btnEnt['2'], frame, frameKembali))
    btnEnt['1'].grid() 
    btnEnt['2'].grid(row=2, column=1)
    btnEnt['3'].grid(row=3, columnspan=2, pady=20)
    for i in btnEnt:
        dark(btnEnt[i], 3)
   
    labelT = {}
    labelT['1'] = tk.Label(frame, text="Setor Tunai",  font=("Noto Sans", 15, "bold"))
    labelT['2'] = tk.Label(frame, text="Masukkan Jumlah", font=("Noto Sans", 10, "bold"))
    labelT['3'] = tk.Label(frame, text="Rp", font=("Noto Sans", 10, "bold"))
    labelT['1'].grid(row=0, columnspan=2, pady=10)
    labelT['2'].grid(row=1, columnspan=2)
    labelT['3'].grid(row=2, column=0)

    for z in labelT:
        dark(labelT[z])
 
def GantiPin():
    frame = tk.Frame(window)
    frame.place(x=65, y=170)
    dark(frame, 1)
  
    frameKembali = tk.Frame(window)
    frameKembali.place(x=10, y=10)
    dark(frameKembali, 1)
  
    btnEnt = {}
    btnEnt['1'] = tk.Button(frameKembali, text="Kembali", font=("Noto Sans", 9, "bold"), command=lambda: backtoMenu(frame, frame, frameKembali))
    btnEnt['2'] = tk.Entry(frame, show="*")
    btnEnt['3'] = tk.Entry(frame, show="*")
    btnEnt['4'] = tk.Button(frame, text="𓁹", font=("default", 6), command=lambda: showHidePassword(btnEnt['2']))
    btnEnt['5'] = tk.Button(frame, text="𓁹", font=("default", 6), command=lambda: showHidePassword(btnEnt['3']))
    btnEnt['6'] = tk.Button(frame, text="Konfirmasi", font=("Noto Sans", 10, "bold"), command=lambda: pin(btnEnt['2'], btnEnt['3'], frame, frameKembali))      
    btnEnt['1'].grid()
    btnEnt['2'].grid(row=1, column=1)
    btnEnt['3'].grid(row=2, column=1)
    btnEnt['4'].grid(row=1, column=2, pady=3, padx=5)
    btnEnt['5'].grid(row=2, column=2, pady=3, padx=5)
    btnEnt['6'].grid(row=3, columnspan=3, pady=20)
    
    for i in btnEnt:
        dark(btnEnt[i], 3)

    labelT = {}
    labelT['1'] = tk.Label(frame, text="Ganti Pin",  font=("Noto Sans", 15, "bold"))
    labelT['2'] = tk.Label(frame, text="Pin Lama", fg='#ffffff', font=("Noto Sans", 10, "bold"))
    labelT['3'] = tk.Label(frame, text="Pin Baru", fg='#ffffff', font=("Noto Sans", 10, "bold"))
    labelT['1'].grid(row=0, columnspan=3, pady=10)
    labelT['2'].grid(row=1, column=0) 
    labelT['3'].grid(row=2, column=0, pady=8)
    for z in labelT:
        dark(labelT[z])

def logOut(frame, frame2):
    frame.destroy()
    frame2.destroy()
    Utama()

def Menu():
    frameMenu = tk.Frame(window)
    frameMenu.place(x=110, y=170)
    dark(frameMenu, 1)
    getS = getSaldo()

    labelT = {}
    labelT['1'] = tk.Label(frameMenu, text="Selamat Datang, "+loginName+"!",  font=("Noto Sans", 10, "bold"))
    labelT['2'] = tk.Label(frameMenu, text="Saldo Anda: Rp"+getS,  font=("Noto Sans", 10, "bold"))
    labelT['1'].pack()
    labelT['2'].pack()
    for z in labelT:
        dark(labelT[z])
    
    frameLogout = tk.Frame(window)
    frameLogout.place(x=10, y=10)
    dark(frameLogout, 1)
     
    btn = {}
    btn['1'] = tk.Button(frameMenu, text="Tarik Tunai", command=lambda: pindah(frameMenu, frameLogout, 1))
    btn['2'] = tk.Button(frameMenu, text="Setor Tunai", command=lambda: pindah(frameMenu, frameLogout, 2))
    btn['3'] = tk.Button(frameMenu, text="Ganti Pin", command=lambda: pindah(frameMenu, frameLogout, 3))
    btn['4'] = tk.Button(frameLogout, text="Logout", command=lambda: logOut(frameMenu, frameLogout))
    btn['4'].grid()

    for i in btn:
        if i != '4':
            btn[i].pack(pady=5)
            btn[i].config(font=("Noto Sans", 10, "bold"), width=15)
        btn[i].config(font=("Noto Sans", 9, "bold"))
        dark(btn[i], 3)

def showHidePassword(entryPw):
    if entryPw.cget('show') == '':
        entryPw.config(show="*")
    else:
        entryPw.config(show="")

def Utama():
    frameLogin = tk.Frame(window)
    frameLogin.place(x=90, y=170)
    dark(frameLogin, 1)
    
    labelT = {}
    labelT['1'] = tk.Label(frameLogin, text="Login",  font=("Noto Sans", 15, "bold"))
    labelT['2'] = tk.Label(frameLogin, text="Username", font=("Noto Sans", 8))
    labelT['3'] = tk.Label(frameLogin, text="Password", font=("Noto Sans", 8))
    labelT['1'].grid(row=0, column=0, pady=10)
    labelT['2'].grid(row=1, column=0, sticky="W")
    labelT['3'].grid(row=3, column=0, sticky="W")
    
    for i in labelT:
        dark(labelT[i])
    
    login = {'user': "", 'password': "", 'showHide': "", 'masuk': ""}
    login['user'] = tk.Entry(frameLogin, width=25) 
    login['password'] = tk.Entry(frameLogin, show="*", width=25)
    login['showHide'] = tk.Button(frameLogin, text="𓁹", font=("default", 6), command=lambda: showHidePassword(login['password']))
    login['masuk'] = tk.Button(frameLogin, text="Login", font=("Noto Sans", 9,"bold"), command=lambda: checkLogin(login['user'], login['password'], frameLogin))
    login['user'].grid(row=2, column=0, pady=5)
    login['password'].grid(row=4, column=0, pady=3)
    login['showHide'].grid(row=4, column=1, pady=3, padx=5)
    login['masuk'].grid(row=5, column=0, pady=22)
    
    for j in login:
        dark(login[j], 3)

window = tk.Tk()
window.title("ATM")
window.minsize(400, 600)
window.maxsize(400, 600)
dark(window, 1)

Utama()

window.mainloop()
