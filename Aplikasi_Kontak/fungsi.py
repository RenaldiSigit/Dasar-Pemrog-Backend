import time

def tampil_kontak(list_kontak):
    for kontak in list_kontak:
        print("========================")
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"Telp : {kontak['telepon']}\n")

def new_kontak():
    nama = input("Nama : ")
    email = input("Email : ")
    telepon = input("Telepon : ")
    kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    return kontak

def del_kontak(list_kontak):
    telepon = input("No Telepon yang akan di hapus : ")

    index = -1

    for i in range(0,len(list_kontak)):
        kontak = list_kontak[i]
        if telepon == kontak["telepon"]:
            index = i
            break

    if index == -1:
        time.sleep(1)
        print("Data Tidak ada\n")
    else:
        del list_kontak[index]
        time.sleep(1)
        print("Kontak Berhasil di hapus\n")

def find_kontak(list_kontak):
    find_nama = input("Nama kontak yang di cari : ")
    time.sleep(1)
    
    for kontak in list_kontak:
        nama = kontak["nama"]
        if nama.lower().find(find_nama.lower()) != -1:
            print("========================")
            print(f"Nama : {kontak['nama']}")
            print(f"Email : {kontak['email']}")
            print(f"Telp : {kontak['telepon']}")