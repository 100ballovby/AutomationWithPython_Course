import json
import requests

url = 'https://api.github.com/users/100ballovby/repos'
response = requests.get(url)
print(json.loads(response.text))
