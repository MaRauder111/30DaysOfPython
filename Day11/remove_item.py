def remove_item(food_staff, item):
    food_staff.remove(item)
    return food_staff

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 7))