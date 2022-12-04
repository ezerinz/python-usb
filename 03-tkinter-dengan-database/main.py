import sqlite3 as sql
import tkinter as tk
import tkinter.messagebox as mb

"""
BAGIAN SQL
"""
def checkLogin(u, p, f):
    con = sql.connect("data.db")
    cur = con.cursor()
    #check table
    checkTable = cur.execute("SELECT name FROM sqlite_master WHERE name='dataUser'")
    
    if checkTable.fetchone() is None:
        cur.execute("CREATE TABLE dataUser(noid INTEGER PRIMARY KEY, nama varchar, umur int, alamat varchar, username varchar, password varchar, saldo varchar)")
    
    username = u.get() 
    password = p.get() #no encrypt/decrypt

    statement = f"SELECT nama, noid FROM dataUser WHERE username='{username}' AND password='{password}';"
    eks = cur.execute(statement)
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

    con.close()
"""
BAGIAN SQL
"""

""" ============================================ """

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
    frame['background'] = '#191920'
    frame.place(x=95, y=170)
 
    frameKembali = tk.Frame(window)
    frameKembali.place(x=10, y=10)
  
    frameLagi=tk.Frame(frame)
    frameLagi['background'] = '#191920'
    frameLagi.grid(row=2, column=1)

    kembali = tk.Button(frameKembali, text="Kembali", font=("Noto Sans", 9, "bold"), command=lambda: backtoMenu(frame, frameLagi, frameKembali))
    kembali['background'] = "#282c34"
    kembali['foreground'] = "#ffffff"
    kembali['highlightbackground'] = "#282a34"
    kembali['relief'] = "flat"
    kembali.grid()

    text1 = tk.Label(frame, text="Tarik Tunai", fg='#ffffff',  font=("Noto Sans", 15, "bold"))
    text1['background'] = '#191920'
    text1.grid(row=0, columnspan=2, pady=10)
    
    rbutton = [*range(4)]
    terpilih = tk.StringVar()
    terpilih.set(None)

    rbutton[0] = tk.Radiobutton(frame, font=("Noto Sans", 10, "bold"),text="Rp50000", variable=terpilih, value=1, command=lambda: terpilih.get())
    rbutton[1] = tk.Radiobutton(frame, font=("Noto Sans", 10, "bold"),text="Rp100000", variable=terpilih, value=2, command=lambda: terpilih.get())

    for i in range(2):
        rbutton[i].grid(row=i+1, column=0, padx=7, sticky="W") 
        rbutton[i]['background'] = "#191920"
        rbutton[i]['foreground'] = "#ffffff"
        rbutton[i]['highlightbackground'] = "#191920"
        rbutton[i]['selectcolor'] = "#282c34"
        rbutton[i]['relief'] = "flat"
 
    rbutton[2] = tk.Radiobutton(frame, font=("Noto Sans", 10, "bold"),text="Rp200000", variable=terpilih, value=3, command=lambda: terpilih.get())    
  
    rbutton[2].grid(row=1, column=1, sticky="W") 
    rbutton[2]['background'] = "#191920"
    rbutton[2]['foreground'] = "#ffffff"
    rbutton[2]['highlightbackground'] = "#191920"
    rbutton[2]['selectcolor'] = "#282c34"
    rbutton[2]['relief'] = "flat"
    
    rbutton[3] = tk.Radiobutton(frameLagi, font=("Noto Sans", 10, "bold"), variable=terpilih, value=4, command=lambda: terpilih.get())
    rbutton[3].grid(row=0, column=0)
    ent = tk.Entry(frameLagi, width=8)
    ent['background'] = "#282a34"
    ent['foreground'] = "#ffffff"
    ent['highlightbackground'] = "#282a34"
    ent['relief'] = "flat"
    ent.grid(row=0, column=1)
     
    rbutton[3]['background'] = "#191920"
    rbutton[3]['foreground'] = "#ffffff"
    rbutton[3]['highlightbackground'] = "#191920"
    rbutton[3]['selectcolor'] = "#282c34"
    rbutton[3]['relief'] = "flat"
    
    konfirm = tk.Button(frame, text="Konfirmasi", font=("Noto Sans", 10, "bold"), command=lambda: tarik(terpilih.get(), ent, frame, frameKembali, frameLagi))
    konfirm['background'] = "#282c34"
    konfirm['foreground'] = "#ffffff"
    konfirm['highlightbackground'] = "#282a34"
    konfirm['relief'] = "flat"
    konfirm.grid(row=3, columnspan=2, pady=20)

def getSaldo():
    con = sql.connect("data.db")
    cur = con.cursor()

    eks = cur.execute(f"SELECT saldo FROM dataUser WHERE noid='{noID}'")
    tangkap = eks.fetchone()
    con.close()
    return tangkap[0]

def tarik(z, y, f1, f2, f3):
    jumlah=0
    z = int(z)
    if z == 1:
        jumlah = 50000
    elif z == 2:
        jumlah = 100000
    elif z == 3:
        jumlah = 200000
    elif z == 4:
        jumlah = float(y.get())
    
    over = False
    
    sld = float(getSaldo())
    if jumlah > sld:
        over = True

    if not over:
        sisa = sld - jumlah
        sisa = str(sisa)
        con = sql.connect("data.db")
        cur = con.cursor()
    
        e = cur.execute(f"UPDATE dataUser SET saldo = '{sisa}' WHERE noid='{str(noID)}'")
        con.commit()

        check = cur.execute(f"SELECT saldo FROM dataUser WHERE noid='{str(noID)}'")
        fetch = check.fetchone()

        if fetch[0] == sisa:
            mb.showinfo("", "Berhasil!")
            backtoMenu(f1, f2, f3)
    else:
        mb.showwarning("","Saldo Tidak Cukup!")

def SetorTunai():
    frame = tk.Frame(window)
    frame['background'] = '#191920'
    frame.place(x=95, y=170)
  
    frameKembali = tk.Frame(window)
    frameKembali.place(x=10, y=10)
  
    kembali = tk.Button(frameKembali, text="Kembali", font=("Noto Sans", 9, "bold"), command=lambda: backtoMenu(frame, frame, frameKembali))
    kembali['background'] = "#282c34"
    kembali['foreground'] = "#ffffff"
    kembali['highlightbackground'] = "#282a34"
    kembali['relief'] = "flat"
    kembali.grid()


    text1 = tk.Label(frame, text="Setor Tunai", fg='#ffffff',  font=("Noto Sans", 15, "bold"))
    text1['background'] = '#191920'
    text1.grid(row=0, columnspan=2, pady=10)

    text2 = tk.Label(frame, text="Masukkan Jumlah", fg='#ffffff', font=("Noto Sans", 10, "bold"))
    text2['background'] = '#191920'
    text2.grid(row=1, columnspan=2)

    text3 = tk.Label(frame, text="Rp", fg='#ffffff', font=("Noto Sans", 10, "bold"))
    text3['background'] = '#191920'
    text3.grid(row=2, column=0)

    ent = tk.Entry(frame)
    ent['background'] = "#282c34"
    ent['foreground'] = "#ffffff"
    ent['highlightbackground'] = "#282a34"
    ent['relief'] = "flat"
    ent.grid(row=2, column=1)

 
    konfirm = tk.Button(frame, text="Konfirmasi", font=("Noto Sans", 10, "bold"), command=lambda: setor(ent, frame, frameKembali))
    konfirm['background'] = "#282c34"
    konfirm['foreground'] = "#ffffff"
    konfirm['highlightbackground'] = "#282a34"
    konfirm['relief'] = "flat"
    konfirm.grid(row=3, columnspan=2, pady=20)

def setor(x, y, z):    
    tambah = x.get()
    if tambah == "":
        mb.showwarning("", "Masukkan Jumlah!")
    else:
        saldo = float(getSaldo())
        tambah = float(tambah)
        con = sql.connect("data.db")
        cur = con.cursor()
    
        jumlah = saldo + tambah
        jumlah = str(jumlah)
        e = cur.execute(f"UPDATE dataUser SET saldo = '{jumlah}' WHERE noid='{str(noID)}'")
        con.commit()

        check = cur.execute(f"SELECT saldo FROM dataUser WHERE noid='{str(noID)}'")
        fetch = check.fetchone()

        if fetch[0] == jumlah:
            mb.showinfo("", "Berhasil!")
            backtoMenu(y, y, z)
        else:
            mb.showwarning("", "Terjadi Masalah")

    
def GantiPin():
    frame = tk.Frame(window)
    frame['background'] = '#191920'
    frame.place(x=65, y=170)
  
    frameKembali = tk.Frame(window)
    frameKembali.place(x=10, y=10)
  
    kembali = tk.Button(frameKembali, text="Kembali", font=("Noto Sans", 9, "bold"), command=lambda: backtoMenu(frame, frame, frameKembali))
    kembali['background'] = "#282c34"
    kembali['foreground'] = "#ffffff"
    kembali['highlightbackground'] = "#282a34"
    kembali['relief'] = "flat"
    kembali.grid()


    text1 = tk.Label(frame, text="Ganti Pin", fg='#ffffff',  font=("Noto Sans", 15, "bold"))
    text1['background'] = '#191920'
    text1.grid(row=0, columnspan=3, pady=10)
 
    text2 = tk.Label(frame, text="Pin Lama", fg='#ffffff', font=("Noto Sans", 10, "bold"))
    text2['background'] = '#191920'
    text2.grid(row=1, column=0)


    text3 = tk.Label(frame, text="Pin Baru", fg='#ffffff', font=("Noto Sans", 10, "bold"))
    text3['background'] = '#191920'
    text3.grid(row=2, column=0, pady=8)

    ent = tk.Entry(frame, show="*")
    ent['background'] = "#282c34"
    ent['foreground'] = "#ffffff"
    ent['highlightbackground'] = "#282a34"
    ent['relief'] = "flat"
    ent.grid(row=1, column=1)

 
    ent2 = tk.Entry(frame, show="*")
    ent2['background'] = "#282c34"
    ent2['foreground'] = "#ffffff"
    ent2['highlightbackground'] = "#282a34"
    ent2['relief'] = "flat"
    ent2.grid(row=2, column=1)

    showHide1 = tk.Button(frame, text="𓁹", font=("default", 6), command=lambda: showHidePassword(ent))
    showHide1.grid(row=1, column=2, pady=3, padx=5)
    showHide1['background'] = "#282a34"
    showHide1['foreground'] = "#ffffff"
    showHide1['highlightbackground'] = "#282a34"
    showHide1['relief'] = "flat"


    showHide2 = tk.Button(frame, text="𓁹", font=("default", 6), command=lambda: showHidePassword(ent2))
    showHide2.grid(row=2, column=2, pady=3, padx=5)
    showHide2['background'] = "#282a34"
    showHide2['foreground'] = "#ffffff"
    showHide2['highlightbackground'] = "#282a34"
    showHide2['relief'] = "flat"





    konfirm = tk.Button(frame, text="Konfirmasi", font=("Noto Sans", 10, "bold"), command=lambda: pin(ent, ent2, frame, frameKembali))
    konfirm['background'] = "#282c34"
    konfirm['foreground'] = "#ffffff"
    konfirm['highlightbackground'] = "#282a34"
    konfirm['relief'] = "flat"
    konfirm.grid(row=3, columnspan=3, pady=20)

def pin(x, y, z, w):
    con = sql.connect("data.db")
    cur = con.cursor()
    
    check = cur.execute(f"SELECT password FROM dataUser WHERE noid='{str(noID)}'")
    fetch = check.fetchone()[0]
    
    oldPin = x.get()
    newPin = y.get()
    if oldPin == fetch:
        if len(newPin) != 6:
            mb.showwarning("", "Pin Harus 6 Karakter!")
        else:
            e = cur.execute(f"UPDATE dataUser SET password = '{newPin}' WHERE noid='{str(noID)}'")
            con.commit()

            check = cur.execute(f"SELECT password FROM dataUser WHERE noid='{str(noID)}'")
            fetch = check.fetchone()

            if fetch[0] == newPin:
                mb.showinfo("", "Berhasil!")
                logOut(z, w)
    else:
        mb.showwarning("", "Pin Salah!")

    con.close()

 
def logOut(frame, frame2):
    frame.destroy()
    frame2.destroy()
    Utama()

def Menu():
    frameMenu = tk.Frame(window)
    frameMenu['background'] = '#191920'
    frameMenu.place(x=125, y=170)
    
    text1 = tk.Label(frameMenu, text="Selamat Datang, "+loginName+"!", fg='#ffffff',  font=("Noto Sans", 10, "bold"))
    text1['background'] = '#191920'
    text1.pack()
    
    getS = getSaldo()
    text2 = tk.Label(frameMenu, text="Saldo Anda: Rp"+getS, fg='#ffffff',  font=("Noto Sans", 10, "bold"))
    text2['background'] = '#191920'
    text2.pack()
 
    frameLogout = tk.Frame(window)
    frameLogout.place(x=10, y=10)
     
    btn = [*range(3)]
    btn[0] = tk.Button(frameMenu, text="Tarik Tunai", font=("Noto Sans", 10, "bold"), width=15, command=lambda: pindah(frameMenu, frameLogout, 1))

    btn[1] = tk.Button(frameMenu, text="Setor Tunai", font=("Noto Sans", 10, "bold"), width=15, command=lambda: pindah(frameMenu, frameLogout, 2))
    btn[2] = tk.Button(frameMenu, text="Ganti Pin", font=("Noto Sans", 10, "bold"), width=15, command=lambda: pindah(frameMenu, frameLogout, 3))

    for i in range(len(btn)):
        btn[i].pack(pady=5)
        btn[i]['background'] = "#282a34"
        btn[i]['foreground'] = "#ffffff"
        btn[i]['highlightbackground'] = "#282a34"
        btn[i]['relief'] = "flat"

    logOutB = tk.Button(frameLogout, text="Logout", font=("Noto Sans", 9, "bold"), command=lambda: logOut(frameMenu, frameLogout))
    logOutB['background'] = "#282c34"
    logOutB['foreground'] = "#ffffff"
    logOutB['highlightbackground'] = "#282a34"
    logOutB['relief'] = "flat"
    logOutB.grid()

def showHidePassword(entryPw):
    if entryPw.cget('show') == '':
        entryPw.config(show="*")
    else:
        entryPw.config(show="")

def Utama():
    frameLogin = tk.Frame(window)
    frameLogin['background'] = '#191920'
    frameLogin.place(x=90, y=170)

    text1 = tk.Label(frameLogin, text="Login", fg='#ffffff',  font=("Noto Sans", 15, "bold"))
    text1['background'] = '#191920'
    text1.grid(row=0, column=0, pady=10)
    
    login = {'user': "", 'password': "", 'showHide': "", 'masuk': ""}
    
    text1 = tk.Label(frameLogin, text="Username", fg='#ffffff', font=("Noto Sans", 8))
    text1['background'] = '#191920'
    text1.grid(row=1, column=0, sticky="W")
    login['user'] = tk.Entry(frameLogin, width=25)
    login['user'].grid(row=2, column=0, pady=5)
    
    text2 = tk.Label(frameLogin, text="Password", fg='#ffffff', font=("Noto Sans", 8))
    text2['background'] = '#191920'
    text2.grid(row=3, column=0, sticky="W")
  
    login['password'] = tk.Entry(frameLogin, show="*", width=25)
    login['password'].grid(row=4, column=0, pady=3)
    
    login['showHide'] = tk.Button(frameLogin, text="𓁹", font=("default", 6), command=lambda: showHidePassword(login['password']))
    login['showHide'].grid(row=4, column=1, pady=3, padx=5)

    login['masuk'] = tk.Button(frameLogin, text="Login", font=("Noto Sans", 9,"bold"), command=lambda: checkLogin(login['user'], login['password'], frameLogin))
    login['masuk'].grid(row=5, column=0, pady=22)

    for i in login:
        login[i]['background'] = "#282a34"
        login[i]['foreground'] = "#ffffff"
        login[i]['highlightbackground'] = "#282a34"
        login[i]['relief'] = "flat"

window = tk.Tk()
window.title("Daftar")
window.minsize(400, 600)
window.maxsize(400, 600)
window['background'] = '#181920'

Utama()

window.mainloop()
