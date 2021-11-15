# Renaldi Sigit Pratama
# 1120101848
# UTS Dasar Pemrograman Backend

import time

profider = ['XL Axiata','Axis','Three','Telkomsel']
pulsa = [5000,10000,25000,50000,100000]
metodeBayar = ['Cash','Dana','OVO','Ngutang dulu']
semua = []

while True:
    print('----------- Jual Pulsa ------------')
    print('----- Silahkan Pilih Provider -----')
    for item in range(0,len(profider)) :
        print(f'{item + 1}.{profider[item]}')
    sc = input('Silahkan Pilih Provider : ')
    no = input("Masukan Nomor anda : ")

    print('----- Silahkan Pilih Nominal Pulsa -----')
    for i in range(0,len(pulsa)) :
        print(f'{i + 1}.{pulsa[i]}')
    jumlah = int(input('Silahkan Pilih Nominal '))
    semua = pulsa[jumlah-1]

    print('-- Silahkan Pilih Metode Pembayaran --')
    for a in range(0,len(metodeBayar)) :
        print(f'{a + 1}.{metodeBayar[a]}')
    metode = int(input('Pilih Metode Pembayaran : '))

    uang = int(input('Masukan Jumlah Uang yang akan anda bayarkan : '))
    if uang < semua :
        print('Maaf Uang anda Tidak Cukup')
    else:
        print(f'No anda : {no}')
        print(f'Metode Pembayaran {metodeBayar[metode]}')
        print('Transaksi Sedang di Proses.... ,\n Silahkan Tunggu Sebentar')
        time.sleep(2)
        print('---- Transaksi Selesai -----')
    
    time.sleep(1)
    repeat = input('Apakah anda ingin bertransaksi lagi ? [y/n]')
    if repeat == 'y' or repeat == "Y":
        continue
    else:
        print('---- Terima kasih Sudah Menggunakan Layanan Kami ----')
        time.sleep(1)
        break