import fungsi

list_kontak = []

while True:
    print("========================")
    print("----------MENU----------")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar ")
    print("========================")

    menu = input("Pilih Menu : ")

    if menu == "0":
        break
    elif menu == "1":
        fungsi.tampil_kontak(list_kontak)
    elif menu == "2":
        kontak = fungsi.new_kontak()
        list_kontak.append(kontak)
    elif menu == "3":
        fungsi.del_kontak(list_kontak)
    elif menu == "4":
        fungsi.find_kontak(list_kontak)
    else:
        print("Menu tidak ditemukan")

print("Terima kasih sudah menggunakan Program kami")
