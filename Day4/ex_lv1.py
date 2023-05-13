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