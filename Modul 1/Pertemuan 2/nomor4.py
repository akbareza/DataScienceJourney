# Buatlah sebuah program untuk menampilkan sebuah kalimat yang jumlah karakternya 
# dibawah 20 karakter. Jika tidak memasukan inputan apa-apa, 
# program akan menampilkan pesan untuk memasukan sebuah kalimat. Berikut ini contoh outputnya.

kalimat = input('Masukkan kalimat: ')
#print (kalimat)
#print (len(kalimat))
if len(kalimat) == 0:
    print('Masukkan kalimat!')
elif len(kalimat) > 20:
    print('Kalimat yang dimasukkan terlalu panjang')
else: # len(kalimat) > 0
    print(f'Jumlah kalimat ideal, berikut ini adalah kalimatnya: \'{kalimat}\'')
