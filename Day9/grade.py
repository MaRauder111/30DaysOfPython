mark = int(input('Enter your mark: '))

if mark >= 0 and mark <= 49:
    print('Your grade is F')
elif mark >= 50 and mark <= 59:
    print('Your grade is D')
elif mark >= 60 and mark <= 69:
    print('Your grade is C')
elif mark >= 70 and mark <= 89:
    print('Your grade is B')
elif mark >= 80 and mark <= 100:
    print('Your grade is A')

else:
    print('Enter a valid mark between 0-100')