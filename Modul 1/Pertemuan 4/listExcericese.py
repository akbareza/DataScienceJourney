angka = []
while True:
    while True:
        try:
            inputAngka = float(input('Input data numeric : '))
            break
        except:
            print('Masukkan angka!')
    angka.append(float(inputAngka))
    print(angka)
    inputState = input('tambahkan angka [Y/N]: ')
    if inputState.upper() == 'Y':
        continue
    elif inputState.upper() == 'N':
        break
    else: #MASIH SALAH DISINI KALAU ELSE HARUSNAY KEMBALI KE INPUT STATTE
        continue
#jumlahAngka = len(angka)
angka.sort()

print(f'Nilai Min = {angka[0]}')
#print(f'Nilai Max = {angka[jumlahAngka-1]}')
print(f'Nilai Max = {angka[-1]}')