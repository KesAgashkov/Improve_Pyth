import math


# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

# Задание 1
class NotHashable(Exception):

    def __str__(self):
        return f'Ошибка. Ключ невозможно хэшировать, ключ конвертируется в строковое представление'


def get_dict(**kwargs) -> dict:
    dct = dict()
    for key, el in kwargs.items():
        try:
            try:
                dct[el] = key
            except:
                print(el, end=": ")
                raise NotHashable
        except NotHashable as h:
            print(h)
            dct[str(el)] = key
    return dct


# tup = (13, 16, 8, 9, 78)
# lst2 = [13, 16, 8, 9, 78]
#
# print(get_dict(a = [], b = 15, c = 30, d = {}))


# Задание 2
class ErrorConvert(Exception):
    def __str__(self):
        return f'Ошибка преобразования данных в тип INT'


class Limit(Exception):
    DOWN = 1
    UP = 1000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Функция может принимать значения от {self.DOWN} до {self.UP}\nВы ввели {self.a, self.b, self.c}'


def solve_quad_equation(a: int, b: int, c: int):
    try:
        try:
            a = int(a)
            b = int(b)
            c = int(c)
        except:
            raise ErrorConvert
        if Limit.DOWN <= a <= Limit.UP and Limit.DOWN <= b <= Limit.UP and Limit.DOWN <= c <= Limit.UP:
            pass
        else:
            raise Limit(a, b, c)
    except ErrorConvert as er:
        print(er)
        exit()
    except Limit as l:
        print(l)
        exit()
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("Решение уравнения есть в комплексных числах")
        base = round(-b / (2 * a), 4)
        last = round(math.sqrt(abs(d)) / (2 * a), 4)
        print(f"x1 = {complex(base, last)}, x2 = {complex(base, -last)}")
    elif d > 0:
        print("Уравнение имеет два корня")
        print(f"x1 = {round((-b - math.sqrt(d)) / (2 * a), 3)} ; x2 = {round((-b + math.sqrt(d)) / (2 * a), 3)} ")
    else:
        print("Уравнение имеет один корень")
        print(f"x = {-b / 2 * a}")


# solve_quad_equation(4,4.4,1011)
