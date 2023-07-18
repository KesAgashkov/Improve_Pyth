import math
import fractions

# Задание № 5
# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.
# version 1
# a = 5
# b = 10
# c = 400
# version 2
def solve_quad_equation(a: int, b: int, c: int):
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

# solve_quad_equation(1,-6,13)


#Задание №2
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def convert_dec_to_hex():
    num_dec = int(input("введите число: "))
    res = ''
    DIVIDER = 16
    num = 0
    print(hex(num_dec))
    while num_dec > 0:
        num = num_dec % DIVIDER
        if num < 10:
            res = str(num) + res
        elif num == 10:
            res = str("A") + res
        elif num == 11:
            res = str("B") + res
        elif num == 12:
            res = str("C") + res
        elif num == 13:
            res = str("D") + res
        elif num == 14:
            res = str("E") + res
        elif num == 15:
            res = str("F") + res
        num_dec //= DIVIDER

    print(res)


# convert_dec_to_hex()

# Задание №3
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
def get_summ_prod_from_fractions():
    a, b = map(int, input("Введите числитель и знаменатель первой дроби через пробел: ").split())
    first = fractions.Fraction(a, b)
    c, d = map(int, input("Введите числитель и знаменатель второй дроби через пробел: ").split())
    second = fractions.Fraction(c, d)
    print(f"Сумма дробей = : {first + second}")
    print(f"Произведение дробей = : {first * second}")


# get_summ_prod_from_fractions()
