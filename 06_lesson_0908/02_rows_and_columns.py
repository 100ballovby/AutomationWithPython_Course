import openpyxl as xl

wb = xl.load_workbook('example.xlsx')
# Получение строк и столбцов с листа

sheet = wb['Sheet1']  # Хочу просмотреть 1 лист

for row in sheet['A1':'C4']:
    # ^ для каждой строки в диапазоне от А1 до С7
    for cell in row:
        # ^ для каждой ячейки в строке
        print(cell.coordinate, cell.value)
    print('---end of the row---')

for text in sheet['B']:
    print(text.value)

