# [1] INISIALISASI VARIABEL UTAMA DAN VALUE
while True:
    inputText = input('Input segitiga kata : ')
    listInputText = []
    panjangKata = len(inputText) #PANJANG
    if ' ' in inputText:
        print('HARAP MASUKKAN SATU KATA SAJA!')
        continue
    else:
        break

# [2] INPUT TO LIST PER HURUF
for i in inputText:
    listInputText.append(i)

# [3] BATAS PRINT HURUF PER BARIS
batas = 0
panjangKataCopy = panjangKata
for i in range(0,panjangKata,1):
    if panjangKataCopy-i > 0: 
        panjangKataCopy -= i #kurangi panjang kata terus sampai abis banget
        batas +=1 #tambahkan batas
    else:
        break

# [4] CEK ERROR KURANG KATA
cekError = 0 
for i in range(1,batas+1):
    cekError += i
if cekError%panjangKata == 0:
    pass
else:
    print('\nMaaf, Panjang kata tidak mencukupi!')


# [5] PRINT OUTPUT SEGITIGA
for i in range(1,batas+1):
    #print(f'batas ke-{i}') #diputaran ke-i loop secara i kali
    try:
        for j in range(i):
            print(listInputText[0], end='') #AMBIL PALING DEPAN
            del [listInputText[0]] #BUANG PALING DEPAN
        print('')
    except: #HANDLING ERROR UNTUK YANG KURANG
        print('')