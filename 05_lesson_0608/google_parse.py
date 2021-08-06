from bs4 import BeautifulSoup
import requests

url = 'https://www.google.com/search?q=купить+телефон'
connection = requests.get(url)  # подключаюсь к ссылке
parser = BeautifulSoup(connection.text, 'html.parser')

res = {}  # в словаре буду хранить ссылки
for name in parser.select('.vvjwJb'):
    print(name)
    res[name.text] = ''

print(res)


