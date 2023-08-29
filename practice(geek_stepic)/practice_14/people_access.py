MIN_LEVEL = 5


class BasedExep(Exception):
    pass


class LevelErr(BasedExep):
    def __init__(self, value, need_value):
        self.value = value
        self.need_value = need_value

    def __str__(self):
        return f"Ошибка уровня - level={self.value} меньше необходимого уровня)"


class AccessErr(BasedExep):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Ошибка доступа'


if __name__ == '__main__':
    try:
        num = int(input('введите целое число:> '))
        if num < 1:
            raise AccessErr(num)
        if num < MIN_LEVEL:
            raise LevelErr(num, MIN_LEVEL)
    except LevelErr as e:
        print(e)
    except AccessErr as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        print('Доступ разрешен')