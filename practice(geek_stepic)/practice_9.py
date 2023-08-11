"""
������� �1
�������� �������-���������, ������� ����������� ��� �����
�����:
? �� 1 �� 100 ��� �����������,
? �� 1 �� 10 ��� ���������� �������
������� ���������� �������, ������� ����� ������� ������
������� ���������� ����� �� ��������� ����� �������.
"""


def func_enigma(q_num, attempts):
    def attempts_count():
        nonlocal attempts
        while attempts > 0:
            num = int(input(f'� ������� ����� �� 1 �� 100. ������:> '))
            if num == q_num:
                return "������!"
            attempts -= 1
            print(f'�������� {attempts} �������')
        return "�� ������."

    return attempts_count


# res = func_enigma(15, 5)
#
# print(res())



"""
������� �2
������������ ������ 1.
���������� ������� ������� � ���������.
�� ������ ��������� ������ �� ���������� � ��������-��������
����� � ��������� [1, 100] � [1, 10].
���� �� ������, �������� ������� �� ���������� �������
�� ����������.
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
        num = int(input(f'� ������� ����� �� 1 �� 100. ������:> '))
        if num == q_num:
            return "������!"
        attempts -= 1
        # if num < q_num:
        #     print('������!')
        # else:
        #     print('������!')
        print(f'�������� {attempts} �������')
    return "�� ������."


# print(attempts_count(105, 25))


"""
������� �3
�������� ���������, ������� ��������� � json ����
��������� ������������ ������� � ���������, ������� ���
����������. ��� ��������� ������ ���� ������
�����������, � �� ����������������.
������ �������� �������� ��������� ��� ��������� ����
json �������.
��� ������������� �������� �������, ������� �����
��������� ��� �����������, ��� � �������� ���������.
��� ����� ������ ��������� � ������ ������������
�������.
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
def power_�(x, y):
    return x ** y


# print(power_�(2, 10))
# print(power_�(5, 3))



"""
������� �4
�������� ��������� � ����������.
�������� - ����� �����, ���������� �������� ������������
�������.
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
������� �5
���������� ������� �� ������� �����.
������� �������� �������������:
? ������������ ��� ���������� ����������,
? ����������� �������� �������� �
? ����������� ��� ������������� �������.
�������� ������ ������� �����������.
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
        num = int(input(f'� ������� ����� �� 1 �� 100. ������:> '))
        if num == q_num:
            return "������!"
        attempts -= 1
        print(f'�������� {attempts} �������')
    return "�� ������."


# print(attempts_count(15, 2))


"""
������� �6
����������� ������� ������ ������� ��������� wraps �
������ �� �����������.
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
        num = int(input(f'� ������� ����� �� 1 �� 100. ������:> '))
        if num == q_num:
            return "������!"
        attempts -= 1
        print(f'�������� {attempts} �������')
    return "�� ������."


#print(attempts_count(15, 2))
print(attempts_count.__name__)



class Log:

    def __init__(self, a):
        self.param = a
        """�����-���������"""

    def __call__(self, func):
        def decorated(*args, **kwargs):
            """�������"""
            print(self.param)
            res = func(*args, **kwargs)
            print(f'log: {func.__name__}({args}, {kwargs}) = {res}')
            return res

        return decorated