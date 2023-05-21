month = input('Enter a month: ')

if month == 'September' or month == 'October' or month == 'November':
    print('Season is Autumn')
elif month == 'December' or month == 'January' or month == 'February':
    print('Season is Winter')
elif month == 'March' or month == 'April' or month == 'May':
    print('Season is Spring')
elif month == 'June' or month == 'July' or month == 'August':
    print('Season is Summer')
else:
    print('Enter a valid month')