import random as rd
#Conditional Statement
x = int(input('Masukan Angka antara 0 - 5:'))
y = rd.randint(0,5)
print(f'Jawaban = {y}')
if(x > 50):
    print('Lebih besar dari angka jawaban')
elif(x == y):
    print('BINGO!')
else:
    print('Lebih kecil dari angka jawaban')