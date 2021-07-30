import requests
# подключаю библиотеку с запросами к проекту

url = 'https://dominos.by/pizza'
# ссылка, к которой я буду подключаться

print(requests.get(url))  # метод get посылает запрос и возвращает результат подключения

with open('dominos.html', 'w') as f:
    # если файла с таким именем нет, он создастся автоматически
    response = requests.get(url)
    f.write(response.text)

