#NUMBER PATTERN
jmlAngka = int(input('Masukkan jumlah angka maksimal : '))
list = []

for i in range(jmlAngka):
    list.append(i+1)
    for j in list :
        print(j, end=' ')
    print('') #MAKE THE NEW LINE
