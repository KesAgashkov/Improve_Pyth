# Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
# 2-5 тестов на задание в трёх вариантах:
# doctest,
# unittest,
# pytest
import doctest


def horse_move(fir: int, sec: int) -> [[str]]:
    """
    Функция принимает две координаты на шахматной доске 8 x 8, и обозначает на доске положение коня 'H'
    и его возможные ходы '*'
    Параметры:
                fir(int) - ось x от 1 до 8 (соответствие буквам)
                fir(int) - ось y от 1 до 8 (соответствие цифрам) нумерация снизу вверх
    Возвращаемое значение:
                [[str]] - матрица 8x8 c положением коня и возможными ходами

    >>> horse_move('dsds',8)
    Traceback (most recent call last):
    ...
    TypeError: can only concatenate str (not "int") to str
    >>> horse_move(7,'dsds')
    Traceback (most recent call last):
    ...
    TypeError: can only concatenate str (not "int") to str
    >>> horse_move(None,8)
    Traceback (most recent call last):
    ...
    TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
    >>> horse_move(9,8)
    Выход за пределы доски
    []
    >>> horse_move(3,10)
    Выход за пределы доски
    []
    >>> horse_move(4,4)
    [['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '*', '.', '*', '.', '.', '.'], ['.', '*', '.', '.', '.', '*', '.', '.'], ['.', '.', '.', 'H', '.', '.', '.', '.'], ['.', '*', '.', '.', '.', '*', '.', '.'], ['.', '.', '*', '.', '*', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']]
    """

    try:
        fir = int(fir)
        sec = int(sec)
        if fir > 8 or sec > 8:
            print("Выход за пределы доски")
            return []
    except ValueError as e:
        print(e)
    y = fir+1
    x = sec+2
    board = [["." for i in range(12)] for j in range(12)]
    res = []
    temp = []
    for i in range(10, 2, -1):
        for j in range(2, 10):
            if x == i and y == j:
                board[i][j] = "H"
            elif ((x - i) ** 2 + (y - j) ** 2) == 5:
                board[i][j] = "*"
    for i in range(10,2,-1):
        for j in range(2,10):
            temp.append(board[i][j])
        res.append(temp)
        temp = []
    return res

# print(*horse_move(4,4),sep="\n")
new = horse_move(4,4)
# new[0][0] = "F"
# print(*new,sep="\n")
# print(horse_move(5,8) == new)

if __name__ == '__main__':
    doctest.testmod(verbose=True)
