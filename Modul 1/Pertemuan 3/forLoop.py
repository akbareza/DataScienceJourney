#for loop in range(START,STOP,STEP)
for i in range(3): #range adalah fungsi untuk memberikan rentang angka 0 - 9
    print(i)

for i  in ['A', 1, 10.5, [2,3,5]]: #inti dari in adalah kita memberikan batasan pada loop yang kita punya
    print (i)

x = [2,5,6,7]
for j in x: #dapat dimasukkan ke variabel
    if j%2 ==0:
        print(f'{j} adalah bilangan genap')
    else:
        print(f'{j} adalah bilangan ganjil')


z = [2,5,6,7,9]
for i,j in zip(range(len(z)),z):
    if j%2 ==0:
        print  (f'Bilangan ke-{i+1} adalah {j} dan merupakan bilangan genap')
    else:
        print  (f'Bilangan ke-{i+1} adalah {j} dan merupakan bilangan ganjil')

