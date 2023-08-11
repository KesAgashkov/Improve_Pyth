import math
import random
import csv
from functools import wraps
import timeit
import json


# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

solve = ""
spis = []
def append_data_squad_equat(func):
    def wrapper(*args, kwargs):
       func(*args)
       spis.append([f"Уравнение которое решаем:\n{args[0]} * x  2 + {args[1]} * x + {args[2]} = 0".replace("\n", ""),solve])
    return wrapper


def deco_solve_squad_equat(func):
    @wraps(func)
    def wrapper(*args, kwargs):
        print(f"Уравнение которое решаем:\n{args[0]} * x  2 + {args[1]} * x + {args[2]} = 0")
        start = timeit.default_timer()
        res = func(*args)
        global solve
        solve = res
        print(res)
        end = timeit.default_timer() - start
        print(f'Выполнение функции заняло {"{:.2f}".format(end*1_000_000)} миллисекунды')
        print()
    return wrapper


@append_data_squad_equat
@deco_solve_squad_equat
def squad_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("Уравнение не имеет корней")
        return None
    elif d > 0:
        print("Уравнение имеет два корня")
        return f"x1 = {round((-b - math.sqrt(d)) / (2 * a), 3)} ; x2 = {round((-b + math.sqrt(d)) / (2 * a), 3)}"
    else:
        print("Уравнение имеет один корень")
        return f"x = {-b / 2 * a}"


def gen_data_to_equa(filename, lines):
    with open(filename, "w",newline='') as c:
        wr = csv.writer(c,quotechar='\n')
        for i in range(lines):
            wr.writerow([random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)])


def get_arg():
    with open("data.csv", "r") as c:
        read = csv.reader(c)
        lst = []
        for el in read:
            args = list(map(int, el))
            if args[0] == 0:
                args[0]=random.randint(1,100)
            lst.append(args)
    return lst



# gen_data_to_equa("data.csv", 5)

# lst = iter(get_arg())

# for i in range(5):
#     squad_roots(*next(lst))

# with open("res.json", "w", encoding="utf-8") as j:
#      json.dump(spis, j, ensure_ascii=False)