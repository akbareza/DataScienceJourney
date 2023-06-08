jmlSimbol = int(input('Masukkan jumlah terbanyak : '))

for i in range(jmlSimbol,0,-1):
    if i != 1:
        print ('*'*i)
    else:
        print ('*'*i)
        for j in range(2,jmlSimbol+1):
            print('*'*j)

print('cek')

# for k in range(1,jmlSimbol+1,1):
#     for l in range(k):
#         print('  '*(jmlSimbol-k)+('*'*(k)))
