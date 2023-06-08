def cekAngka(text):
    while True:
        try:
            inputValue = input(f'{text}')
            convertInput = float(inputValue)
            valid = isinstance(convertInput,(float))
            if valid == True:
                break
            else:
                continue
        except:
            print('THE INPUT IS NON-NUMERICAL')
    return convertInput

def printMenu():
    print('''
        Menu:
        \t\t[1] Total
        \t\t[2] Rata-rata
        \t\t[3] Nilai Tengah
        \t\t[4] Exit
        Masukan nomor menu yang ingin kalian pilih:
    ''')
    cekAngka()


# angka = cekAngka('Masukkan input : ')
# print(angka)

menu = 1
