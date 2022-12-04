import sqlite3 as sql
import tkinter as tk

"""
BAGIAN SQL
"""
def checkLogin(u, p, f):
    con = sql.connect("data.db")
    cur = con.cursor()

    #check table
    checkTable = cur.execute("SELECT name FROM sqlite_master WHERE name='dataAdmin'")

    if checkTable.fetchone() is None:
        cur.execute("CREATE TABLE dataAdmin(noid INTEGER PRIMARY KEY, user varchar, pw varchar)")

    username = u.get() 
    password = p.get() #no encrypt

    statement = f"SELECT user FROM dataAdmin WHERE user='{username}' AND pw ='{password}';"
    cur.execute(statement)

    if not cur.fetchone():
        tulis = tk.Label(f, text="Password atau Username Salah", font=("Noto Sans", 8, "bold"))
        tulis['background'] = "#191920"
        tulis['foreground'] = "#D0342C"
        tulis.place(x=0, y=155)
    else:
        loginSucces(f)

    con.close()

def addData(ent, text):
    con = sql.connect("data.db")
    cur = con.cursor()
    #check table
    checkTable = cur.execute("SELECT name FROM sqlite_master WHERE name='dataUser'")
    
    if checkTable.fetchone() is None:
        cur.execute("CREATE TABLE dataUser(noid INTEGER PRIMARY KEY, nama varchar, umur int, alamat varchar, username varchar, password varchar, saldo varchar)")
    
    #get
    nama = str(ent[0].get())
    umur = int(ent[1].get())
    username = str(ent[2].get())
    alamat = str(ent[3].get())

    dataToAdd = (nama, umur, username, alamat, '123456', "200000")

    #chek user dan kosong
    userSudahAda = False
    adaKosong = False
    for u in cur.execute("SELECT username FROM dataUser"):
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
        text.config(text="Data Berhasil ditambah! Password: 123456")
        cur.execute("INSERT INTO dataUser(nama, umur, username, alamat, password, saldo) VALUES (?, ?, ?, ?, ?, ?)", dataToAdd)
        con.commit()
    con.close()

"""
BAGIAN SQL
"""

""" ============================================ """

def loginSucces(frame):
    frame.destroy()
    FormDaftar()
   
def logOut(frame, frame2):
    frame.destroy()
    frame2.destroy()
    Utama()

def FormDaftar():
    frameDaftar = tk.Frame(window)
    frameDaftar['background'] = '#191920'
    frameDaftar.place(x=90, y=170)
    
    text1 = tk.Label(frameDaftar, text="Form Pendaftaran", fg='#ffffff',  font=("Noto Sans", 15, "bold"))
    text1['background'] = '#191920'
    text1.grid(row=0, columnspan=2, pady=5)

    data = {}
    entry = [*range(1,5)]
    
    for i in range(len(entry)):
        entry[i] = tk.Entry(frameDaftar, width=20)
        if i == 1:
            entry[i] = tk.Spinbox(frameDaftar, from_=12, to=70, width=18)
        entry[i].grid(row=i+1, column=1, pady=5, padx=5)

        entry[i]['background'] = "#282a34"
        entry[i]['foreground'] = "#ffffff"
        entry[i]['highlightbackground'] = "#282a34"
        entry[i]['relief'] = "flat"

    data['nama'] = tk.Label(frameDaftar, text="Nama")
    data['nama'].grid(row=1, column=0, sticky="W")

    data['umur'] = tk.Label(frameDaftar, text="Umur")
    data['umur'].grid(row=2, column=0, sticky="W")

    data['username'] = tk.Label(frameDaftar, text="Username")
    data['username'].grid(row=3, column=0, sticky="W")
    
    data['alamat'] = tk.Label(frameDaftar, text="Alamat")
    data['alamat'].grid(row=4, column=0, sticky="W")

    for z in data:
        data[z]['background'] = '#191920'
        data[z]['foreground'] = '#ffffff'

    text = tk.Label(frameDaftar, text="", font=("Noto Sans", 8, "bold")) 
    text['background'] = "#191920"
    text['foreground'] = "#D0342C"
    text.place(x=0, y=175)
 
    daftarB = tk.Button(frameDaftar, text="Daftar", font=("Noto Sans", 9, "bold"), command=lambda: addData(entry, text))
    daftarB.grid(row=5, columnspan=2, pady=25)
    daftarB['background'] = "#282c34"
    daftarB['foreground'] = "#ffffff"
    daftarB['highlightbackground'] = "#282a34"
    daftarB['relief'] = "flat"

    frameLogout = tk.Frame(window)
    frameLogout.place(x=10, y=10)
    
    logOutB = tk.Button(frameLogout, text="Logout", font=("Noto Sans", 9, "bold"), command=lambda: logOut(frameDaftar, frameLogout))
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

    text1 = tk.Label(frameLogin, text="Login Admin", fg='#ffffff',  font=("Noto Sans", 15, "bold"))
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

#con = sql.connect("data.db")
#cur = con.cursor()

#userbaru = "edwin"
#id = "1"
#z = cur.execute(f"UPDATE dataAdmin SET user='{userbaru}' WHERE noid='{id}'")
#con.commit()
#y = z.fetchon e()

#print(y)

window.mainloop()
