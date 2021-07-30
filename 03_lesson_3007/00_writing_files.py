'''
1. Открыть
2. Прочитать
3. Закрыть

Режимы работы с файлами
1. w - write
2. r - read
3. a - добавить
'''
with open('example.txt', 'r') as f:
    # открыть файл example.txt в режиме чтения и присвоить его переменной f
    lines = f.readlines()
    print(f'В файле {len(lines)} строк. {lines}')

# запись в файл
with open('example.txt', 'w') as f:
    # открыть файл example.txt в режиме записи и присвоить его переменной f
    f.writelines('Hello\nMy name is Demid\nI love programming')

# запись в файл БЕЗ удаления предыдущего содержимого
with open('example.txt', 'a') as f:
    # открыть файл example.txt в режиме добавления и присвоить его переменной f
    f.writelines('\nЯ добавил строчку\nИ вот эту тоже')
