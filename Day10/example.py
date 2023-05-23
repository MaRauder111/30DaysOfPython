# while condition:
#     code goes here

# count = 0

# while count < 5:
#     print(count)
#     count += 1
#     if count == 3:
#         break

# else:
#     print(count)

# BUG
# count = 3
# while count < 5:
#     if count == 3:
#         continue
#     print(count)
#     count = count + 1
#     break

numbers = [0,1,2,3,4,5]
for number in numbers:
    print(number)

language = 'Python'

for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    },
    'number': [1, 2, 3, 4, 5, 6]
}

for i in person:
    print(i)

for key, value in person.items():
    print(key,value)

for i in numbers:
    print(i)
    if numbers[i] == 3:
        break

for i in numbers:
    print(i)
    if numbers[i] == 3:
        continue
    print('Hello')

lst = list(range(11))
print(lst)

st = set(range(1,5))
print(st)

lst = list(range(0,11,3))
print(lst)

for number in range(11):
    print(number)

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

for key in person:
    if key == 'number':
        for value in person['number']:
            print(value)

for number in range(11):
    print(number)
else:
    print(f'The loop stop at number {number}')

for number in range(5):
    pass