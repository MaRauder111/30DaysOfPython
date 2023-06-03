def generate_full_name():
    first_name = 'Ningthoujam'
    last_name = 'Justwant'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)

generate_full_name()

def sum_of_two_number():
    first = 10
    second = 20
    sum = first + second
    return sum

print(sum_of_two_number())

def add_ten(num):
    ten = 10
    return num + ten

print(add_ten(1))

def add(num_one, num_two):
    sum = num_one + num_two
    return sum

print(add(10,20))
print(add(num_one=30,num_two=40))

def print_first_name(first_name):
    return first_name

print(print_first_name('Justwant'))

def even_odd(num):
    if num % 2 == 0:
        print('even')
        return True
    else:
        print('odd')
        return False

print(even_odd(10))
print(even_odd(9))