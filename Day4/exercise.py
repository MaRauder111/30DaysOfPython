from operator import index
from traceback import print_tb


string_one = 'Thirty'
string_two = 'Days'
string_three = 'Of'
string_four = 'Python'

print(f'Concatenation of strings is {string_one} {string_two} {string_three} {string_four}')

string_five = 'Coding'
string_six = 'For'
string_seven = 'All'

string_all = string_five + string_six + string_seven

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[0:6])
company_new = company.replace('Coding For All','Python')
print(company_new)

new_string = 'Python for Everyone'
print(new_string)
new_string_update = new_string.replace('Everyone', 'All')
print(new_string_update)

string_value = 'Coding for All'
print(string_value.split())

string_value_one = 'Facebook, Amazon, IBM, Apple, Oracle'
print(string_value_one.split(', '))

string_eight = 'Coding For All People'
print(string_eight[0])

print(len(string_eight))
print(string_eight[10])

print(string_eight.find('C'))
print(string_eight.find('F'))

print(string_eight.rfind('l'))

string_nine = 'You cannot end a sentence with because because because is a conjunction'
print(string_nine.find('because'))
print(string_nine.rfind('because'))

print(string_nine[31:54])

sub_string = 'Coding'
print(string_eight.startswith(sub_string))
print(string_eight.endswith('coding'))

string_ten = '   Coding For All      '
print(string_ten)
print(string_ten.strip(' '))

string_eleven = '30DaysOfPython'
print(string_eleven.isidentifier())

string_tweleve = 'thirty_days_of_python'
print(string_tweleve.isidentifier())

string_thirteen = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

print('#'.join(string_thirteen))

print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\t\tCity\nAsabeneh\t250\tFinland\t\tHelsinki')

radius = int(10)
area = 3.14 * radius ** 2
print('radius = %s' %(radius))
print('area = {} * radius ** {}'.format(radius,area))
print(f'The area of a circle with radius {radius} is {area} meters')

print(f'8 + 6 = ')