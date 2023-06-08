# #PRIME NUMBER
angkaAwal = int(input('Masukkan angka awal\t: '))
angkaAkhir = int(input('Masukkan angka akhir\t: '))
banyakBil = 0
primeNumber = []
for i in range(angkaAwal,angkaAkhir+1):
    if i > 1: #must be above one
        for j in range(2,i): #dicari apakah ada fakorialnuya selain dirinya sendiri
            if i%j == 0:
                print('Non-Prime')
                break
        else: #kalau tidak ada break
            print(i)
            primeNumber.append(i)
            banyakBil+=1
print(f'Total bilangan prima diantara {angkaAwal} dan {angkaAkhir} sebanyak {banyakBil} Bilangan\nBerikutini daftar Bilangan Prima dari rentan tersebut:')
#print(primeNumber)
for j in primeNumber:
     print(j)


