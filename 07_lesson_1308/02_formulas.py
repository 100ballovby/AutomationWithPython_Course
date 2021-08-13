import openpyxl as xl

wb = xl.load_workbook('example.xlsx')  # открываю таблицу
sheet = wb['Sheet1']  # сохраняю рабочий лист

sheet['B8'] = 'Итог:'
sheet['C8'] = '=SUM(C1:C7)'

wb.save('formulas.xlsx')
