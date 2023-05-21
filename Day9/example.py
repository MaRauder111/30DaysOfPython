a = -1

if a > 0:
    print('A is positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is negative number')

a = 3
print('A is positive number') if a > 0 else print('A is negative number')

a = 0
if a > 0:
    if a%2 == 0:
        print('A is a positive number and a even number')
    else:
        print('A is positive number')
elif a==0:
    print('A is zero')
else:
    print('A is negative number')

user = 'Justwant'
access_level = 10

if user == 'admin' or access_level >= 5:
    print('Access Granted')
else:
    print('Access denied')