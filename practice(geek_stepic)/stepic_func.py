# def matrix(n=1, m = None, value=0):
#     if m == None:
#         m = n
#     return [[value]*m for i in range(n)]



# 1. Позиционные аргументы без значений по умолчанию.
# 2. Позиционные аргументы со значениями по умолчанию.
# 3. Позиционные аргументы, указанные как *args.
# 4. Именованные аргументы.
# 5. Именнованные со значением по умолчанию
# 6. Именованные аргументы, указанные как *kwargs.
# def my_func(a, b, c=10, *args, d, g=1, **kwargs):
#     print(a, b)
#     print(c)
#     print(args)
#     print(d)
#     print(g)
#     print(kwargs)
#
#
# my_func(1, 2, 3, 4, 5, d=3, g=2, f=1)
#
#
# def sq_sum(*args):
#     return (sum([el**2 for el in args]))
#
#
#
# def mean(*args):
#     res=[el for el in args if type(el) in (int, float)]
#     return sum(res)/len(res) if len(res) else 0
#
#
# def greet(fir, *args):
#     res = []
#     res.append(fir)
#     res.extend(args)
#
#     return "Hello, " + " and ".join(res) + "!"
#
# def greet(name, *args):
#     return 'Hello, ' + ' and '.join([name, *args]) + '!'


# def print_products(*args):
#     i = 1
#     flag = True
#     for el in args:
#         if type(el) == str and el:
#             print(f'{i}) {el}')
#             i = i + 1
#             flag = False
#     print("Нет продуктов") if flag else None
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
#
#
#
# def info_kwargs(**kwargs):
#     for name, value in sorted(kwargs.items()):
#         print(f"{name}: {value}")
#
#
#
#
# def generator_square_polynom(a, b, c):
#     def square_polynom(x):
#         return a*x**2 + b*x + c
#     return square_polynom
#
# f = generator_square_polynom(a=1, b=2, c=1)
# g = generator_square_polynom(a=2, b=0, c=-3)
# h = generator_square_polynom(a=-3, b=-10, c=50)
#
# print(f(1))
# print(g(2))
# print(h(-1))
#
#
# def comparator(pair):
#     return pair[1]
#
# pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
# pairs.sort(key=comparator)
# print(pairs)
#
#
#
# def comparator(pair):
#     return pair[0] + pair[1]
#
# pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
# pairs.sort(key=comparator, reverse=True)
# print(pairs)

# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
#
#
# print(max(numbers, key= lambda x: sum(x)/len(x)), min(numbers, key=lambda x: sum(x)/len(x)), sep="\n")
#
# import math
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
#
# def lenght(x):
#     return math.sqrt(x[0]**2+x[1]**2)
#
# print(sorted(points,key=lenght))
#
#
#
# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
# def summ(x):
#     return min(x) + max(x)
# print(sorted(numbers,key=summ))
#
#
#
#
# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
# def sor(x,check = int(input())):
#     return x[check-1]
#
#
# res = sorted(athletes,key=sor)
# for el in res:
#     print(*el)
#
#
# import math
# num =  int(input())
# com =  input()
#
# def f1(x):
#     return x**2
#
# def f2(x):
#     return x**3
#
# def f3(x):
#     return x**0.5
#
# def f4(x):
#     if x<0:
#        return x * -1
#     return x
#
# def f5(x):
#     return math.sin(x)
#
# dct = {'квадрат': f1, 'куб': f2, 'корень': f3, 'модуль': f4, 'синус': f5}
#
# print(dct[com](num))
#
#
# from math import *
# n = int(input())
# funks = {'квадрат': n**2, 'куб': n**3, 'корень': n**0.5, 'модуль': abs(n), 'синус': sin(n)}
# print(funks[input()])
#
#
# lst = input().split()
# def sor(x):
#     summ=0
#     for el in x:
#         summ+=int(el)
#     return summ
# print(*sorted(lst, key=sor))
#
#
# print(*sorted(input().split(), key=lambda x: sum(map(int, x))))
#


# inp = input().split()
# inp.sort(reverse=True)
# print(*sorted(inp, key=lambda x: sum(map(int, x))))


inp = input().split()
inp = sorted([int(i) for i in inp])
inp.sort(key=lambda x: sum(map(int, str(x))))

print(*inp)



print(*sorted(input().split(), key=lambda n: (sum(map(int, n)), int(n))))