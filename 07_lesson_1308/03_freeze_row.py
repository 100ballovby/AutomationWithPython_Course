import openpyxl as xl
from openpyxl.styles import Font

wb = xl.load_workbook('censuspopdata.xlsx')  # открываю таблицу
sheet = wb['Population by Census Tract']  # сохраняю рабочий лист
font_obj = Font(name='Calibri', size=24, italic=True, color='FF0000')
# ^ создал объект шрифта, который буду применять к ячейкам таблицы

for row in sheet['A1':'D1']:
    for cell in row:
        cell.font = font_obj
for col in 'ABCD':
    sheet.column_dimensions[col].width = 30  # ширина столбца
sheet.row_dimensions[1].height = 50  # высота строки
wb.save('new_styles.xlsx')


