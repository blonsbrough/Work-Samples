import requests

url = 'https://static.webucator.com/media/public/documents/hrleaders.json'
r = requests.get(url)
records = r.json()
def main():
    #Phrase primary request
    for i, record in enumerate(records,1):
        player = record['Player']
        hr = record['HR']
        year = record['Year']
        print(f'{i}. {player} hit {hr} home runs in {year}')



main()