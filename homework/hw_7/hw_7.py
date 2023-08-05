import os
from pathlib import Path
from file_function import *

"""
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

"""

def sort_files_by_exten():
    exts = {"видео": ("mp4", "avi"), "изображения": ("jpg", "png"), "текст": ("txt", "md")}
    for key, extens in exts.items():
        pat = os.getcwd()
        ful_p = pat + "\\" + key
        os.mkdir(ful_p)
        for i in range(len(extens)):
            os.chdir(ful_p)
            os.mkdir(ful_p + "\\" + extens[i])
            os.chdir("..")

    for el in os.listdir():
        if os.path.isfile(el):
            temp_el = el.split(".")[-1]
            for k, v in exts.items():
                if temp_el in v:
                    cur = os.getcwd() + "\\" + el
                    distin = os.getcwd() + "\\" + k + "\\" + v[v.index(temp_el)] + "\\" + el
                    os.replace(cur, distin)


# sort_files_by_exten()

# Задание 2
# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
# исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

def rename_files_by_cond(desire_name:str, count_dig_sn: int, exten_init: str, exten_finit: str, rang_init_name: (int,int)):

    start_num = 1
    for el in os.listdir():
        if os.path.isfile(el) and el.split(".")[-1] == exten_init:
            temp =el[rang_init_name[0]:rang_init_name[1]] + desire_name+str(start_num).rjust(count_dig_sn,"0") +  exten_finit
            new_name = os.path.join(os.getcwd(), temp)
            old_name = os.path.join(os.getcwd(), el)
            start_num += 1
            os.rename(old_name,new_name)

# rename_files_by_cond("new", 5, "txt", ".md", (1,4))

# Задание 3
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

# Функции сгруппированы в файле file_function

