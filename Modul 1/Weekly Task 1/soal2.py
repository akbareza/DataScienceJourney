numList = []
import random as rd
for i in range(20):
    numList.append(rd.randint(1,100))
 
while True:
    try:
        maxNum = int(input('Please enter the maximum number\t: '))  
        divNum = int(input('Please enter the divisor number\t: '))
        break
    except:
        print('Please enter the numerical value!')

print(numList)
for j in numList:
    if j > maxNum:
        continue
    else:
        if j%divNum == 0:
            print(j)
        else:
            continue
