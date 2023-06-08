# Terdapat 3 buah variable yang input, anggap saja bernama X, Y, dan Z. 
# Buatlah sebuah program untuk mengeksekusi ketiga variable tersebut, dengan ketentuan berikut ini.
    # 1. Value X, Y, dan Z adalah sebuah input
    # 2. Jika nilai X, Y, dan Z sama, maka lakukan perkalian terhadap ketiga variable tersebut.
    # 3. Jika nilai X, Y, dan Z berbeda, maka jumlahkan ketiganya.
# Jika belum terbayang, perhatikan flowchart dan contoh output berikut ini.
x = int(input('Masukkan nilai X: '))
y = int(input('Masukkan nilai Y: '))
z = int(input('Masukkan nilai Z: '))

if x == y == z:
    print (x*y*z)
else:
    print(x+y+z)


