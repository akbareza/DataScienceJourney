#MAIN DICT OF FRUITS
buah = {
    'buah0': {
        'namaBuah' : 'Apel',
        'stokBuah' : 20.0,
        'hargaBuah' : 10000.0
    },
    'buah1': {
        'namaBuah' : 'Jeruk',
        'stokBuah' : 15.0,
        'hargaBuah' : 15000.0
    },
    'buah2': {
        'namaBuah' : 'Anggur',
        'stokBuah' : 25.0,
        'hargaBuah' : 20000.0
    },
}

historiIndexBuah = len(buah)
#print(historiBuah)

while True:
    menu = input('''
    Selamat Datang di Pasar Buah

    List Menu:
    [1] Menampilkan Daftar Buah
    [2] Menambah Buah
    [3] Menghapus Buah
    [4] Membeli Buah
    [5] Exit Program
    Masukkan angka menu yang diinginkan : '''
    )
    print('\n')
    try:
        if menu == '1':
            #SHOWING LIST OF FRUITS
            print('Daftar Buah :')
            print('Index\t|Nama\t\t\t|Stock\t\t|Harga')
            for i,j,k in zip(range(len(buah)),buah.values(),buah):
                if len(j["namaBuah"]) > 6:
                    print(f'{k[4:]}\t|{j["namaBuah"]}\t\t|{j["stokBuah"]}\t\t|{j["hargaBuah"]}') #perlu diotomasi untuk kerapihan bila nama terlalu panjang
                else:
                    print(f'{k[4:]}\t|{j["namaBuah"]}\t\t\t|{j["stokBuah"]}\t\t|{j["hargaBuah"]}') 

        elif menu == '2':
             #ADDING LIST OF FRUITS
            buahTemp = {}
            namaBuah = input('Masukkan nama buah\t: ')
            buahTemp['namaBuah'] = namaBuah
            #print(buahTemp)
            while True:
                try:
                    while True:
                        stokBuah = float(input('Masukkan stok buah\t: '))
                        if stokBuah <= 0:
                            print('Masukkan angka lebih dari 0')
                        else:
                            buahTemp['stokBuah'] = stokBuah
                            break
                    break
                except:
                    print('Masukkan angka!')

            while True:
                try:
                    while True:
                        hargaBuah = float(input('Masukkan harga buah\t: '))
                        if hargaBuah <= 0:
                            print('Masukkan angka lebih dari 0')
                        else:
                            buahTemp['hargaBuah'] = hargaBuah
                            break
                    break
                except:
                    print('Masukkan angka!')
            urutBuah = ('buah'+str(historiIndexBuah))
            historiIndexBuah +=1
            print(urutBuah)
            buah[urutBuah] = buahTemp
            #print(buah)
        
        elif menu == '3':
            #DELETE ITEM IN LIST OF FRUITS
            indexListBuah = []
            for m in buah:
                indexListBuah.append(m[4:])
            #print('ini index buah :', indexListBuah)
            jumlahJenisBuah = len(buah)
            print(jumlahJenisBuah)
            print('\nDaftar Buah :')
            print('Index\t|Nama\t\t\t|Stock\t\t|Harga')
            for i,j,k in zip(range(len(buah)),buah.values(),buah):
                if len(j["namaBuah"]) > 6:
                    print(f'{k[4:]}\t|{j["namaBuah"]}\t\t|{j["stokBuah"]}\t\t|{j["hargaBuah"]}') #perlu diotomasi untuk kerapihan bila nama terlalu panjang
                else:
                    print(f'{k[4:]}\t|{j["namaBuah"]}\t\t\t|{j["stokBuah"]}\t\t|{j["hargaBuah"]}') 
            
            while True:
                try:
                    delBuah = int(input('Masukkan nomor index buah yang ingin dihapus: '))
                    if str(delBuah) in indexListBuah:
                        delBuah = ('buah'+str(delBuah))
                        del buah[delBuah]
                        print('Daftar Buah :')
                        print('Index\t|Nama\t\t\t|Stock\t\t|Harga')
                        for i,j,k in zip(range(len(buah)),buah.values(),buah):
                            if len(j["namaBuah"]) > 6:
                                print(f'{k[4:]}\t|{j["namaBuah"]}\t\t|{j["stokBuah"]}\t\t|{j["hargaBuah"]}') #perlu diotomasi untuk kerapihan bila nama terlalu panjang
                            else:
                                print(f'{k[4:]}\t|{j["namaBuah"]}\t\t\t|{j["stokBuah"]}\t\t|{j["hargaBuah"]}') 
                        break
                    else:
                        print('Index tidak ditemukan')
                except:
                    print('Masukkan angka!')
        
        elif menu == '4':
            #TRANSACTION
            historiBelanjaBuah = 0
            indexListBuah = []
            for m in buah:
                indexListBuah.append(m[4:])
            print(indexListBuah)
            jumlahJenisBuah = len(buah)
            markBuah = ''
            cart = {}
            #SHOWING LIST OF FRUITS
            while True:
                cartTemp = {}
                print('Daftar Buah :')
                print('Index\t|Nama\t\t\t|Stock\t\t|Harga')
                for i,j,k in zip(range(len(buah)),buah.values(),buah):
                    if len(j["namaBuah"]) > 6:
                        print(f'{k[4:]}\t|{j["namaBuah"]}\t\t|{j["stokBuah"]}\t\t|{j["hargaBuah"]}') #perlu diotomasi untuk kerapihan bila nama terlalu panjang
                    else:
                        print(f'{k[4:]}\t|{j["namaBuah"]}\t\t\t|{j["stokBuah"]}\t\t|{j["hargaBuah"]}')  
                
                while True:
                    try:
                        while True:
                            indexBuah = input('Masukkan index buah yang ingin dibeli\t: ')
                            #print("DEBUG")
                            markBuah = 'buah'+str(indexBuah)
                            #print(markBuah)
                            if str(indexBuah) not in indexListBuah:
                                print('Index tidak ditemukan!')
                            else:
                                cartTemp['namaBuah'] = (f'{buah[markBuah]["namaBuah"]}')
                                #print(cartTemp) #DELETED SOON
                                #cartTemp.append(buah[indexBuah][0])
                                break
                        break
                    except:
                        print('Masukkan angka!')
                        
                while True:
                    try:
                        while True:
                            stokBuahBeli = int(input('Masukkan banyak buah yang ingin dibeli\t: '))
                            if stokBuahBeli <= 0:
                                print('Masukkan angka lebih dari 0!')
                                #print('DEBUG 1')
                            #elif stokBuahBeli > int(f'{buah[markBuah]["stokBuah"]}'):
                            elif stokBuahBeli > int(buah[markBuah]["stokBuah"]):
                                print('Stok tidak cukup!')
                                #print('DEBUG 2')
                            else:
                                print('DEBUG 3')
                                cartTemp['stokBuah'] = stokBuahBeli
                                cartTemp['hargaBuah'] = buah[markBuah]["hargaBuah"]
                                #cartTemp.append(stokBuahBeli)
                                #cartTemp.append(buah[indexBuah][2])
                                
                                buah[markBuah]['stokBuah'] = buah[markBuah]['stokBuah']-stokBuahBeli
                                print('sisa stock:', buah[markBuah]['stokBuah'])
                                #print(cartTemp) #DELETED SOON

                                #buah[indexBuah][1] = buah[indexBuah][1]-stokBuahBeli
                                if buah[markBuah]['stokBuah'] == 0: #TAKE OUT THE EMPTY STOCK
                                    #delBuah = markBuah
                                    del buah[markBuah]
                                    #del buah[indexBuah]
                                else:
                                    pass
                                break
                        break
                    except:
                        print('Masukkan angka!')
                urutBelanja = ('buah'+str(historiBelanjaBuah))
                historiBelanjaBuah +=1
                #print(urutBelanja)
                cart[urutBelanja] = cartTemp
                #cart.append(cartTemp)
                
                #Print Cart

                print('Isi Keranjang :')
                print('Nama\t\t\t|Qty\t\t|Harga')
                for i,j,k in zip(range(len(cart)),cart.values(),cart):
                    if len(j["namaBuah"]) > 6:
                        print(f'{j["namaBuah"]}\t\t|{j["stokBuah"]}\t\t|{j["hargaBuah"]}') #perlu diotomasi untuk kerapihan bila nama terlalu panjang
                    else:
                        print(f'{j["namaBuah"]}\t\t\t|{j["stokBuah"]}\t\t|{j["hargaBuah"]}')  

                # print('Isi Keranjang :')
                # print('Nama\t\t\t|Qty\t\t|Harga')
                # for i,j in zip(range(len(cart)), cart):
                #     if len(j[0]) > 6:
                #         print(f'{j[0]}\t\t|{j[1]}\t\t|{j[2]}') #perlu diotomasi untuk kerapihan bila nama terlalu panjang
                #     else:
                #         print(f'{j[0]}\t\t\t|{j[1]}\t\t|{j[2]}')


                while True:
                    stateLagi = input('Tambahkan barang [Y/N]?:') 
                    
                    if stateLagi.upper() == 'Y' or stateLagi.upper() == 'N':
                        break                
                    else:
                        print('Perintah tidak dimengerti!')
                        continue
                if stateLagi.upper() == 'Y' or stateLagi.upper() == 'N':
                    if stateLagi.upper()== 'Y':
                        continue
                    else:
                        print('Mulai Perhitungan total:')
                        break
                
            #print(cart)

            #Rekap
            totalHarga = 0

            print('Daftar Belanja :')
            print('Nama\t\t\t|Qty\t|Harga\t\t\t|Total')
            for i,j,k in zip(range(len(cart)),cart.values(),cart):
                if len(j["namaBuah"]) > 6:
                    print(f'{j["namaBuah"]}\t\t|{j["stokBuah"]}\t|{j["hargaBuah"]}\t\t|{j["stokBuah"]*j["hargaBuah"]}') #perlu diotomasi untuk kerapihan bila nama terlalu panjang
                    totalHarga += j["stokBuah"]*j["hargaBuah"]
                else:
                    print(f'{j["namaBuah"]}\t\t\t|{j["stokBuah"]}\t|{j["hargaBuah"]}\t\t|{j["stokBuah"]*j["hargaBuah"]}')  
                    totalHarga += j["stokBuah"]*j["hargaBuah"]

            #Total  yang harus dibayar
            print(f'Grand Total yang harus dibayar : {totalHarga}')

            #Masukkan Jumlah Uang
            while True:
                try:
                    uang = float(input('Masukkan jumlah uang:'))

                    if uang>totalHarga:
                        print(f'Terima Kasih!\nUang kembali anda: IDR {uang-totalHarga}')
                        break
                    elif uang == totalHarga:
                        print('Terima Kasih')
                        break
                    else:
                        print(f'Transaksi anda dibatalkan!\nUang anda kurang sebesar IDR {totalHarga-uang}')
                except:
                    print('Masukkan angka!')
        
        elif menu == '5':
            break
        else:
            print('Angka menu tidak dikenali!')
    except:
        print('Masukkan nomor menu!')




    


    