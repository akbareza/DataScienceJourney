#BINGO
import random as rd
#Conditional Statement

y = rd.randint(1,9)

while True:
    try:
        x = int(input('Plese guess the number between 1 - 9 :'))
        if(x == y):
            print('Bingo!! Right Guess!!')
            break
        else:
            continue
    except:
        pass