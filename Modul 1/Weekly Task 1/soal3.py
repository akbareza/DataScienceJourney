#REVERSE LIST W/O FUNCTION
angka = input('Input angka yang hendak dibalik : ')
listAngka = []
output = ''

for i in angka:
    listAngka.append(i)
print('angka asli = ', angka)
listReverse = listAngka.copy()

for j,k,l in zip(range(len(listAngka)),listAngka,range(1,len(listAngka)+1)):
    listReverse[j] = listAngka[j-(l+j)]
    output+=listReverse[j]
print('angka setelah dibalik = ',output)