"""
Задача. Написать программу, которая:

1. Читать данные из таблицы;
2. Подсчитать количество районов, которые переписывали;
3. Считать численность населения в каждом округе;
4. Вывод результатов.

"""
import openpyxl as xl
import pprint  # perfect print

wb = xl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countryData = {}

for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Гарантированный ключ для штата
    countryData.setdefault(state, {})
    # Гарантированный ключ для округа
    countryData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    # Каждая строка - это отдельный округ. Поэтому я буду увеличивать их на 1
    countryData[state][county]['tracts'] += 1
    countryData[state][county]['pop'] += int(pop)

# TODO: создать текстовый файл и наполнить его
#  содержимым словаря countryData

resFile = open('USAcensus.py', 'w')
resFile.write('pop_data = ' + pprint.pformat(countryData))
resFile.close()
print('Done!')