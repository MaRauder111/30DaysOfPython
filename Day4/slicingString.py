from re import sub


language = 'Python'

firstThree = language[0:3]

print('%s' %(firstThree))
print('{}'.format(firstThree))
print(f'{firstThree}')

print(f'Last Index is {(len(language) - 1)}')

lastThree = language[3:6]
print(f'{lastThree}')

last_three_new = language[-3:]
print(last_three_new)

last_three = language[3:]
print(last_three)

# string reverse

print(language[::-1])

# skipping character while slicing

print(language[0:6:2])

string = 'new learning'
print(string.capitalize())

print(string.count('n'))
print(string.count('n', 7, 14))
print(string.endswith('w'))

new_string = 'new\tlearning'
print(new_string.expandtabs())
print(new_string.expandtabs(10))

print(string.find('n'))
print(string.find('ew'))

print(string.rfind('n'))

first_name = 'Justwant'
last_name = 'Ningthoujam'

print('First name is %s and last name is %s' %(first_name, last_name))
print('First name is {} and last name is {}'.format(first_name,last_name))
print(f'First name is {first_name} and last name is {last_name}')

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))
print(challenge.index('t'))

print(challenge.rindex(sub_string))
print(challenge.rindex('y'))

string_one = 'ThirtyDaysOfPython'
print(string_one.isalnum())

string_two = '30 Days of Python'
print(string_one.isalpha())
print(string_two.isalnum())
print(string_two.isdecimal())
print(string_two.isdigit())
print(string_two.islower())

web_tech = ['HTML', 'CSS', 'JS', 'React']
result = '#'.join(web_tech)
print(result)

print(string_two.strip('30'))
print(string_two.replace('30', '100'))

string_three = 'thirty days of python'
print(string_three.title())
print(string_three.swapcase())
print(string_three.startswith('t'))