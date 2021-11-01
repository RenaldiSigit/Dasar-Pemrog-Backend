list_Crypto = ['COIN', 'NFT', 'Exchange']
list_Coin = ['Bitcoin', 'BNB', 'Ethereum', 'USDT']
list_Nft = ['Axie Infinity', 'Theta', 'Decentraland', 'Flow (Dapper Labs)']
list_exchange = ['Binance', 'Indodax', 'Toko Crypto', 'Coin base Exchange']

keranjang = []

while True:
    print('==== list Crypto ====')
    for item in range(0, len(list_Crypto)):
        print(f'{item + 1}. {list_Crypto[item]} ')
    crypto = input('Silahkan Pilih menu 1-3 : \n')
    if crypto == '1':
        for item_crypto in range(0, len(list_Coin)):
            print(f'{item_crypto + 1}. {list_Coin[item_crypto]} ')
        ulang = True
        while ulang:
            select_coin = int(
                input(f'Silahkan Pilih Coin 1-{len(list_Coin)} '))
            if select_coin <= 0 or select_coin > len(list_Coin):
                print('silahkan masukan menu dengan benar')
                for item_crypto in range(0, len(list_Coin)):
                    print(f'{item_crypto + 1}. {list_Coin[item_crypto]} ')
                continue
            else:
                keranjang.append(list_Coin[select_coin - 1])
                print('==== list Coin ====')
                for list_keranjang in range(0, len(keranjang)):
                    print(f'{list_keranjang +1} . {keranjang[list_keranjang]}')
                ulang = False
            continue
    elif crypto == '2':
        for item_crypto2 in range(0, len(list_Nft)):
            print(f'{item_crypto2 + 1}. {list_Nft[item_crypto2]} ')
        ulang = True
        while ulang:
            select_coin = int(
                input(f'Silahkan Pilih NFT 1-{len(list_Nft)} '))
            if select_coin <= 0 or select_coin > len(list_Nft):
                print('silahkan masukan menu dengan benar')
                for item_crypto2 in range(0, len(list_Nft)):
                    print(
                        f'{item_crypto2 + 1}. {list_Nft[item_crypto2]} ')
            else:
                keranjang.append(list_Nft[select_coin - 1])
                print('==== list Crypto ====')
                for list_keranjang in range(0, len(keranjang)):
                    print(f'{list_keranjang +1} . {keranjang[list_keranjang]}')
                    ulang = False
                continue
    elif crypto == '3':
        for item_crypto3 in range(0, len(list_exchange)):
            print(f'{item_crypto3 + 1}. {list_exchange[item_crypto3]} ')
        ulang = True
        while ulang:
            select_coin = int(
                input(f'Silahkan Pilih Exchange 1-{len(list_exchange)} '))
            if select_coin <= 0 or select_coin > len(list_exchange):
                print('silahkan masukan menu dengan benar')
                for item_crypto3 in range(0, len(list_exchange)):
                    print(
                        f'{item_crypto3 + 1}. {list_exchange[item_crypto3]} ')
            else:
                keranjang.append(list_exchange[select_coin - 1])
                print('==== list Crypto ====')
                for list_keranjang in range(0, len(keranjang)):
                    print(f'{list_keranjang +1} . {keranjang[list_keranjang]}')
                    ulang = False
            continue
    else:
        print('Menu tidak ditemukan')
        continue
    pilih = input('Apakah anda ingin memilih lagi ?  y/n \n')
    if pilih == 'y' or pilih == 'Y':
        continue
    else:
        print('==== list Item yang anda pesan ====')
        for list_keranjang in range(0, len(keranjang)):
            print(f'{list_keranjang +1} . {keranjang[list_keranjang]}')
        break
