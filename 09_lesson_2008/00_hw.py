import requests
import json


def get_repos_from_github(username):
    """
    Функция подключается к гитхабу, находит полоьзователя и
    собирает все его репозитории в словарь.
    :param username: имя пользователя на github.com
    :return: возвращает словарь, где ключ - название репозитория, а значение - ссылка на него.
    """
    url = f'https://api.github.com/users/{username}/repos'
    res = requests.get(url)
    json_res = json.loads(res.text)

    repositories = {}

    for repo in json_res:
        repositories[repo['name']] = repo['svn_url']

    return repositories

sto_ballov = get_repos_from_github('100ballovby')
print(sto_ballov)

