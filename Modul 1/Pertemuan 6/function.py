#Example of function without input and output, no parameter and no return
def namePrint():
    print('Akbareza Muhammad')

def tambah():
    x = int(input('enter a number : '))
    y = int(input('enter a number : '))
    print(x+y)

#Example of function with input and without output, has parameter and no return
def kali(x,y):
    print(x*y)

#Example of function with input and output, has parameter and return
def bagi(x=13,y=1): #13 and 1 is default paramter, works when there is no value added to the parameter
    #print(x/y)
    return x/y #save the value of the function's output.

def kaliBagi(x,y):
    a = (x*y)+(bagi(x,y))
    return(a)

namePrint() 
tambah()
kali(x=10, y=5) #=== kali(5,10), sehingga bisa diacak urutan untuk input parameternya

#print(bagi(10,5))
outputBagi = bagi(10,5) + 10
print(outputBagi) 

print("DEBUG")

print(kaliBagi(1,2))