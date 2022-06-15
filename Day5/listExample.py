# using built in function
lst = list()

empty_list = list()

print(len(empty_list))

# using square bracket []
fruit = ['banana','orange','mango']

print(f'{fruit}')

print(f'{fruit[0]}')

print(f'{fruit[-1]}')

lst1 = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst1

print(first_item)