kata1 = input('Input Kata 1: ')
kata2 = input('Input Kata 2: ')

kata1Baru = kata1.replace(kata1[0:2],kata2[0:2])
kata2Baru = kata2.replace(kata2[0:2],kata1[0:2])

print(kata1Baru,kata2Baru)