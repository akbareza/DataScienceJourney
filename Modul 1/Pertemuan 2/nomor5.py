# Buatlah sebuah perhitungan untuk mengkonversi suhu Fahrenheit ke dalam bentuk Celsius. 
# Kemudian, jika hasil konversinya diantara 36.5 – 37.2 derajat maka tampilkan pesan suhu badan normal ;
# jika di bawah suhu tersebut, tampilkan hipotermia;
# dan jika di atas tampilkan hipertermia. Berikut ini contohnya.
suhuF = float(input('Masukkan suhu Farenheit: '))
suhuCRaw = (suhuF - 32) * 5/9
suhuC = float("{:.2f}".format(suhuCRaw)) #Ambil 2 dibelakang koma
if suhuC < 36.5:
    print(f'Suhu anda {suhuC}\u00b0C, anda sedang mengalami Hipotermia!\nSegera lakukan pertolongan pertama!')
elif suhuC >= 36.5 and suhuC <= 37.2:
    print(f'Suhu anda {suhuC}\u00b0C, suhu badan anda normal!')
else:
    print(f'Suhu anda {suhuC}\u00b0C, anda sedang mengalami Hipertermia!\nSegera lakukan pertolongan pertama!')