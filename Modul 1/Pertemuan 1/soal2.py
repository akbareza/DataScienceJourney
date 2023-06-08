hari = int(input('Masukan hari:'))

tahun = hari//360
hari -= (360*tahun)
#hari = hari - (360*tahun)

bulan = hari//30
hari -= 30 * bulan

minggu = hari//7
hari -= 7*minggu

print(f'Hasil Konversi = {tahun} tahun {bulan} bulan {minggu} minggu {hari} hari')