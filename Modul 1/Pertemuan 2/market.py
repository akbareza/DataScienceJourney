apel = float(input('Masukan jumlah apel: '))
jeruk = float(input('Masukan jumlah jeruk: '))
anggur = float(input('Masukan jumlah anggur: '))

print('\n\nDetail Belanja\n')

print(f'Apel : {apel} x 10000 = IDR {apel*10000}')
print(f'Jeruk : {jeruk} x 15000 = IDR {jeruk*15000}')
print(f'Anggur : {anggur} x 20000 = IDR {anggur*20000}')

total = float((apel*10000)+(jeruk*15000)+(anggur*20000))
print(f'\nTotal : IDR {total}')

uang = float(input('Masukkan jumlah uang:'))

if uang>total:
    print(f'Terima Kasih!\nUang kembali anda: IDR {uang-total}')
elif uang == total:
    print('Terima Kasih')
else:
    print(f'Transaksi anda dibatalkan!\nUang anda kurang sebesar IDR {total-uang}')
