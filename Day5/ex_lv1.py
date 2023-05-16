lst = list()

country = ['India', 'Sri Lanka', 'Bangladesh', 'China', 'Japan']
print(len(country))

last_index = len(country) - 1
middle_index = int(last_index/2)
print(f'{country[0]} {country[middle_index]} {country[last_index]}')

mixed_data_types = ['Justwant', 24, 180, 'Single', 'Palace Compound']
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))

last_idx = len(it_companies) - 1
middle_idx = int(last_idx/2)
print(f'{it_companies[0]} {it_companies[middle_idx]} {it_companies[last_idx]}')
it_companies.insert(middle_idx, 'TSP')
print(it_companies)

print(it_companies[0].upper())

print('#'.join(it_companies))
print('Apple' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[:3])
print(it_companies[-3:])
print(it_companies[middle_idx])
print(it_companies.pop(0))
print(it_companies.pop(middle_idx))
print(it_companies.pop(len(it_companies)-1))

it_companies.clear()
print(it_companies)
del it_companies
# print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

web_dev = front_end + back_end
print(web_dev)
full_stack = web_dev.copy()
print(full_stack)
full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)