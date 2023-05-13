letter = 'p'
print(letter)
print(len(letter))

multi_line = '''I am enjoying 30Days of
Python'''

first_name = 'Ningthoujam'
last_name = 'Justwant'

print(first_name + last_name)
print(len(first_name) < len(last_name))

print('Hello\nWorld\nI am enjoying\tPython\t\nUsing backslash\\ Hi I\'m Justwant')

#Old String Formatting
format_string = 'I am %s %s' %(first_name, last_name)
print(format_string)

libraries = ['Django', 'Flask', 'Pandas']
print('Some Libraries %s'%(libraries))

#New string Formatting
print('{} {}'.format(first_name,last_name))

a = 10
b = 20
print('{} + {} = {}'.format(a,b,a+b))

#f string python(3.6)
print(f'{a} + {b} = {a+b}')

language = 'Python'
first_letter = language[0]
print(first_letter)
last_index = len(language)-1
last_letter = language[last_index]

print(last_letter)

print(language[::-1])

challenge = 'thirty days of python'
print(challenge.capitalize())

print(challenge.count('y'))
print(challenge.endswith('on'))
print(challenge.expandtabs())

print(challenge.rfind('y'))

sub_string = 'da'

print(challenge.index(sub_string))

string_value = 'ThirtyDaysOfPython'
print(string_value.isalnum())

print(string_value.isdecimal())
print(string_value.isdigit())

print(string_value.islower())
print(string_value.isupper())

web_tech = ['HTML', 'CSS']
result = '# '.join(web_tech)
print(result)

print(challenge.strip('thon'))
print(challenge.replace('python', 'coding'))

print(challenge.split())
print(challenge.swapcase())