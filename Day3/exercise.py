from traceback import print_tb
from numpy import intp


age = int(24)
height = float(3.14)
complex_number = 1+2j

base = float(input('Enter the base '))
height = float(input('Enter the height '))

print('The area of the triangle is ', float((0.5*base*height)))

a = int(input('Enter the first side '))
b = int(input('Enter the second side '))
c = int(input('Enter the third side '))

print('Perimeter is ', a+b+c)

length = int(input('Enter the length of rect '))
width = int(input('Enter the width '))

print('Perimeter of rect ', int((2*(length+width))))

radCir = int(input('Enter the radius of circle '))
pi = 3.14

print('Area of circle is ', pi * radCir * radCir)
print('Circumference of circle is ', 2 * pi * radCir)

x = int(input('Enter the x intercept value'))
y = 2*x-2
print('Y intercept is ', y)

x1 = int(2)
x2 = int(6)
y1 = int(2)
y2 = int(10)

m = (y2-y1)/(x2-x1)

print('Slope of y and x is ',m)

print(m == y)

xValue = int(input('Enter value of x for equation: '))
yValue = xValue**2 + 6*xValue + 9

print(yValue)

stringOne = 'python'
stringTwo = 'dragon'

print(stringOne == stringTwo)

stringThree = 'I hope this course is not full of jargon'

print('jargon' in stringThree)
print('on' in 'python')

lenString = float(len('python'))

stringFloat = str(lenString)
print(lenString)
print(stringFloat)