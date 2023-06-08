sentence = input('Please enter the sentence : ')
output = ''
if sentence == '':
    print('Please input the value!')
else:
    if len(sentence) > 20:
        print('The character limit is 20')
    else:
        sentence = sentence.split()
        for i in sentence:
            output += i
        print(f'*{output.upper()}*')
