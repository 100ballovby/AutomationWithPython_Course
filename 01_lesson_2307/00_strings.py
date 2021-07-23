msg = input('Введите сообщение: ')
phone = ''
for symbol in msg:
    if symbol.isdigit():  # если символ - число
        phone += symbol  # я добавляю его в переменную
print(phone)

