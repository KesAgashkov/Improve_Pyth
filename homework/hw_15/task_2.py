import logging
import argparse

logging.basicConfig(filename='log_task_2.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname:<6} - {asctime} в модуле {module} функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def dat(st: str):
    """
    Функция определяет является ли введенная дата корректной"
    :param st: str дата в формате (dd.mm.yyyy)
    :return: True or False
    """
    try:
        day, month, year = map(int, (st.split(".")))
        logger.info("Валидация параметра прошла успешно")
    except ValueError:
        logger.error("Ошибка валидации")
        raise ValueError
    if year in range(1, 10000) and month in range(1, 13) and day in range(1, 32):
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 and month == 2:
            if day <= 29:
                logger.info(f"Дата {day}.{month}.{year} существует")
                return True
            else:
                logger.info(f"Дата {day}.{month}.{year} не существует")
                return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day <= 31:
                logger.info(f"Дата {day}.{month}.{year} существует")
                return True
            else:
                logger.info(f"Дата {day}.{month}.{year} не существует")
                return False
        elif month == 2:
            if day <= 28:
                logger.info(f"Дата {day}.{month}.{year} существует")
                return True
            else:
                logger.info(f"Дата {day}.{month}.{year} не существует")
                return False
        else:
            if day <= 30:
                logger.info(f"Дата {day}.{month}.{year} существует")
                return True
            else:
                logger.info(f"Дата {day}.{month}.{year} не существует")
                return False
    else:
        logger.info(f"Дата {day}.{month}.{year} не существует")
        return False


parser = argparse.ArgumentParser(description=dat.__doc__)
parser.add_argument('-inp', type=str, default="01.01.2000")
args = parser.parse_args()

print(dat(args.inp))
