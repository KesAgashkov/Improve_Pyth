
# Решить задания, которые не успели решить на семинаре.
# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.

# Задание 1
import random

class Fabric:
    def __init__(self, type_animal):
        self.type_animal = type_animal

    def get_kind(self):
        dct = {"рыба": Fishes, "птица": Birds, "млек": Mammals}
        if self.type_animal == "рыба":
            kind = random.choice(["Карась", "Окунь", "Щука", "Премудрый пескарь"])
            name = random.choice(["Кеша", "Василий", "Алексей", "Дори"])
            age = random.randint(1,10)
            size = random.randint(10,300)
            return dct[self.type_animal](kind, name, age, size)
        elif self.type_animal == "птица":
            kind = random.choice(["Сойка", "Ворона", "Воробей", "Глухарь"])
            name = random.choice(["Марина", "Аркадий", "Федор", "Гриша"])
            age = random.randint(1, 10)
            color = random.choice(["Красный", "Черный", "Белый", "Синий"])
            return dct[self.type_animal](kind, name, age, color)
        elif self.type_animal == "млек":
            kind = random.choice(["Варан", "Кит", "Кенгуру", "Свинья"])
            name = random.choice(["Пётр", "Саша", "Кристина", "Оля"])
            age = random.randint(1, 10)
            spec = random.randint(10,500)
            return dct[self.type_animal](kind, name, age, spec)
        else:
            return None


class Animal:
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1


class Fishes(Animal):

    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def get_specific(self):
        return self._size


class Birds(Animal):

    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def get_specific(self):
        return self._color


class Mammals(Animal):

    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def get_specific(self):
        return self._spec


mystery_kind = Fabric("м").get_kind()

if str(type(mystery_kind)).split(".")[-1].rstrip("'>") == "Fishes":
    print(f'Вид: {mystery_kind.get_kind()}')
    print(f'кличка: {mystery_kind.get_name()}')
    print(f'возраст: {mystery_kind.get_age()} лет')
    print(f'размер: {mystery_kind.get_specific()} см.')

elif str(type(mystery_kind)).split(".")[-1].rstrip("'>") == "Birds":
    print(f'Вид: {mystery_kind.get_kind()}')
    print(f'кличка: {mystery_kind.get_name()}')
    print(f'возраст: {mystery_kind.get_age()} лет')
    print(f'размер: {mystery_kind.get_specific()} см')

elif str(type(mystery_kind)).split(".")[-1].rstrip("'>") == "Mammals":
    print(f'Вид: {mystery_kind.get_kind()}')
    print(f'кличка: {mystery_kind.get_name()}')
    print(f'возраст: {mystery_kind.get_age()} лет')
    print(f'размер: {mystery_kind.get_specific()} см')

else:
    raise TypeError("Ошибка. Такого типа животного нет в системе")


# Задание 2

class FunctionPath:
    def __init__(self, path):
        self.path =  path

    def get_path_filename_fileexten(self):
        str_list = self.path.rsplit('/', maxsplit=1)
        path = str_list[0]
        file_name, file_exten = str_list[-1].split('.')
        return path, file_name, file_exten

# file_path = Function("/home/itsecforu/Documents/ubuntu-commands.md")
# print(*file_path.get_path_filename_fileexten(), sep=" | ")

class FunctionMatrix:
    def __init__(self, matr):
        self.matr =  matr

    def transp_matrix(self):
        res = []
        lst = self.matr
        if lst:
            res = [[lst[j][i] for j in range(len(lst[0]))] for i in range(len(lst))]
            return res
        else:
            print("Введенная матрица пустая")
            return res

    def look_matrix(self):
        matr =self.matr
        for el in matr:
            print(*el)
        print()


    def mirror_matrix(self):
        res = []
        lst = self.matr
        if lst:
            res = [[lst[j][i] for j in range(len(lst[0]))][::-1] for i in range(len(lst))]
            return res
        else:
            print("Введенная матрица пустая")
            return res


# new_matr = FunctionMatrix([[3, 8, 5], [4, 9, 1], [3, 4, 0]])
#
# new_matr.look_matrix()
# print(*new_matr.transp_matrix(), sep="\n")
# print()
# print(*new_matr.mirror_matrix(),sep="\n")


