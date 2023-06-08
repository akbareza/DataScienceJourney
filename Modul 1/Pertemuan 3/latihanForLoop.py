while True:
    print("List Program:\n[1] Penghitung Faktorial\n[2] FizzBuzz")
    menu = input('Masukkan nomor program yang diinginkan:')

    if menu == '1': #mencari nilai faktorial
        while True:
            nilai = int(input('Masukkan nilai faktorial : '))
            if nilai < 0:
                print('Dilarang memasukkan bilangan negatif!')
            else:
                angka = 1
                for i in range(1, nilai+1,1): #pembentuk dari fungsi range adalah start, stop, step
                    angka *= i
                print(angka)
                break
        break

    elif menu == '2': #FIZZBUZZ
        akhir = int(input('Masukkan panjang bilangan :'))
        bil1 = int(input('Masukkan bilangan ke-1 : '))
        bil2 = int(input('Masukkan bilangan ke-2 : '))

        for i in range(1,akhir+1):
            if i%bil1==0 and i%bil2==0:
                print(f'fizzbuzz ({i})')
                continue
            elif i%bil1==0:
                print(f'fizz ({i})')
            elif i%bil2==0:
                print(f'buzz ({i})')
            else:
                print(i)
        break

    else:
        print('Masukkan ulang nomor program!')
