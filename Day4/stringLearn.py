letter = 'P'
print(letter)

print(len(letter))

multilineString = """He is teacher and he enjoys teacher
I didn't find anything as rewarding
This is why he created 30 days of python
"""

print(multilineString)

firstName = 'Justwant'
lastName = 'Ningthoujam'

print(len(firstName) > len(lastName))

print('Hello World, I\'m doing 30 days of Python\nI have reach upto day 4\t After the tab')

# Old style formatting
print('First name is %s and last name is %s' %(firstName, lastName))

# New style formatting
print('First name is {} and last name is {}'.format(firstName,lastName))

a = 10
b = 20
print('Sum of a {} + b {} is {}'.format(a, b, a+b))

print(f'{a} + {b} = {a + b}')

stringValue = 'Python'
x,y,c,d,e,f = stringValue

print(x)

firstLetter = stringValue[0]
print(firstLetter)

lastIndex = len(stringValue) - 1
lastLetter1 = stringValue[lastIndex]
lastLetter = stringValue[-1]

print('%s %s' %(lastLetter, lastLetter1))
print('{} {}'.format(lastLetter,lastLetter1))
print(f'{lastLetter} {lastLetter1}')