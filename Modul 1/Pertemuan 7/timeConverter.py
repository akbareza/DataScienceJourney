def secToHour(sec):
    global hour
    hour = sec//3600
    # print(sec)
    global timeInput
    timeInput = sec-(hour*3600)
    return timeInput

def secToMinute(sec):
    global minute
    minute  = sec//60
    global timeInput
    timeInput = sec-(minute*60)
    return timeInput

def force2digit(digit):
    if len(digit) == 1:
        digit = '0'+str(digit)
    else:
        pass
    return digit

def validasiAngkaBulatPositif(nmVariable, nmInput):
    while True:   
        try:
            nmVariable = int(input(f'Masukkan {nmInput} : '))
            if nmVariable < 0 or nmVariable >359999: # nmVariable >359999 tambahan khusus fungsi
                print('Invalid input!')
            else:
                break
        except:
            print('Invalid input!')
    return nmVariable



#while True:   
timeInput = 0
timeInput = validasiAngkaBulatPositif(timeInput,'detik')
    # valid = False
    # timeInput = input(f'Masukkan detik : ')
    # valid = validasiAngkaBulatPositif(timeInput)
    
    
    # try:
    #     timeInput = int(input(f'Masukkan detik : '))
    #     if timeInput < 0 or timeInput >359999: # nmVariable >359999 tambahan khusus fungsi
    #         print('Invalid input!')
    #     else:
    #         break
    # except:
    #     print('Invalid input!')


secToHour(timeInput)
secToMinute(timeInput)

print(f'{force2digit(str(hour))}:{force2digit(str(minute))}:{force2digit(str(timeInput))}')

