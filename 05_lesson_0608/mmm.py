from bs4 import BeautifulSoup
import requests

res = requests.get('https://100ballov.by/minsk')
print(res.status_code)

