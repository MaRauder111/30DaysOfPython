first = 'Thirty'
second = 'Days'
third = 'of'
forth = 'Python'

result = first + second + third + forth
print(f'{result}')

fifth = 'Coding'
sixth = 'For'
seventh = 'All'

concatenate = fifth + sixth + seventh
print(f'{concatenate}')

company = 'Coding for All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[1:])

string_value = 'Coding For All'
print(string_value.find('Coding'))

print(string_value.replace('Coding', 'Python'))

challenge = 'Python for Everyone'
print(challenge.replace('Everyone', 'All'))

print(challenge.split())

challenge_value = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(challenge_value.split(','))

print(string_value[0])
len_val = len(string_value) - 1
print(len_val)
print(string_value[len_val])

print(string_value[10])

acronym_1 = 'Python For Everyone'

first_val = acronym_1[0]
index = acronym_1[7]
last_val = acronym_1[11]

print(f'{first_val}{index}{last_val}')

acronym_2 = 'Coding For All'

first_ = acronym_2[0]
middle_ = acronym_2[7]
last_ = acronym_2[11]

print(f'{first_}{middle_}{last_}')

print(acronym_2.index('C'))
print(acronym_2.index('F'))

print(acronym_2.rfind('l'))

value = 'You cannot end a sentence with because because because is a conjunction'
print(value.index('because'))

print(value.rfind('because'))

print(value[31:54])

substring_check = 'Coding For All'
substring = 'Coding'
print(substring_check.startswith(substring))
print(substring_check.endswith('coding'))

remove_space = '   Coding For All      '
print(remove_space.strip('  '))

checking_value = '30DaysOfPython'
checking_value_1 = 'thirty_days_of_python'
print(checking_value.isidentifier())
print(checking_value_1.isidentifier())

val = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(val))

print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

radius = 10
pie = 3.14
area = pie * radius ** 2
print('radius = {}'.format(radius))
print('area = {} * {} ** 2'.format(pie,radius))
print('The area of a circle with radius {} is {} meters square.'.format(radius,area))

print('{} + {} = {}'.format(8, 6, 14))
print('{} - {} = {}'.format(8,6,2))
