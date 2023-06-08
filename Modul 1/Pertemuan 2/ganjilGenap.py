##BELUM SELESAI KARENA MINUS DIANGGAP BUKAN ANGKA
#angka = int(input('Masukkan angka:'))
angka = int(input('Masukkan angka:'))
try: #ERROR HANDLING
    if (angka>0):
        if(angka%2==0):
            print(f'Angka {angka} tergolong bilangan GENAP!')
        else:
            print(f'Angka {angka} tergolong bilangan GANJIL!')
    elif (angka==0):
        print(f'Angka {angka} tidak tergolong bilangan GENAP ataupun GANJIL!')
    else:
        print('Masukkan angka positif!')
except: #ERROR HANDLING
    print('Masukkan Angka!')

