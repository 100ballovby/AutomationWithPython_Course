'''
Словарь - это набор пар ключ-значение.
'''
import requests

products = {
    'Ham': 2.99, 
    'Egg': 3,
    'Cookie': 4.5,
    'Banana': 0.99,
}

for product in products:
    print(product)

print(products['Banana'])
products['Banana'] = 1.56  # обновить значение ключа

for prod, price in products.items():  # метод items() забирает из словаря и ключи, и значения
    print(f'Product: {prod}\nPrice: {price}')






