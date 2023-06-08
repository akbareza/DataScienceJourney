#Mencari nilai terbesar ke-2
inputNumber = input('Plesae enter number(s), use comma (,) to seperate number(s): ').split(',')
number = []
for item in inputNumber:
    number.append(int(item))

# [int(item) for item]


if len(number)<2:
    print('Input angka lebih dari satu (1)')
elif len(number) == 2:
    if number[0] == number [1]:
        print('Kedua nilai sama, masukkan angka yang berbeda')
    else:
        number.sort()
        #print(number)
        print(f'Nilai kedua tertinggi = {number[0]}')
else:
    setNumber = set(number)
    listNumberFinal = []
    for i in setNumber:
        listNumberFinal.append(i)
    #print(listNumberFinal)
    listNumberFinal.sort()
    print(f'Nilai kedua tertinggi = {listNumberFinal[-2]}')

    
