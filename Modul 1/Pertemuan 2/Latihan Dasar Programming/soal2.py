# Seorang anak ingin mengetahui luas dan keliling sebuah lingkaran.
# Untuk mempermudah hal tersebut, seorang programmer ingin membuat program untuk
# menghitung luas dan keliling lingkaran hanya dengan memasukan nilai jari-jarinya saja.
# Anggaplah Anda merupakan programmer tersebut, buatlah sebuah program menghitung luas dan keliling 
# dengan ketentuan sebagai berikut:
    # Nilai jari-jarinya berupa inputan
    # Hitunglah luas dan keliling lingkaran utuh dan setengah lingkaran
    # Tampilkan juga nilai diameter lingkaran
# Berikut ini output contoh program yang diinginkan
import math as mt
r = float(input('Please enter the radius value in centimeter!: '))
print(f'The circle has radius {r} cm and the diamter {r*2}')
area = mt.pi * (r**2)
circumference = mt.pi * (r*2)
print(f'The area of the circle is {area}\u00b2 and the circumference is {circumference}')

