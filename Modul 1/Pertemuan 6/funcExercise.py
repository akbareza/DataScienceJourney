def pengaliLima(list1):
    listFinal = [] #hanya berlaku lokal
    for i in list1:
        listFinal.append(i*5)
    return listFinal #Value saja, variabel tetap lokal

def reverseWord(word):
    #angka = input('Input angka yang hendak dibalik : ')
    listAsli = []
    output = ''

    for i in word:
        listAsli.append(i)
    #print('angka asli = ', word)
    listReverse = listAsli.copy()

    for j,k,l in zip(range(len(listAsli)),listAsli,range(1,len(listAsli)+1)):
        #print(f'{j}, {k}, {l}')
        listReverse[j] = listAsli[j-(l+j)]
        output+=listReverse[j]
    #print('angka setelah dibalik = ',output)

    return(output)

def reverseSentence(listSentence):
    listFinal = []
    for i in listSentence:
        listFinal.append(reverseWord(i))
    return listFinal

def countUpper(listSentece):
    count = 0
    for i in listSentece:
        char = str(i)
        if char.isupper():
            count+=1
    return count

def countLower(listSentece):
    count = 0
    for i in listSentece:
        char = str(i)
        if char.islower():
            count+=1
    return count
            
#SOAL 1
## listAngka = [int(i) for i in input('Input Number(s): ').split(',')]
## print(pengaliLima(listAngka))


#SOAL2
listSentence = input('Input Sentence: ').split(' ')
listReverseFinal = reverseSentence(listSentence)
for i in listReverseFinal:
    print(i, end= ' ')
print('')

# #SOAL3
# textSoal3 = 'SiaPa Aku' #input('Input Sentence: ').split(' ')
# print(f'Kalimat asli : {textSoal3}')
# print(f'Banyaknya huruf kapital dalam kalimat ini adalah : {countUpper(textSoal3)}')
# print(f'Banyaknya huruf non-kapital dalam kalimat ini adalah : {countLower(textSoal3)}')

