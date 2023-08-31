# Задание №3
# 📌 Доработаем задачу 2.
# 📌 Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

import logging
from functools import wraps

logging.basicConfig(filename='Log/log_3.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname:<6} - {asctime} в строке {lineno:>3d} функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def decor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'аргументы функции: {args}, результат функции: {result}')
        return result

    return wrapper


@decor
def power_х(x, y):
    return x ** y


print(power_х(2, 10))
print(power_х(5, 3))