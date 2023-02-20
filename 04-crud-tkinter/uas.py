import mysql.connector as sql

namaDb = "mkpython"
namaTable = "nilai"

#buat database
mydb = sql.connect(host="localhost", user="root", password="")
cmd = f"CREATE DATABASE IF NOT EXISTS {namaDb}"
mydb.cursor().execute(cmd)
mydb.close()

#connect to database dan buat table
db = sql.connect(host="localhost", user="root", password="", database=namaDb)
cursor = db.cursor()
cmd2 = f"SHOW TABLES LIKE '{namaTable}'"
cursor.execute(cmd2)

if not cursor.fetchall():
    cmd3 = f"CREATE TABLE {namaTable}(nim VARCHAR(8) PRIMARY KEY, nama VARCHAR(255), alamat VARCHAR(255), nilai INT)"
    cursor.execute(cmd3)

# insert
"""
tambah = [('D0221371', 'Edwin', 'Mekkatta', 87),
          ('D0221111', 'Amelia', 'Patoke', 95),
          ('D0221303', 'Ryan', 'Mamuju', 98),
          ('D0221375', 'Haikal', 'Tubo', 75),
          ('D0221376', 'Efortuntrio', 'Mamasa', 89)]
cmd4 = "INSERT INTO nilai VALUES(%s, %s, %s, %s)" 
cursor.executemany(cmd4, tambah)
db.commit()
"""
#insert

#tampilkan
"""
cmd5 = f"SELECT * from {namaTable}"
cursor.execute(cmd5)
for i in cursor.fetchall():
    print(i)
"""
#tampilkan

#delete
nimHapus = 'D0221111'
cmd6 = f"DELETE FROM {namaTable} WHERE nim='{nimHapus}'"
cursor.execute(cmd6)
db.commit()

#update
"""
nimUpdate = 'D0221111'
kolom = 'alamat'
dataBaru = 'Mamuju'
cmd7 = f"UPDATE {namaTable} SET {kolom}='{dataBaru}' WHERE nim='{nimUpdate}'"
cursor.execute(cmd7)
db.commit()
"""


#while True:
#    print("""1. Tambah
#2. Update
#3. Delete
#4. Berhenti""")
"""    pilih = int(input("=> "))
    if pilih == 1:
        dta = []
        input = []
        while True:
            nim = input("Masukkan NIM: ")
            input.append(nim)
            nama = input("Masukkan Nama: ")
            input.append(nama)
            alamat = input("Masukkan Alamat: ")
            input.append(alamat)
            nilai = int(input("Masukkan Nilai: "))
            input.append(nilai)

            data.append(tuple(input))
            ulang = input("Masih ingin menginput? (y/n): ").lower()
            if ulang == "n":
                break
        cmd = "INSERT INTO nilai VALUES(%s, %s, %s, %s)" 
        cursor.executemany(cmd4, dta)
        db.commit()
    if pilih == 2:
        nim = input("Masukkan Nim: ")
        cmd = f"SELECT nim FROM {namaTable} WHERE
"""
