print('Aplikasi Konversi antara Celcius - Farenheit\n')
try:
    suhuAwal = input('Masukkan suhu yang ingin dikonversikan beserta satuannya (Co: 100F atau 20C): ')
    if(len(suhuAwal))==0:
        print('Masukkan input sesuai dengan ketentuan!')
    else:
        if 'C' in suhuAwal or 'c' in suhuAwal:
            suhu = float((suhuAwal[:-1]))
            cToF = (9*suhu + (32*5))/5
            print (f'Suhu {suhuAwal} jika dikonversikan ke dalam Farenheit menjadi {cToF}F')
        elif 'F' in suhuAwal or 'f' in suhuAwal:
            suhu = float((suhuAwal[:-1]))
            fToC = (5*(suhu-32))/9
            print (f'Suhu {suhuAwal} jika dikonversikan ke dalam Celcius menjadi {fToC}C')
        else:
            print('Masukkan input sesuai dengan ketentuan!')
except:
    print('Masukkan input sesuai dengan ketentuan!')