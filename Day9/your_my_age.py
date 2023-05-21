
my_age = 26
your_age = int(input('Enter your age '))

if your_age > my_age:
    print(f'You are {your_age-my_age} years older than me.')
elif your_age < my_age:
    print(f'You are {my_age-your_age} years younger than me')
else:
    print(f'Same age')