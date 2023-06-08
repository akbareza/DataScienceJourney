import math as mt

alas = 12 
#Membuat input agar lebih dinamis, bila perhitungan pastikan sudah di-casting ke tipe data numeric
tinggi = float(input('Masukan nilai tinggi: '))
sisi1 = 2
sisi2 = 12

#tinggi = mt.sqrt(alas**2-((sisi1**2+sisi2**2)/4))

luasSegitiga = alas*tinggi/2

kelilingSegitiga  = sisi1 + sisi2 + alas

print('Tinggi = ',tinggi)
print(f'Luas segitiga = {luasSegitiga} dan Keliling Segitiga = {kelilingSegitiga}')
