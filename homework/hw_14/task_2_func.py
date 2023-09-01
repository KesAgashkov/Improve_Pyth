import doctest
def dat(st: str):
    """
    Функция определяет является ли введенная дата корректной"
    :param st: str дата в формате (dd.mm.yyyy)
    :return: True or False
    >>> dat("25.04.2012")
    True
    >>> dat("29.02.2008")
    True
    >>> dat("32.04.2012")
    False
    >>> dat("25.13.2012")
    False
    >>> dat("32.04.-1245")
    False
    >>> dat("blabla")
    Traceback (most recent call last):
    ...
    ValueError
    """
    try:
        day, month, year = map(int, (st.split(".")))
    except ValueError:
        raise ValueError
    if year in range(1, 10000) and month in range(1, 13) and day in range(1, 32):
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 and month == 2:
            if day <= 29:
                return True
            else:
                return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day <= 31:
                return True
            else:
                return False
        elif month == 2:
            if day <= 28:
                return True
            else:
                return False
        else:
            if day <= 30:
                return True
            else:
                return False
    else:
        return False


if __name__ == '__main__':
    doctest.testmod(verbose=True)