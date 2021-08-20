import time

print('Чтобы начать отсчет, нажмите Enter. Для выхода нажмите Ctrl + C')
input()  # нажатие Enter будет запускать программу

print('Отсчет начат.')
start = time.time()
last_time = start
lap = 1

try:
    while True:
        input()  # если нажали Enter
        lap_time = round(time.time() - last_time, 4)
        total_time = round(time.time() - start, 4)
        print(f'Круг: {lap},\nВремя круга: {lap_time},\nОбщее время {total_time}')
        lap += 1
        last_time = time.time()

except KeyboardInterrupt:  # Ловит сочетание Ctr+C и останавливает программу
    print('Готово')

