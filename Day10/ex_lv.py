for i in range(11):
    print(i)

count = 0
while count < 11:
    print(count)
    count += 1

for i in range(10,-1,-1):
    print(i)

count = 10
while count > -1:
    print(f'While loop {count}')
    count -= 1

hash = '#'
for i in range(1,8):
    print(hash * i)

for i in range(1,9):
    for j in range(1,9):
        print(f'{hash}', end=' ')
    print()

for i in range(11):
    print(f'{i} * {i} = {i*i}')

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in lst:
    print(i)

for i in range(101):
    if i%2 == 0:
        print(f'Even number {i}')
    elif i%2 == 1:
        print(f'Odd number {i}')

number = 0
for i in range(101):
    number += i
print(f'The sum of all numbers is {number}')

even_sum = 0
odd_sum = 0
for i in range(101):
    if i %2 == 0:
        even_sum += i
    elif i%2 == 1:
        odd_sum += i

print(f'The sum of all even number is {even_sum}')
print(f'The sum of all odd number is {odd_sum}')