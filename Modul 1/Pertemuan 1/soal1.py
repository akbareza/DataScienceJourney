import math as mt
x = float(input('masukan nilai x:'))
y = float(input('masukan nilai y:'))
z = float(input('masukan nilai z:'))

#POW adalah fungsi untuk memangkatkan
w = mt.pow(((x+y*z)/(x*y)),z)

print(f'Hasil = {w}')