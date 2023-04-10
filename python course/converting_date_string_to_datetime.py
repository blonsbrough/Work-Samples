import datetime

def str_to_date(str_date):
    # Write function
    datestr = str_date.split(sep = '-')
    dateint = [int(i) for i in datestr]
    date = datetime.date(*dateint)
    return date

str_date = input('Input date as YYYY-MM-DD: ')
date = str_to_date(str_date)
print(date)

