# Coba buatlah sebuah program untuk mengganti sebuah karakter tertentu dalam sebuah string.
# Ada beberapa ketentuan yang perlu diperhatikan, yaitu :
    # 1. Karakter yang diganti adalah karakter pertama dari sebuah inputan.
    # 2. Karakter pertama tersebut tidak terganti
    # namun karakter yang sama di inputan tersebutakan terganti sepenuhnya.
    # 3. Karakter penggantinya adalah sebuah inputan.

kalimat = input('Masukkan sebuah kalimat:')
charChanger = input('Masukka karakter pengganti:')

hurufAwal = kalimat[0]
kalimatSisa = kalimat[1:]
# print(kalimatSisa)
kalimatSisa = kalimatSisa.replace(hurufAwal,charChanger)
# print(kalimatSisa)
kalimatBaru = (hurufAwal+kalimatSisa)
print(kalimatBaru)
