import re


def check_email(email):
    domains = ['@gmail.com',
               '@yandex.ru',
               '@mail.ru',
               '@icloud.com']
    emailRegex = re.compile(r'@\w+.\w+')
    search = emailRegex.search(email)
    print(search.group())
    if search.group() in domains:
        print('Ок')
    else:
        print('Такой домен не существует!')


check_email('Мой имейл это: emai@chotomail.com, держи')
check_email('Мой имейл это: emai@protonmail.com, держи')
check_email('Мой имейл это: emai@yandex.ru, держи')

