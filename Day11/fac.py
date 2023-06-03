# def factorial(fac):
#     fact = 1
#     for i in range(fac + 1):
#         fact *= i
#     return fact

def factorial(n):
    i = 1
    fac = 1
    while(i <= n):
        fac *= i
        i += 1
    return fac

print(factorial(3))