import math as mt

#inisialisasi
h = float(input('Please enter the height value in centimeter!: '))
r = float(input('Please enter the radius value in centimeter!: '))

#rumus
surfaceArea = (2*mt.pi*(r**2)+(2*mt.pi*r*h))
volume = mt.pi * (r**2) * h

#output
print(f'The cylinder surface area that has {h} as height and {r} as radius is {surfaceArea}\u00b2')
print(f'and the volume of the cylinder is {volume}\u00b3')