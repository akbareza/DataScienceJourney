import math as mt
######## INISIALISASI ########
angka = []

while True:
    inputAngka = input('Input data numeric : ')
    angka.append(float(inputAngka))
    print(angka)
    inputState = input('tambahkan angka [Y/N]: ')
    if inputState.upper() == 'Y':
        continue
    else:
        break

penyebut = len(angka)
pembilangMean = 0
pembilangDev = 0
######## MEAN ########
for i in range(len(angka)):
    pembilangMean+=float(angka[i])

mean= pembilangMean/penyebut

######## STANDAR DEVIASI DAN VARIAN ########
for j in range(len(angka)):
    pembilangDev += ((float(angka[j])-mean)**2)

stdev = mt.sqrt(pembilangDev/(penyebut-1))
varians = stdev**2


######## OUTPUT ########
print (f'Angka {angka} memiliki:\n1. rata-rata : {mean}\n2. standar deviasi {stdev}\n3. varian : {varians}')
    
    