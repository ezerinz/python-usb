import mysql.connector as sql

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
cursor.execute("SHOW TABLES LIKE 'data'")
if not cursor.fetchall():
    cursor.execute("CREATE TABLE data(nim VARCHAR(8) PRIMARY KEY, nama VARCHAR(255), kelas VARCHAR(255) )")
def tampil(lst):
    for i in lst:
        print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
while True:
    print("""1. Tampilkan
2. Ubah
3. Buat
4. Hapus
5. Berhenti""")
    pilihan = int(input("Masukkan Pilihan: "))

    cursor.execute("SELECT * FROM data")
    lst = cursor.fetchall()

    if pilihan == 1:
        print()
        tampil(lst)
    elif pilihan == 2:
        inputNim = input("Masukkan NIM dari data yang akan diubah: ")
        perintah = f"SELECT nim FROM data WHERE nim='{inputNim}'"
        cursor.execute(perintah)
        getNim = cursor.fetchone()

        if getNim:
            nim = input("Masukkan NIM baru: ")
            nama = input("Masukkan Nama baru: ")
            kelas = input("Masukkan Kelas Baru: ")

            perintah1 = f"UPDATE data SET nim='{nim}' WHERE nim='{inputNim}'"
            perintah2 = f"UPDATE data SET nama='{nama}' WHERE nim='{nim}'"
            perintah3 = f"UPDATE data SET kelas='{kelas}' WHERE nim='{nim}'"
            cursor.execute(perintah1)
            cursor.execute(perintah2)
            cursor.execute(perintah3)
            db.commit()
            print("Data diupdate!")
        else:
            print("NIM tidak ditemukan!")
    elif pilihan == 3:
        nim = input("Masukkan NIM: ")
        perintah = f"SELECT nim FROM data WHERE nim='{nim}'"
        cursor.execute(perintah)
        ya = cursor.fetchone() 
        if ya:
            print("NIM sudah ada!")
        else:
            nama = input("Masukkan Nama: ")
            kelas = input("Masukkan Kelas: ")

            perintah2 = f"INSERT INTO data VALUES('{nim}', '{nama}', '{kelas}')"
            cursor.execute(perintah2)
            db.commit()
            print("Data ditambahkan!")
    elif pilihan == 4:
        nim = input("Masukkan NIM dari baris yang akan dihapus: ")
        perintah = f"SELECT nim FROM data WHERE nim='{nim}'"
        cursor.execute(perintah)
        ya = cursor.fetchone() 
        if ya:
            perintah = f"DELETE FROM data WHERE nim='{nim}'"
            cursor.execute(perintah)
            db.commit()
            print("Data dihapus!")
        else:
            print("NIM tidak ditemukan!")
    elif pilihan == 5:
        break


