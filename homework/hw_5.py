# """
# Задание 1
# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.
# """
def get_path_filename_fileexten(full_path: str) -> tuple:
    """Функция принимает абсолютный путь в ОС linux
    и возвращает путь, имя файла, расширение файла
    """
    str_list = full_path.rsplit('/', maxsplit=1)
    path = str_list[0]
    file_name, file_exten = str_list[-1].split('.')
    return path, file_name, file_exten


# print(get_path_filename_fileexten("/home/itsecforu/Documents/ubuntu-commands.md"))

# """
# Задание 2
# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии
# """

def func(lst_names: str, lst_bases: int, lst_bonuses: float):
    yield ((el_1, el_2 * float(el_3.rstrip("%")) / 100) for el_1, el_2, el_3 in zip(lst_names, lst_bases, lst_bonuses))


names = ['Борис', 'Иван', 'Петр', "Сергей"]
salaries = [10000, 12000, 16000, 14000]
awards = ['12.35%', '10.25%', '7.75%', '8.85%']

# for el in func(names, salaries, awards):
#     print(*el, sep='\n')


"""
# Задание 3
# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
# """


def get_fibon_n(n: int):
    k = n
    f_1 = f_2 = 1
    n = int(n) - 2
    while n > 0:
        f_1, f_2 = f_2, f_1 + f_2
        n -= 1
    yield f'{k} = {f_2}'

# print(f'Число Фибоначчи от' , *get_fibon_n(45))
