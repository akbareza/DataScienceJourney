number = [1,3,5,6,7,8]
median = 0
if len(number)%2 == 1:
    indexMedian = int((len(number)/2)-0.5)
    median = number[indexMedian]
    print (median)
else:
    indexMedian = int((len(number)/2)-0.5)
    median = (number[indexMedian] + number[indexMedian+1])/2
    print (median)