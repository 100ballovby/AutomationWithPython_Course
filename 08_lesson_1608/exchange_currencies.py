import json

import exchange as exchange
import requests


def exchanger(amount, currency):
    url = 'https://api.coinbase.com/v2/exchange-rates'
    response = requests.get(url)
    currencies = json.loads(response.text)
    rate = float(currencies['data']['rates'][currency])

    res = rate * amount
    return res

print(exchanger(2456.45, 'BYN'))
