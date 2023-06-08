import math as mt
######## INISIALISASI ########
angka = input('Input angka yang ingin diinputkan, pisahkan dengan tanda koma (,) : ')
angka = angka.split(',')
pembilangMean = 0
pembilangDev = 0
penyebut = len(angka)

######## MEAN ########
for i in range(len(angka)):
    pembilangMean+=int(angka[i])

mean= pembilangMean/penyebut

######## STANDAR DEVIASI DAN VARIAN ########
for j in range(len(angka)):
    pembilangDev += ((int(angka[j])-mean)**2)

stdev = mt.sqrt(pembilangDev/(penyebut-1))
varians = stdev**2


######## OUTPUT ########
print (f'Angka {angka} memiliki:\n1. rata-rata : {mean}\n2. standar deviasi {stdev}\n3. varian : {varians}')
    
    