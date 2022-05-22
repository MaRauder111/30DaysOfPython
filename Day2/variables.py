# Day 2: 30 Day of python programming

from math import floor, remainder
from xml.etree.ElementTree import PI

from numpy import floor_divide


firstName = 'Justwant'
lastName = 'Ningthoujam'
fullName = firstName + ' ' +lastName

print(fullName)

country = 'India'
city = 'Imphal'
age = 24
year = 2022
is_maried = False
is_true = True
is_light_on = False

valOne, valTwo = 'One', 2

print(valOne, valTwo)

print(type(firstName))

print(len(firstName))

print(firstName == lastName)

num_one = 5
num_two = 4

print(num_one + num_two)
print(num_two - num_one)
print(num_one * num_two)
print(num_one/num_two)
print(num_one%num_two)
print(pow(num_one,num_two))
print(floor(num_one/num_two))

rad = 30

import math
print(int(math.pi*pow(rad,2)))

print(int(2*math.pi*rad))

radValue = int(input('Enter the radius value '))
print(math.pi*pow(radValue,2))

print(2*math.pi*radValue)

print(type(firstName))
print(type(age))

print(len(firstName))

print(len(firstName) == len(lastName))

num_one = int(5)
num_two = int(4)

total = num_one + num_two
print(total)

diff = num_one - num_two
print(diff)

product = num_one * num_two
print(product)

division = num_one/num_two
print(division)

remainder = num_one%num_two
print(remainder)

exp = num_one ** num_two
print(exp)

floor_division = floor(num_one/num_two)
print(floor_division)

radius = int(30)
area_of_circle = math.pi * (radius ** 2)

print(area_of_circle)

circum_of_circle = 2 * math.pi * radius
print(circum_of_circle)

radiusInput = print(input('Enter Radius of circle '))

print(area_of_circle)

help('keywords')