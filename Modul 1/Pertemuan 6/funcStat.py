import math as mt
######## INISIALISASI ########
# angka = []

def InputAngka():
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
    return(angka,len(angka))

def Mean(angka):
    ######## MEAN ########
    pembilangMean = 0
    for i in range(len(angka)):
        pembilangMean+=float(angka[i])
    
    mean = pembilangMean/penyebut
    return mean

def StdevVar(angka):
    ######## Stdev ########
    pembilangDev = 0
    for j in range(len(angka)):
        pembilangDev += ((float(angka[j])-mean)**2)

    stdev = mt.sqrt(pembilangDev/(penyebut-1))
    varians = stdev**2
    return stdev, varians



outInpAng = InputAngka()
print(outInpAng[0])

penyebut = outInpAng[1]
print(penyebut)

mean = Mean(outInpAng[0])
stdevVar = StdevVar(outInpAng[0])


######## OUTPUT ########
print (f'Angka {outInpAng[0]} memiliki:\n1. rata-rata : {mean}\n2. standar deviasi {stdevVar[0]}\n3. varian : {stdevVar[1]}')
    
    