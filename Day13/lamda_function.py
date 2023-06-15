# x = lambda param1, param2: param1 + param2

# print(x(arg1, arg2, arg3))

def add_two_number(a,b):
    return a+b

add_two_number = lambda a,b: a+b
print(add_two_number(10,20))

def square_of_number(a,b):
    return a ** b

square_of_number = lambda a,b: a**b
print(square_of_number(2,3))

def divide(a):
    return lambda b: a/b

value = divide(20)(2)
print(divide)