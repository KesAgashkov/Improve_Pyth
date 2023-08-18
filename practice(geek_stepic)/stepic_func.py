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


# inp = input().split()
# inp = sorted([int(i) for i in inp])
# inp.sort(key=lambda x: sum(map(int, str(x))))
#
# print(*inp)
#
#
#
# print(*sorted(input().split(), key=lambda n: (sum(map(int, n)), int(n))))


# Цепочки преобразований
# Мы также можем строить цепочки преобразований, несколько раз вызывая функцию map().
# Приведенный ниже код, при условии, что функция map() определена как указано выше:

# numbers = ['-1', '20', '3', '-94', '65', '6', '-970', '8']
#
# new_numbers = list(map(abs, map(int, numbers)))
#
# print(new_numbers)
#
# import math
#
#
# def func(temp):
#     return round(temp, 2)
#
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828,
#            1.41546]
#
# print(*list(map(func, numbers)), sep="\n")
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# def func1(temp):
#     if len(str(temp)) == 3 and temp % 5 == 2:
#         return temp
#
#
# def func2(temp):
#     return temp ** 3
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462,
#            815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155,
#            230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669,
#            105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351,
#            1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
#
# preres = filter(func1, numbers)
# print(*list(map(func2, preres)), sep="\n")
#
#
# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
# def oper(acc, item):
#     return acc + item**2
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
#
# print(reduce(oper, numbers, 0))
#
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# def func1(item):
#     if len(str(item).lstrip("-")) == 2 and item % 7 == 0:
#         return item
#
#
# def func2(item):
#     return item ** 2
#
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270,
#            219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35,
#            152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5,
#            187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35,
#            211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2,
#            79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234,
#            10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
# preres = filter(func1, numbers)
# print(sum(list(map(func2, preres))))
#
#
# def func_apply(func, seq):
#     res = []
#     if seq:
#         for item in seq:
#             res.append(func(item))
#
#     return res
#
#
#
# list1 = list(map(len, ['this', 'is', 'a', 'test']))
# list2 = [len(word) for word in ['this', 'is', 'a', 'test']]
#
# print(list1 == list2)
#
#
#
# from operator import add
#
# result = list(map(add, 'abc', '1234'))
# print(result)
#
#
# points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
#
# print(sorted(points, key=lambda point: point[1]))                 # сортируем по второму значению кортежа
# print(sorted(points, key=lambda point: point[0] + point[1]))      # сортируем по сумме элементов кортежа
#
#
#
# dict1 = {'x': 1}
# dict2 = {'y': 2}
# dict3 = {'x': 3, 'y': 4}
#
# result = list(filter(lambda d: 'x' in d.keys(), [dict1, dict2, dict3]))
#
# print(result)


# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda x: round(x**2,1) , floats))
# filter_result = list(filter(lambda name: name == name[::-1] and len(name)>4, words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)
#
# from functools import reduce
#
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
# lst = list(filter(lambda x: x[1]>10_000_000 and x[2] == "primary", data))
# res = sorted(list(map(lambda x: x[0], lst)))
# print(f"Cities: {', '.join(res)}")
#
#
# func = lambda x: x%19==0 or x%13==0
#
#
# func = lambda x: x[0].lower() == x[-1].lower() == 'a'
#
#
# is_non_negative_num = lambda x: str(x).replace('.', '' ,1).isdigit() and not str(x).startswith('-')
#
# print(is_non_negative_num(33.47))
#
#
#
# is_num = lambda x: '-' not in x[1:] and (x.replace('.', '' ,1).replace('-', '' ,1).isdigit() or x.replace('.', '' ,1).replace('-', '' ,1).isdecimal())
#
#
# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
#
# res = sorted(filter(lambda x: len(x) == 6, words))
# print(*res, sep=" ")
#
#
# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# res = map(lambda x: x//2 if x%2 == 0 else x, filter(lambda x: x>47 and x%2==1, numbers))
# print(*res)



numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]

res = list(map(lambda x: x // 2 if x % 2 == 0 else x, list(filter(lambda x: not(x%2 != 0 and x > 47), numbers))))
print(*res, sep=" ")


data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

res =  sorted(data, key= lambda x: x[1][-1],reverse= True)

for el in res:
    print(f"{el[1]}: {el[0]}")


data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

res = sorted(data, key= lambda x: (len(x),x))
print(*res)


mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]

print(max(filter(lambda x: str(x).isdigit(), mixed_list)))



res = map(lambda x: 255 - int(x), input().split())
print(*res)


def evaluate():
    coefficients = list(map(int, input().split()))
    x = int(input())
    grade = len(coefficients) - 1
    res = 0
    for el in coefficients:
        res += el * x ** grade
        grade -= 1

    return res


print(evaluate())