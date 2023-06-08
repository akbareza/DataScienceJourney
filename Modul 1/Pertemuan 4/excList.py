#List
data = ['hallo', 1, True, 'Akbareza', False, 5, str(23), 84.2, 'True', 'True']
print(data[-4:])
print([data[2], data[1]])
print(data.index('Akbareza'))

stringA = 'Akbareza Muhammad'.split() #list can be constructed with a string
print(stringA)

#change a data in list
data[0] = 'Hai'
data[-1] = 10/2
print(data)

#add data to list
#append : add data in the last row
data.append('Data Science')

#insert : add data with specified index
data.insert(4,'Muhammad') #add data to data[4]

print(data)

#Empyt List
# emptyList = []
# print(emptyList)
# for i in range(5):
#     a = float(input(f'Masukkan angka ke-{i}: '))
#     emptyList.append(a)
# print(emptyList)

#shorthand add to list with for loop
# emptyList = [float(input(f'Masukkan angka ke-{i+1}: ')) for i in range(5)]
# print(emptyList)

#another shorthand
# emptyList = [float(i) for i in input(f'Masukkan angka (pisahkan dengan spasi): ').split()]
# print(emptyList)


#delete data
data.remove(5) #remove first item with 5 value
data.pop() #remove last item
del data[1] #remove specified index
print(data)

# data.clear()
# print (data)

print(f'Banyaknya anggota List : {len(data)}') #jumlahList

print(data+stringA) #concat 2 string

numeric = [1,10,100,4,6,2.3]
numeric.reverse #reversing the index
print(numeric)
numeric.sort(reverse=True) #sorting VALUE with reverse, should be same data types.
print(numeric)

#2D List
newList = [
    [1,2,3],
    ['A','B','C'],
    'Akbareza Muhammad'.split()
]
print(newList)
print(newList[2][0])
