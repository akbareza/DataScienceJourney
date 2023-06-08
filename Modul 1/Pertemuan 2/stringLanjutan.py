#Escape Character
x = 'I\'m \nAkbareza\tMuhammad\\Ab\bang'
print(x)
print('---------------------------------------')

#String Function
print(f'Terdapat total {len(x)} karakter pada variabel x')
print(x.index('Akbareza'))
print(x.split(' ')) #disimpan dalam bentuk list

y = 'Masyita kok cantik banget ya?'
print(y[0:3]) #spasi dihitung
print(y[-3:])