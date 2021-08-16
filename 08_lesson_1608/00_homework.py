import openpyxl as xl

wb = xl.load_workbook('freezeExample.xlsx')  # открываю таблицу
sheet = wb['Sheet']  # сохраняю рабочий лист

for row in range(2, sheet.max_row + 1):
    sheet[f'D{row}'].value = f'=ROUND(B{row} * C{row}, 2)'

wb.save('result.xlsx')
