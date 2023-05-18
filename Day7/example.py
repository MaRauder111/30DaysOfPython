st = set()

st1 = {}

print(st, st1)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))

print('mango' in fruits)

fruits.add('lime')
print(fruits)

vegetables = {'tomato', 'potato', 'cabbage'}
print(vegetables)

fruits.update(vegetables)

print(fruits)
fruits.remove('mango')
fruits.pop()
print(fruits)
# fruits.clear()
print(fruits)
# del fruits

lst = list(vegetables)

print(lst)

print(fruits.union(vegetables))
print(fruits.intersection(vegetables))

st2 = {'item1', 'item2', 'item3'}
st3 = {'item2', 'item3'}
print(st3.issubset(st2))
print(st2.issuperset(st1))

print(st2.difference(st3))
print(st2.symmetric_difference(st3))
print(st2.isdisjoint(st1))