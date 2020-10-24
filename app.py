import mysql.connector, time, sys
from sys import platform
from os import system
class Data:
    def __init__(self):
        try:
            self.db=mysql.connector.connect(
                host='gns2nd.ddns.net',
                port=3306,
                user='root2',
                password='root2',
                database="test"
            )
            self.cursor = self.db.cursor()
            if self.db.is_connected:
                print("Berhasil Connect Ke-Server")
                
            print("---Selamat Datang----")
            self.user = input("Masukkan Username Admin: ")
            self.passwd = input("Masukkan Password Admin: ")
            query = "SELECT * FROM admin WHERE username=%s AND passwd=%s"
            value = (self.user,self.passwd)
            self.cursor.execute(query,value)
            hasil = self.cursor.fetchall()
            hasil = len(hasil)
            
            if hasil < 1:
                print("---Username Salah---")
                time.sleep(1)
                Data.check_os()
                Data()
            else:
                Data.check_os()
                print("---Login Berhasil---")
                Data.menu(self)
                
        except KeyboardInterrupt:
            sys.exit("\nTerima Kasih Telah Menggunakan Tools Ini\nExiting")
            time.sleep(1)
            
    #Define checck OS#
    def check_os():
        if platform == 'linux' or platform == 'linux2':
            system('clear')
        elif platform == 'win32':
            system('cls')
        else:
            print("System Tidak Diketahui")
            
    #Define select#
    def read(self):
        Data.check_os()
        print("----Halaman Read Data----")
        query = "SELECT nim,nama,kelas,jurusan FROM mahasiswa"
        self.cursor.execute(query)
        hasil = self.cursor.fetchall()
        
        i = 1
        for x in hasil:
            print("NO: ",i,"\n------------","\nNAMA: "+x[1],"\nNIM: "+x[0],"\nKELAS: "+x[2],"\nJURUSAN: "+x[3],"\n")
            i = i + 1
        input("Tekan Enter Untuk Lanjutkan")
                
        Data.check_os()
        Data.menu(self)
        
    def nim(self):
        nim = int(input("Masukan Nim Mahasiswa: "))
        self.nim = str(nim)
        
    def nama(self):
        nama = input("Masukan Nama Mahasiswa: ")
        self.nama = nama
        
    def kelas(self):
        kelas = input("Masukan Kelas Mahasiswa: ")
        self.kelas = kelas
        
    def jurusan(self):
        jurusan = input("Masukan Jurusan Mahasiswa: ")
        self.jurusan = jurusan
        
    #Define seacrh#
    def search(self):
        Data.check_os()
        print("----Halaman Cari Data----")
        Data.nim(self)
        query = "SELECT nama,nim,kelas,jurusan FROM mahasiswa WHERE nim="
        value = str(self.nim)
        self.cursor.execute(query+value)
        hasil = self.cursor.fetchall()
        hasil2 = len(hasil)
        
        if hasil2 < 1 :
            print ("---Tidak Ada Data---")
            time.sleep(1)
            Data.menu(self)
        else:
            i = 1
            for x in hasil:
                print("----Data Ditemukan----")
                print("NO: ",i,"\n------------","\nNAMA: "+x[1],"\nNIM: "+x[0],"\nKELAS: "+x[2],"\nJURUSAN: "+x[3],"\n")
                i = i + 1
            input("Tekan Enter Untuk Lanjutkan")
            Data.check_os()
            Data.menu(self)
        
    def update(self):
        Data.check_os()
        print("----Halaman Update Data----")
        Data.nim(self)
        query1 = "SELECT nama,nim,kelas,jurusan FROM mahasiswa WHERE nim="
        value1 = str(self.nim)
        self.cursor.execute(query1+value1)
        hasil = self.cursor.fetchall()
        hasil2 = len(hasil)
        
        if self.cursor.rowcount < 1 :
            print("\n")
            print("----Data Tidak Ditemukan----")
            time.sleep(1)
            Data.menu(self)
        for d in hasil:
            print("\n")
            print("----Data Ditemukan----")
            print(" Nama: "+d[0],"\n","NIM: "+d[1],"\n","Kelas: ",d[2],"\n","Jurusan: "+d[3])
            
        print("\n")
        print("Masukkan Nim Anda: "+self.nim)
        Data.nama(self)
        Data.kelas(self)
        Data.jurusan(self)
        query2 = "UPDATE mahasiswa SET nama=%s, kelas=%s, jurusan=%s WHERE nim=%s"
        value2 = (self.nama,self.kelas,self.jurusan,self.nim)
        self.cursor.execute(query2,value2)
        self.db.commit()
        Data.check_os()
        print("----{} Data Berhasil Diubah".format(self.cursor.rowcount),"----\n")
        Data.menu(self)
        
    def delete(self):
        print("----HALAMAN HAPUS DATA----\n","----BERHATI-HATILAH----\n")
        Data.nim(self)
        query = "SELECT nim,nama,kelas,jurusan FROM mahasiswa WHERE nim="
        value = self.nim
        self.cursor.execute(query+value)
        hasil = self.cursor.fetchall()
        for x in hasil:
            Data.check_os()
            print("----DATA YANG INGIN DI HAPUS----")
            print("\n------------","\nNAMA: "+x[1],"\nNIM: "+x[0],"\nKELAS: "+x[2],"\nJURUSAN: "+x[3],"\n")
        tanya = input("Anda Yakin Ingin Menghapusnya? Y/N: ")
        if tanya == 'Y' or tanya == 'y':
            query =  "DELETE FROM mahasiswa WHERE nim=%s"
            value = self.nim
            self.db.commit()
            Data.check_os()
            print("----{} data berhasil dihapus----\n".format(self.cursor.rowcount))
            Data.menu(self)
        elif tanya == 'N' or tanya == 'n':
            Data.check_os()
            print("----DATA TIDAK TERHAPUS----\n")
            Data.menu(self)
    
    def insert(self):
        print("\nTekan CTRL-C Untuk Keluar Dari Halaman Insert Ini")
        print("----Halaman Insert Data----")
        print("\n")
        Data.nim(self)
        check = "SELECT nama, nim, kelas, jurusan FROM mahasiswa WHERE nim="
        nimstr = (self.nim)
        self.cursor.execute(check+nimstr)
        hasil = self.cursor.fetchall()
        hasilstr = len(hasil)
        if hasilstr > 0 :
            for x in hasil:
                Data.check_os()
                print("Data Sudah Ada Dengan :\n")
                print("Nama: "+x[0],"\nNIM: "+x[1],"\nKelas: "+x[2],"\nJurusan: "+x[3])
                print("\nSilahkan Input NIM Dengan Yang Lain\n")
                Data.insert(self)
        else:
            query = "INSERT INTO mahasiswa (nama , nim, kelas, jurusan) VALUES (%s, %s, %s, %s)"
            print("--------------------")
            print("Masukkan NIM: "+nimstr)
            Data.nama(self)
            Data.kelas(self)
            Data.jurusan(self)
            value = (self.nama, self.nim, self.kelas, self.jurusan)
            self.cursor.execute(query,value)
            self.db.commit()
            Data.check_os()
            print("----{} Data Berhasil Disimpan".format(self.cursor.rowcount),"-----\n")
            Data.menu(self)
    #Define menu#
    def menu(self):
        print("---Selamat Datang {}---\n".format(self.user),
              "1. INSERT Data\n",
              "2. READ Data\n",
              "3. UPDATE Data\n",
              "4. DELETE Data\n",
              "5. SEARCH Data\n",
              "Tekan CTRL-C Untuk Keluar Dari Program")
        pil = input("Masukkan Pilihan: ")
        if pil == '1':
            Data.insert(self)
        elif pil == '2':
            Data.read(self)
        elif pil == '3':
            Data.update(self)
        elif pil == '4':
            Data.delete(self)
        elif pil == '5':
            Data.search(self)
        else:
            print("Input Salah")
if __name__ == '__main__':
    while (True):
        Data()