# Buatlah sebuah program menu untuk menghitung beberapa rumus bangun ruang. 
# Ketika memasukan angka 1, akan menghitung rumus segitiga
# Ketika memasukan angka 2, akan menghitung rumus persegi
# Ketika memasukan angka 3 atau karakter lain, akan mengeluarkan output ‘Masukan Inputan Yang Benar’

print('Menu Menghitung Bangun Ruang')
print('Masukkan angka 1 untuk menghitung luas segitiga')
print('Masukkan angka 2 untuk menghitung luas persegi\n')

try:
    inputMenu = int(input('Masukkan Angka: '))
    if inputMenu == 1:
        alas = float(input('Masukaan nilai alas: '))
        tinggi = float(input('Masukaan nilai tinggi: '))
        luas = alas * tinggi / 2
        print(f'Luas segitiga = {luas}')
    elif inputMenu == 2:
        sisi = float(input('Masukaan nilai sisi: '))
        luas = sisi * sisi
        print(f'Luas persegi = {luas}')
    else:
        print('Masukkan inputan yang benar')

    print('Terima kasih!')
except:
    print('Masukkan inputan yang benar')
    print('Terima kasih!')
