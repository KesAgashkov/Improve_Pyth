"""
# Задание №1
# Погружение в Python | Функции
# ✔ Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.
# """
#
# # text = "Слова выводятся отсортированными согласно кодировки Unicode"
# #
# #
# # def print_sort_txt(txt):
# #     words = txt.lower().split()
# #     words = sorted(words)
# #     max_len = max(len(word) for word in words)
# #
# #     for i, word in enumerate(words, start=1):
# #         print(f'{i}. {word:>{max_len}}')
# #
# #
# # def print_sort(txt):
# #     for i, word in enumerate(sorted(txt.lower().split()), 1):
# #         print(f'{i}. {word:>{max(len(word) for word in txt.lower().split())}}')
# #
# #
# # print_sort_txt(text)
# # print_sort(text)
#
# """
# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.
# """
# def sort_char(data):
#     return sorted(list(set([ord(el) for el in data])), reverse=True)
# print(sort_char("Задание №2 Напишите функцию, которая принимает строку текста"))
#
# """
# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.
# """
# """
# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.
# """
#
#
# def dict_fnc(my_str):
#     dct = {ord(el): int(el) for el in sorted(my_str.split())}
#     return dct
#
#
# # print(dict_fnc("9 7"))
#
# """
# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.
# """
#
# def sort_data(data):
#     for i in range(len(data) - 1):
#         index = i
#         for j in range(i+1, len(data)):
#             if data[j] < data[index]:
#                 index = j
#         if index != i:
#             data[index], data[i] = data[i], data[index]
#
#
# data = [3, 2, 9, 6, 5, 1, 7, 4, 8]
# # print(data)
# # sort_data(data)
# # print(data)
#
#
# """
# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.
# """
#
# def func(lst_names, lst_bases, lst_bonuses):
#     res = {el_1: el_2 * float(el_3.rstrip("%"))/100 for el_1, el_2, el_3 in zip(lst_names,lst_bases,lst_bonuses)}
#     return res
#
# names = ['Борис', 'Иван', 'Петр', "Сергей"]
# salaries = [10000, 12000, 16000, 14000]
# awards = ['12.35%', '10.25%', '7.75%', '8.85%']
#
# # print(func(names,salaries,awards))
#
#
# """
# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
# """
#
#
# def sum_nums(lst, ind_1, ind_2):
#     res = 0
#     if ind_1 >= ind_2:
#         print("Между индексами элементов нет")
#         return res
#     elif ind_2 >= len(lst):
#         return sum(lst[ind_1 + 1:])
#     elif ind_1 < 0:
#         return sum(lst[:ind_2])
#     else:
#         return sum(lst[ind_1 + 1: ind_2])
#
#
# lst = [1, 2, 3, 4, 5]
# index_1 = 2
# index_2 = 4
#
# # print(f"Сумма: {sum_nums(lst, index_1, index_2)}")
#
# """
# Задание №7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь
# """
#
# data = {"company_1": [70, 12, 25, -28, 10, 36],
#         "company_2": [-55, 10, -20, -10, -15, -15],
#         "company_3": [40, 12, 21, -70, 11, 65]
#         }
#
#
# def total_result(dct):
#     res = {key: sum(value) for key, value in dct.items()}
#
#     print(res)
#
#     if all(map(lambda x: x > 0, res.values())):
#         return True
#     else:
#         return False
#
# # print(total_result(data))
#
# """
# Задание №8
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
# """

names = ['Alex', 'Nick', 'Michael']
count = 1
tapes = 1500
txt = 'Test'
rows = 'first'
s = -15
sym_calls = True

tmp_var = globals().copy()

print(tmp_var)

my_var_name = {}

for item in tmp_var.keys():
    if not item.startswith('__'):
        my_var_name[item] = tmp_var[item]


for el in my_var_name.copy():
    if el.endswith("s") and len(el) != 1:
        my_var_name[el[:-1]] = my_var_name[el]
        my_var_name[el] = None

print(my_var_name)
