def say_hello(name):
    print(f'Привет, {name}!')


def clear_number(r_phone):
    phone = ''
    for symbol in r_phone:
        if symbol.isdigit():  # если символ - число
            phone += symbol  # я добавляю его в переменную
    print(phone)

clear_number('+375(29)1235674')
clear_number('+375 33 5667-34-1')
clear_number('+375 (33) - 367-12 98')
