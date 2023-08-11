"""
Задание №1
Создайте функцию-замыкание, которая запрашивает два целых
числа:
? от 1 до 100 для загадывания,
? от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""


def func_enigma(q_num, attempts):
    def attempts_count():
        nonlocal attempts
        while attempts > 0:
            num = int(input(f'Я загадал число от 1 до 100. Угадай:> '))
            if num == q_num:
                return "Угадал!"
            attempts -= 1
            print(f'осталось {attempts} попыток')
        return "Не угадал."

    return attempts_count


# res = func_enigma(15, 5)
#
# print(res())



"""
Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюу-угадайку
числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""


from random import randint


def func_enigma(func):
    def wrapper(q_num: int, attempts: int):
        q_num = q_num if 1 < q_num < 100 else randint(1, 100)
        attempts = attempts if 1 < attempts < 10 else randint(1, 10)
        #print(q_num, attempts)
        res = func(q_num, attempts)
        return res
    return wrapper

@func_enigma
def attempts_count(q_num, attempts):
    while attempts > 0:
        num = int(input(f'Я загадал число от 1 до 100. Угадай:> '))
        if num == q_num:
            return "Угадал!"
        attempts -= 1
        # if num < q_num:
        #     print('Больше!')
        # else:
        #     print('Меньше!')
        print(f'осталось {attempts} попыток')
    return "Не угадал."


# print(attempts_count(105, 25))


"""
Задание №3
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
"""


import json

def decor(func):
    write_dct = {}

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        filename = f'{func.__name__}.json'
        write_dct["arguments"] = f'{args[0]} , {args[1]}'
        for key, value in kwargs.items():
            write_dct[key] = value
        write_dct["result"] = result
        with open(filename, 'a', encoding="utf-8") as js_f:
            json.dump(write_dct, js_f, indent=2)
        return result

    return wrapper

@decor
def power_х(x, y):
    return x ** y


# print(power_х(2, 10))
# print(power_х(5, 3))



"""
Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""


def func(param):
    def deco(f):
        def wrapper(*args, **kwargs):
            count = 0
            for _ in range(param):
                res = f(args[0], args[1])
                count += 1
            return res, count

        return wrapper

    return deco

@func(10)
def summ(x, y):
    return x + y

#
# print(summ(2, 2))


"""
Задание №5
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
? декораторами для сохранения параметров,
? декоратором контроля значений и
? декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""


def deco_param(func):
    dct = {}

    def wrapper(*args, **kwargs):
        dct[args[0]] = args[1]
        res = func(args[0], args[1])
        return res, dct

    return wrapper


def func(param):
    def deco(f):
        def wrapper(*args, **kwargs):
            count = 0
            for _ in range(param):
                res = f(args[0], args[1])
                count += 1
            return res, count

        return wrapper

    return deco


@func(1)
@deco_param
def attempts_count(q_num, attempts):
    while attempts > 0:
        num = int(input(f'Я загадал число от 1 до 100. Угадай:> '))
        if num == q_num:
            return "Угадал!"
        attempts -= 1
        print(f'осталось {attempts} попыток')
    return "Не угадал."


# print(attempts_count(15, 2))


"""
Задание №6
Доработайте прошлую задачу добавив декоратор wraps в
каждый из декораторов.
"""

from functools import wraps


def deco_param(func):
    dct = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        dct[args[0]] = args[1]
        res = func(args[0], args[1])
        return res, dct

    return wrapper


def func(param):
    def deco(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            count = 0
            for _ in range(param):
                res = f(args[0], args[1])
                count += 1
            return res, count

        return wrapper

    return deco


@func(1)
@deco_param
def attempts_count(q_num, attempts):
    while attempts > 0:
        num = int(input(f'Я загадал число от 1 до 100. Угадай:> '))
        if num == q_num:
            return "Угадал!"
        attempts -= 1
        print(f'осталось {attempts} попыток')
    return "Не угадал."


#print(attempts_count(15, 2))
print(attempts_count.__name__)



class Log:

    def __init__(self, a):
        self.param = a
        """Класс-декоратор"""

    def __call__(self, func):
        def decorated(*args, **kwargs):
            """Обертка"""
            print(self.param)
            res = func(*args, **kwargs)
            print(f'log: {func.__name__}({args}, {kwargs}) = {res}')
            return res

        return decorated