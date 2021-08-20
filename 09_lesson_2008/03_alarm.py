from datetime import datetime
import platform
try:
    import winsound  # для windows
except:
    import os  # для остальных систем


def alarm(wake_date):
    now = datetime.now()
    #alarm_time = datetime(now.year, now.month, day, hour, minute)
    alarm_time = datetime.strptime(wake_date, '%d/%m/%Y, %H:%M')
    # собираю дату пробуждения из строчки: 21/08/2021, 07:49
    while now < alarm_time:
        now = datetime.now()

    for i in range(3):
        if platform.system() == 'Windows':
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)  # частота 5000 Гц, продолжительность 1000 мс = 1с
        elif platform.system() == 'Darwin':
            os.system('say wake up')
        elif platform.system() == 'Linux':
            os.system('beep -f 5000')

alarm('20/08/2021, 12:50')
