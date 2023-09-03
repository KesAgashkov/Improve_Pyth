# Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.
import logging
import argparse

logging.basicConfig(filename='log_task_1.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname:<6} - {asctime} в модуле {module} функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def horse_move(fir: int, sec: int) -> [[str]]:
    """
    Функция принимает две координаты на шахматной доске 8 x 8, и обозначает на доске положение коня 'H'
    и его возможные ходы '*'
    Параметры:
                fir(int) - ось x от 1 до 8 (соответствие буквам)
                fir(int) - ось y от 1 до 8 (соответствие цифрам) нумерация снизу вверх
    Возвращаемое значение:
                [[str]] - матрица 8x8 c положением коня и возможными ходами
    """
    try:
        fir = int(fir)
        sec = int(sec)
        if fir > 8 or sec > 8:
            logging.warning("Введнные координаты за пределами доски")
            return f"Выход за пределы доски"
    except ValueError:
        logging.error("Невозможно привести введённое значение к int")
    y = fir + 1
    x = sec + 2
    board = [["." for i in range(12)] for j in range(12)]
    res = []
    temp = []
    for i in range(10, 2, -1):
        for j in range(2, 10):
            if x == i and y == j:
                board[i][j] = "H"
            elif ((x - i) ** 2 + (y - j) ** 2) == 5:
                board[i][j] = "*"
    for i in range(10, 2, -1):
        for j in range(2, 10):
            temp.append(board[i][j])
        res.append(temp)
        temp = []
    logging.info(f"Вычисления с координатами коня {fir, sec} прошли успешно")
    for el in res:
        print(*el)
    return res


parser = argparse.ArgumentParser(description=horse_move.__doc__)
parser.add_argument('-fir', type=int, default=4)
parser.add_argument('-sec', type=int, default=4)
args = parser.parse_args()

horse_move(args.fir, args.sec)
