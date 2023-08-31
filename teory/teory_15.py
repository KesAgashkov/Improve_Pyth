import logging

# logging.basicConfig(level=logging.CRITICAL)
# logger = logging.getLogger(__name__)
# logger.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
# logger.info('Немного информации о работе кода')
# logger.warning('Внимание! Надвигается буря!')
# logger.error('Поймали ошибку. Дальше только неизвестность')
# logger.critical('На этом всё')


from log_all import log_all

# logging.basicConfig(filename='project.log.', filemode='w', encoding='utf-8', level=logging.INFO)
# logger = logging.getLogger('Основной файл проекта')
# logger.warning('Внимание! Используем вызов функции из другого модуля')
# log_all()


# FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
# 'в строке {lineno:03d} функция "{funcName}()" ' \
# 'в {created} секунд записала сообщение: {msg}'
# logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
# logger = logging.getLogger('main')
# logger.warning('Внимание! Используем вызов функции из другого модуля')
# log_all()


from datetime import time, date, datetime

d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, second=0, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
              second=0, microsecond=24)
print(f'{d = }\t-\t{d}')
print(f'{t = }\t-\t{t}')
print(f'{dt = }\t-\t{dt}')

from datetime import timedelta

delta = timedelta(weeks=1, days=2, hours=3, minutes=4, seconds=5,
                  milliseconds=6, microseconds=7)
print(f'{delta = }\t-\t{delta}')


from datetime import datetime, timedelta

date_1 = datetime(2012, 12, 21)
date_2 = datetime(2017, 8, 19)
delta = date_2 - date_1
print(f'{delta = }\t-\t{delta}')
birthday = datetime(1503, 12, 14)
dlt = timedelta(days=365.25 * 33)
new_date = birthday + dlt
print(f'{new_date = }\t-\t{new_date}')


from datetime import time, date, datetime, timedelta
d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)
delta = timedelta(weeks=53, hours=73, minutes=101, seconds=303, milliseconds=60)
print(f'{d.month}')
print(f'{t.second}')
print(f'{dt.hour}')
print(f'{delta.days}')

from datetime import time, date, datetime, timedelta
t = time(hour=2, minute=14, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)
new_dt = dt.replace(year=2012)
one_more_hour = t.replace(t.hour + 1)
print(f'{new_dt}\n{one_more_hour}')


dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
microsecond=24)
print(dt)
print(dt.timestamp())
print(dt.isoformat())
print(dt.weekday())
print(dt.strftime('Дата %d %B %Y День недели %A. Время %H:%M:%S.Это %W неделя и %j день года.'))



date_original = '2022-12-12 18:01:21.555470'
date_timestamp = 1181862840.000024
date_iso = '2007-06-15T02:14:00.000024'
date_text = 'Дата 15 June 2007. День недели Friday. Время 02:14:00. Это 24 неделя и 166 день года.'

original_date = datetime.fromisoformat(date_original)
timestamp_date = datetime.fromtimestamp(date_timestamp)
iso_date = datetime.fromisoformat(date_iso)
text_date = datetime.strptime(date_text, 'Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.')
print(original_date)
print(timestamp_date)
print(iso_date)
print(text_date)


import argparse
def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Solving quadratic equations')
#     parser.add_argument('param', metavar='a b c', type=float, nargs=3, help='enter a b c separated by a space')
#     args = parser.parse_args()
#     print(quadratic_equations(*args.param))
#
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solvingquadratic equations')
    parser.add_argument('-a', metavar='a', type=float, help='enter a for ax^2+bx+c=0', default=1)
    parser.add_argument('-b', metavar='b', type=float, help='enter b for ax^2+bx+c=0', default=0)
    parser.add_argument('-c', metavar='c', type=float, help='enter c for ax^2+bx+c=0', default=0)
    args = parser.parse_args()
    print(quadratic_equations(args.a, args.b, args.c))
