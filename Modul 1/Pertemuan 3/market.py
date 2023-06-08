#==============================INPUT STOK=========================================
stokApel = 10
stokJeruk = 10
stokAnggur = 10

#==============================INPUT ITEM========================================


while True:
    apel = float(input('Masukan jumlah apel: '))
    if apel < 0:
        print('Maaf, tidak dapat input bilangan negatif!')
    elif apel > 10:
        print(f'Stok apel tersisa : {stokApel}, harap input kembali!')
    else:
        break
while True:
    jeruk = float(input('Masukan jumlah jeruk: '))
    if jeruk < 0:
        print('Maaf, tidak dapat input bilangan negatif!')
    elif jeruk > 10:
        print(f'Stok jeruk tersisa : {stokJeruk}, harap input kembali!')
    else:
        break
while True:
    anggur = float(input('Masukan jumlah anggur: '))
    if anggur < 0:
        print('Maaf, tidak dapat input bilangan negatif!')
    elif anggur > 10:
        print(f'Stok anggur tersisa : {stokAnggur}, harap input kembali!')
    else:
        break

#==============================KALKULASI========================================

print('\n\nDetail Belanja\n')

print(f'Apel : {apel} x 10000 = IDR {apel*10000}')
print(f'Jeruk : {jeruk} x 15000 = IDR {jeruk*15000}')
print(f'Anggur : {anggur} x 20000 = IDR {anggur*20000}')

total = float((apel*10000)+(jeruk*15000)+(anggur*20000))
print(f'\nTotal : IDR {total}')

#========================PEMBAYARAN==========================================================    
while True:
    uang = float(input('Masukkan jumlah uang:'))

    if uang>total:
        print(f'Terima Kasih!\nUang kembali anda: IDR {uang-total}')
        break
    elif uang == total:
        print('Terima Kasih')
        break
    else:
        print(f'Transaksi anda dibatalkan!\nUang anda kurang sebesar IDR {total-uang}')
    