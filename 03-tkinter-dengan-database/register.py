import sqlite3 as sql
import tkinter as tk

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
    checkTable = db.cur.execute("SELECT name FROM sqlite_master WHERE name='dataAdmin'")

    if checkTable.fetchone() is None:
        db.cur.execute("CREATE TABLE dataAdmin(noid INTEGER PRIMARY KEY, user varchar, pw varchar)")
    
    #mff :(((((
    check = db.cur.execute("SELECT user FROM dataAdmin WHERE user='admin'")
    if check.fetchone() is None:
        db.cur.execute("INSERT INTO dataAdmin(user, pw) VALUES('admin', 'admin')")
        db.con.commit()

    username = u.get().lower()
    password = p.get() #no encrypt

    statement = f"SELECT user FROM dataAdmin WHERE user='{username}' AND pw ='{password}';"
    db.cur.execute(statement)

    if not db.cur.fetchone():
        tulis = tk.Label(f, text="Password atau Username Salah", font=("Noto Sans", 8, "bold"))
        dark(tulis, 2)
        tulis.place(x=0, y=155)
    else:
        loginSucces(f)

    db.close()

def addData(ent, text):
    db = Database("data.db")
    
    #check table
    checkTable = db.cur.execute("SELECT name FROM sqlite_master WHERE name='dataUser'")
    
    if checkTable.fetchone() is None:
        db.cur.execute("CREATE TABLE dataUser(noid INTEGER PRIMARY KEY, nama varchar, umur int, alamat varchar, username varchar, password varchar, saldo varchar)")
    
    #get
    nama = str(ent[0].get())
    umur = int(ent[1].get())
    username = str(ent[2].get()).lower()
    alamat = str(ent[3].get())

    dataToAdd = (nama, umur, username, alamat, '123456', "200000")

    #check user dan kosong
    userSudahAda = False
    adaKosong = False
    for u in db.cur.execute("SELECT username FROM dataUser"):
        if u[0] == username:
            userSudahAda = True

    for i in range(len(ent)):
        if ent[i].get() == "":
            adaKosong = True
   
    if adaKosong:
        text["text"] = ""
        text.config(text="Isi Semua!")
    elif userSudahAda:
        text["text"] = ""
        text.config(text="Username Sudah Dipakai!")
    else:
        text["text"] = ""
        text.config(text="Data Berhasil ditambah! Password: 123456", font=("Noto Sans", 7, "bold"))
        db.cur.execute("INSERT INTO dataUser(nama, umur, username, alamat, password, saldo) VALUES (?, ?, ?, ?, ?, ?)", dataToAdd)
        db.con.commit()
    db.close()

""" ======================= SQL ======================== """


""" ==================================================== """
def loginSucces(frame):
    frame.destroy()
    FormDaftar()
   
def logOut(frame, frame2):
    frame.destroy()
    frame2.destroy()
    Utama()

def FormDaftar():
    frameDaftar = tk.Frame(window)
    frameDaftar.place(x=90, y=170)
    dark(frameDaftar, 1)
    
    text1 = tk.Label(frameDaftar, text="Form Pendaftaran",  font=("Noto Sans", 15, "bold"))
    text1.grid(row=0, columnspan=2, pady=5)
    dark(text1)

    data = {}
    entry = [*range(1,5)]
    
    for i in range(len(entry)):
        entry[i] = tk.Entry(frameDaftar, width=20)
        if i == 1:
            entry[i] = tk.Spinbox(frameDaftar, from_=12, to=70, width=18)
        entry[i].grid(row=i+1, column=1, pady=5, padx=5)

        dark(entry[i], 3)

    data['nama'] = tk.Label(frameDaftar, text="Nama")
    data['nama'].grid(row=1, column=0, sticky="W")

    data['umur'] = tk.Label(frameDaftar, text="Umur")
    data['umur'].grid(row=2, column=0, sticky="W")

    data['username'] = tk.Label(frameDaftar, text="Username")
    data['username'].grid(row=3, column=0, sticky="W")
    
    data['alamat'] = tk.Label(frameDaftar, text="Alamat")
    data['alamat'].grid(row=4, column=0, sticky="W")

    for z in data:
        dark(data[z])

    text = tk.Label(frameDaftar, text="", font=("Noto Sans", 8, "bold")) 
    text.place(x=0, y=175)
    dark(text, 2)
    
    tombol = {}
    tombol['daftar'] = tk.Button(frameDaftar, text="Daftar", font=("Noto Sans", 9, "bold"), command=lambda: addData(entry, text))
    tombol['daftar'].grid(row=5, columnspan=2, pady=25)

    frameLogout = tk.Frame(window)
    frameLogout.place(x=10, y=10)
    
    tombol['keluar'] = tk.Button(frameLogout, text="Logout", font=("Noto Sans", 9, "bold"), command=lambda: logOut(frameDaftar, frameLogout))
    tombol['keluar'].grid()
    
    for i in tombol:
        dark(tombol[i], 3)

def showHidePassword(entryPw):
    if entryPw.cget('show') == '':
        entryPw.config(show="*")
    else:
        entryPw.config(show="")

def Utama():
    frameLogin = tk.Frame(window)
    frameLogin.place(x=90, y=170)
    dark(frameLogin, 1)

    text1 = tk.Label(frameLogin, text="Login Admin",  font=("Noto Sans", 15, "bold"))
    text1.grid(row=0, column=0, pady=10)
    dark(text1)
    
    loginI = {'user': "", 'password': "", 'showHide': "", 'masuk': ""}
    loginL = {}

    loginL['u'] = tk.Label(frameLogin, text="Username", font=("Noto Sans", 8))
    loginL['u'].grid(row=1, column=0, sticky="W")
    loginL['pw'] = tk.Label(frameLogin, text="Password", font=("Noto Sans", 8))
    loginL['pw'].grid(row=3, column=0, sticky="W")
    
    for i in loginL:
        dark(loginL[i])
 
    loginI['user'] = tk.Entry(frameLogin, width=25)
    loginI['user'].grid(row=2, column=0, pady=5) 
    loginI['password'] = tk.Entry(frameLogin, show="*", width=25)
    loginI['password'].grid(row=4, column=0, pady=3)
    loginI['showHide'] = tk.Button(frameLogin, text="𓁹", font=("default", 6), command=lambda: showHidePassword(loginI['password']))
    loginI['showHide'].grid(row=4, column=1, pady=3, padx=5)
    loginI['masuk'] = tk.Button(frameLogin, text="Login", font=("Noto Sans", 9,"bold"), command=lambda: checkLogin(loginI['user'], loginI['password'], frameLogin))
    loginI['masuk'].grid(row=5, column=0, pady=22)

    for i in loginI:
        dark(loginI[i], 3)

window = tk.Tk()
window.title("Daftar")
window.minsize(400, 600)
window.maxsize(400, 600)
dark(window, 1)

Utama()

#con = sql.connect("data.db")
#cur = con.cursor()

#userbaru = "edwin"
#id = "1"
#z = cur.execute(f"UPDATE dataAdmin SET user='{userbaru}' WHERE noid='{id}'")
#con.commit()
#y = z.fetchone()

#print(y)

window.mainloop()
