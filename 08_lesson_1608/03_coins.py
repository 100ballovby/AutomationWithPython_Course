import json
import requests

url = 'https://api.coinbase.com/v2/currencies'
response = requests.get(url)
currencies = json.loads(response.text)

coin_db = {}

for cur in currencies['data']:
    #print(f'Код: {cur["id"]}, название: {cur["name"]}')
    coin_db[cur["id"]] = cur["name"]

with open('example.py', 'w', encoding='utf-8') as f:
    f.write('data = ' + str(coin_db))
