def check_season(month):
    if month == 'September' or month == 'October' or month == 'November':
        return 'Autumn'
    elif month == 'December' or month == 'January' or month == 'February':
        return 'Winter'
    elif month == 'March' or month == 'April' or month == 'May':
        return 'Spring'
    elif month == 'June' or month == 'July' or month == 'August':
        return 'Summer'
    else:
        return 'Enter a valid month'

month = input('Enter a month ')
print(check_season(month))