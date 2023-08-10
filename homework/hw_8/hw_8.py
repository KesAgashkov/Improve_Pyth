# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов
# в ней с учётом всех вложенных файлов и директорий.
import os
import json
import csv
import pickle
def get_directory_files(path):
    """Функция вывода содержимого директории"""
    structure = []
    for file_or_directory in os.listdir(path):
        full_name = os.path.join(os.path.abspath(path), file_or_directory)
        if os.path.isfile(full_name):
            p = os.path.abspath(path) + "\\" + file_or_directory
            structure.append((p))
        else:
            structure.append(os.path.join(os.path.abspath(path), file_or_directory))
            structure.append(get_directory_files(full_name))
    return structure


my_res = get_directory_files(r'C:\Users\Zver\PycharmProjects\improve_pyth\homework\hw_8')
# print(*my_res)

# def get_info_files_system (my_res:list)->list[str,[str]]:
#     for i in range(len(my_res)):
#         if os.path.isfile(f'{my_res[i]}'):
#             my_res[i] = my_res[i] + " | file |" +  f' size: {my_res[i].__sizeof__()}'
#         elif os.path.isdir(f'{my_res[i]}'):
#             my_res[i] = str(my_res[i]) + " | directory |" + f' count(files): {len(my_res[i+1])}'
#             for j in range(len(my_res[i+1])):
#                 if os.path.isfile(f'{my_res[i+1][j]}'):
#                     my_res[i+1][j] = my_res[i+1][j] + " | file |" + f' size: {my_res[i+1][j].__sizeof__()}'
#                 elif os.path.isdir(f'{my_res[i+1][j]}'):
#                     my_res[i] = str(my_res[i+1][j]) + " | directory |" + f' count(files): {len(my_res[i + 1][j+1])}'
#     return my_res


def get_info_files_system (my_res:list)->list[str,[str]]:
    for i in range(len(my_res)):
        if os.path.isfile(f'{my_res[i]}'):
            my_res[i] = my_res[i] + " | file |" +  f' size: {my_res[i].__sizeof__()}'
        elif os.path.isdir(f'{my_res[i]}'):
            my_res[i] = str(my_res[i]) + " | directory |" + f' count(files): {len(my_res[i+1])}'
            get_info_files_system(my_res[i+1])

    return my_res

print(*get_info_files_system (my_res), sep="\n")




with open ("final_res.json", "w", encoding="utf-8") as j:
    json.dump((get_info_files_system(my_res)),j)


with open ("final_res.csv", "w",  newline='', encoding="utf-8") as c:
    data = get_info_files_system(my_res)
    writer = csv.writer(c)
    for el in data:
        print(el)
        writer.writerow([el])

with open ("final_res.pickle", "wb") as p:
    pickle.dump((get_info_files_system(my_res)),p)

# data = get_info_files_system(my_res)

# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.