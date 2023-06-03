import math
def solve_quadratic_eqn(a,b,c):
    x = (-b + math.sqrt((b**2) - (4 *a*c)))/2*a
    x_negative = (-b - math.sqrt((b**2) - (4 *a*c)))/2*a
    first = (a * x**2) + (b * x) + c
    second = (a * x_negative**2) + (b * x_negative) + c

    return second
print(solve_quadratic_eqn(2,-1,-1))