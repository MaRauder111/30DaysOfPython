tup = tuple()
t1 = ()

print(tup, t1)

brother = ('Ningthoujam', 'Tomchw')
sister = ('Devi', 'Tombi')

sib = brother + sister
print(sib)
print(f'I have {len(sib)} siblings')

family_members = sib + ('Father', 'Mother')
print(family_members)

print(family_members[:4])
print(family_members[-2:])

fruits = ('banana', 'apple', 'orange')
vegetables = ('mustard', 'peas', 'onion')
animal = ('cat', 'dog', 'cow')

food_stuff_tp = fruits + vegetables + animal

print(food_stuff_tp)

food_stuff_ls = list(food_stuff_tp)

print(food_stuff_ls)

middle_term = int(len(food_stuff_ls)/2)
print(middle_term)

print(food_stuff_ls[middle_term])
print(food_stuff_ls[:3])
print(food_stuff_ls[-3:])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)