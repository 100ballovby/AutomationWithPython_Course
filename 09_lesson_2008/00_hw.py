import requests
import json

url = 'https://api.github.com/users/100ballovby/repos'
res = requests.get(url)
print(res.text)
