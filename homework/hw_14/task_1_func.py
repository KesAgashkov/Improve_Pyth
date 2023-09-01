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
            return f"Выход за пределы доски"
    except ValueError:
        raise ValueError
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