lst = list()

empty_list = list()
print(len(empty_list))

fruits = ['banana', 'orange', 'mango', 'lemon']

print('Fruits: {}'.format(fruits))
print(f'{len(fruits)}')

lst_val = ['Ningthoujam', 200, {'country': 'India', 'age': 24}]

print(lst_val)

print(fruits[-1])

first_item, second_item, *rest = fruits
print(f'{first_item}, {second_item}, {rest}')

print(fruits[0:2])
print(fruits[0:])
print(fruits[::3])

print(fruits[-3:-1])
print(fruits[-3:])
print(fruits[::-1])

does_exist = 'banana' in fruits
print(does_exist)

lst.append('Value')
print(lst)

fruits.insert(2,'Watermelon')
print(fruits)

fruits.remove('banana')
print(fruits)

fruits.pop()
print(fruits)

del lst[0]
print(lst)

# fruits.clear()
# print(fruits)

lst = fruits.copy()

print(lst)

print(f'{lst + lst}')
list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)
print(f'{list1}')

print(list1.count(1))
print(fruits.index('orange'))
print(list1.index(3))
fruits.reverse()
print(fruits)

list1.sort(reverse=True)
print(list1)

print(sorted(fruits))