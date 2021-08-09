"""
Задача. Написать программу, которая:

1. Читать данные из таблицы;
2. Подсчитать количество районов, которые переписывали;
3. Считать численность населения в каждом округе;
4. Вывод результатов.

"""
import openpyxl as xl

wb = xl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census tract']
countryData = {}

# TODO: заполнить словарь данными о
#  численности населения и районах переписи

for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value


# TODO: создать текстовый файл и наполнить его
#  содержимым словаря countryData
