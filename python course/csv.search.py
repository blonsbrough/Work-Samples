import csv

def get_data_as_list(csvfile):
    with open(csvfile, newline = '', encoding = "utf-8") as csvfile:
        data = csv.DictReader(csvfile)
        return list(data)

def getpop(data, state, year):
    for row in data:
        if row['State'] == state:
            return row[year]
    else:
        print('state not found')

def main():
    data = get_data_as_list('working-with-data\data\population-by-state.csv')
    state = input('Input state name: ')
    year = input('Input year: ')
    if int(year) in list(range(2010,2021)):
        pop = getpop(data, state, year)
        if pop:
            print(f'{state}\'s population in {year}: {pop}')
        

        else:
            print(f'state {state} not found')
    else:
        print(f'year: {year} out of data range')


main()