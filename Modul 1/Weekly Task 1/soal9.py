#Phone number
phoneNum = input('Please input your phone number  : ')
if phoneNum.isnumeric():    
    if len(phoneNum)>13:
        if phoneNum[:2] != '08':
            print("The phone number must not be above 13 digits AND must be strated with '08'!")
        else:
            print('The phone number must not be above 13 digits!')
    else:
        if phoneNum[:2] != '08':
            print("The phone number must be strated with '08'")
        else:
            print(f'My phone number is {phoneNum}')
else:
    print('The phone number must be numeric!')
