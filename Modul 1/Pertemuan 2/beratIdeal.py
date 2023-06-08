massa = float(input('Masukkan Massa (kg):'))
tinggi = float(input('Masukkan Tinggi (cm):'))

imt = massa/((tinggi/100)**2)

print(f'Massa {massa} kg dan tinggi {tinggi/100} m')

if imt<18.5:
    print(f'{imt}, BERAT BADAN KURANG!')
elif imt>=18.5 and imt < 25:
    print(f'{imt}, BERAT BADAN IDEAL!')
elif imt>=25.0 and imt < 30:
    print(f'{imt}, BERAT BADAN BERLEBIH!')
elif imt>=30.0 and imt < 40:
    print(f'{imt}, BERAT BADAN SANGAT BERLEBIH!')
else:
    print(f'{imt}, OBESITAS!')