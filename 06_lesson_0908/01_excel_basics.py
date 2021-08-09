import openpyxl as xl

wb = xl.load_workbook('example.xlsx')
print(type(wb))

print(wb.sheetnames)
# ^ получил имена всех листов

print(wb['Sheet2'])  # Обратиться к определенному листику

print(wb.active)  # получить активный лист
sheet = wb['Sheet1']
c4 = sheet['B3']
print(f'Строка "{c4.row}", Столбец "{c4.column}", Значение "{c4.value}"')
