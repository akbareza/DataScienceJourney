#cek the total of alphabet and digit
numOfDigit  = 0
numOfAplhabet = 0
sentence = input('Please enter the sentece : ')
for i in sentence:
    if i.isdigit():
        numOfDigit += 1
    elif i.isalpha():
        numOfAplhabet += 1
    else:
        continue

print(f'The number of alphabet\t: {numOfAplhabet}\nThe number of digit\t: {numOfDigit}')
