def greetings (name = 'Justwant'):
    msg = name + ', welcome to Python for Everyone'
    return msg

print(greetings())
print(greetings('Ningthoujam'))

# def function_name(*args):
#     codes

# function_name(param1, param2)

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_all_nums(2,3,4))

def generate_groups (team, *args):
    print(team)
    for i in args:
        print(i)

print(generate_groups('Team-1', 'Ningthoujam', 'Justwant'))

def square_number (n):
    return n*n
def do_something(f, x):
    return f(x)

print(do_something(square_number, 3))