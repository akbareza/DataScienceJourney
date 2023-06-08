#letter minimum per word
output = []
minWord = int(input('Please enter the minimum letter : '))
sentence = input('Please enter the sentece : ').split()
print(sentence)
for i in sentence:
    if len(i) > 4:
        output.append(i)
    else:
        continue
print(f'The word(s) that has letter more than 4 is : ')
print(output)