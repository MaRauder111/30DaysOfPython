empty_tuple = tuple()
tup = ()

tp1 = ('item1', 'item2')

fruits = ('banana', 'orange', 'mango', 'lemon')
print(len(fruits))

print(fruits[0])

last_fruit = fruits[-1]
print(last_fruit)
print(fruits[:2])
print(fruits[-3:])

lst = list(fruits)
print(lst)
print('lemon' in fruits)

tp2 = ('item3', 'item4')

tp1 = tp1 + tp2
print(tp1)

del tp1