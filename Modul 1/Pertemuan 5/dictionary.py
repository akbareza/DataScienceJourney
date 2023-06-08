dataDiri = {
    'Nama' : 'Akbareza',
    'Usia' : 26,
    12 : 15
}
print(dataDiri)
print(dataDiri['Nama'])

for i,j in zip(dataDiri,dataDiri.values()):
    print(f'{i} - {j}')

for key, value in dataDiri.items():
    print(f'{key} - {value}')