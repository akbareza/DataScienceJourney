#MAIN LIST OF FRUITS
buah = [['Apel', 20.0, 10000.0],['Jeruk', 15.0, 15000.0], ['Anggur', 25.0, 20000.0]]



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
            for i,j in zip(range(len(buah)), buah):
                if len(j[0]) > 6:
                    print(f'{i}\t|{j[0]}\t\t|{j[1]}\t\t|{j[2]}') #perlu diotomasi untuk kerapihan bila nama terlalu panjang
                else:
                    print(f'{i}\t|{j[0]}\t\t\t|{j[1]}\t\t|{j[2]}') 
        elif menu == '2':
            #ADDING LIST OF FRUITS
            buahTemp = []
            namaBuah = input('Masukkan nama buah\t: ')
            buahTemp.append(namaBuah)
            while True:
                try:
                    while True:
                        stokBuah = float(input('Masukkan stok buah\t: '))
                        if stokBuah <= 0:
                            print('Masukkan angka lebih dari 0')
                        else:
                            buahTemp.append(stokBuah)
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
                            buahTemp.append(hargaBuah)
                            break
                    break
                except:
                    print('Masukkan angka!')

            buah.append(buahTemp)
            #print(buahTemp)
        elif menu == '3':
            #DELETE ITEM IN LIST OF FRUITS
            jumlahJenisBuah = len(buah)
            
            while True:
                try:
                    delBuah = int(input('Masukkan nomor index buah yang ingin dihapus: '))
                    if delBuah in range(0,jumlahJenisBuah):
                        del buah[delBuah]
                        print('Daftar Buah :')
                        print('Index\t|Nama\t\t\t|Stock\t\t|Harga')
                        for i,j in zip(range(len(buah)), buah):
                            if len(j[0]) > 6:
                                print(f'{i}\t|{j[0]}\t\t|{j[1]}\t\t|{j[2]}') #perlu diotomasi untuk kerapihan bila nama terlalu panjang
                            else:
                                print(f'{i}\t|{j[0]}\t\t\t|{j[1]}\t\t|{j[2]}') 
                        break
                    else:
                        print('Index tidak ditemukan')
                except:
                    print('Masukkan angka!')
        elif menu == '4':
            #TRANSACTION
            jumlahJenisBuah = len(buah)
            cart = []
            #SHOWING LIST OF FRUITS
            while True:
                cartTemp = []
                print('Daftar Buah :')
                print('Index\t|Nama\t\t\t|Stock\t\t|Harga')
                for i,j in zip(range(len(buah)), buah):
                    if len(j[0]) > 6:
                        print(f'{i}\t|{j[0]}\t\t|{j[1]}\t\t|{j[2]}') #perlu diotomasi untuk kerapihan bila nama terlalu panjang
                    else:
                        print(f'{i}\t|{j[0]}\t\t\t|{j[1]}\t\t|{j[2]}') 
                
                while True:
                    try:
                        while True:
                            indexBuah = int(input('Masukkan index buah yang ingin dibeli\t: '))
                            if indexBuah < 0 or indexBuah >= jumlahJenisBuah:
                                print('Index tidak ditemukan!')
                            else:
                                cartTemp.append(buah[indexBuah][0])
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
                            elif stokBuahBeli > int(buah[indexBuah][1]):
                                print('Stok tidak cukup!')
                            else:
                                cartTemp.append(stokBuahBeli)
                                cartTemp.append(buah[indexBuah][2])
                                buah[indexBuah][1] = buah[indexBuah][1]-stokBuahBeli
                                if buah[indexBuah][1] == 0: #TAKE OUT THE EMPTY STOCK
                                    del buah[indexBuah]
                                else:
                                    pass
                                break
                        break
                    except:
                        print('Masukkan angka!')
                cart.append(cartTemp)
                
                #Print Cart
                print('Isi Keranjang :')
                print('Nama\t\t\t|Qty\t\t|Harga')
                for i,j in zip(range(len(cart)), cart):
                    if len(j[0]) > 6:
                        print(f'{j[0]}\t\t|{j[1]}\t\t|{j[2]}') #perlu diotomasi untuk kerapihan bila nama terlalu panjang
                    else:
                        print(f'{j[0]}\t\t\t|{j[1]}\t\t|{j[2]}') 


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
                
            print(cart)

            #Rekap
            totalHarga = 0
            print('Daftar Belanja :')
            print('Nama\t\t\t|Qty\t|Harga\t\t\t|Total')
            for i,j in zip(range(len(cart)), cart):
                if len(j[0]) > 6:
                    print(f'{j[0]}\t\t|{j[1]}\t|{j[2]}\t\t|{j[1]*j[2]}') #perlu diotomasi untuk kerapihan bila nama terlalu panjang
                    totalHarga += j[1]*j[2]
                else:
                    print(f'{j[0]}\t\t\t|{j[1]}\t|{j[2]}\t\t|{j[1]*j[2]}')
                    totalHarga += j[1]*j[2]

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




    


    