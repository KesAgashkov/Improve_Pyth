"""
Задание №1
📌 Создайте класс Моя Строка, где:
📌 будут доступны все возможности str
📌 дополнительно хранятся имя автора строки и время создания
(time.time)
"""

import time
from datetime import datetime


class MyStr(str):
    """Класс для создания эксземпляров со строкой именем и датой создания"""
    def __new__(cls, value, author_name):
        my_srt = super().__new__(cls, value)
        my_srt.author_name = author_name
        # my_srt.creation_time = time.time()
        my_srt.creation_time = datetime.now()
        return my_srt

    def __str__(self):
        return f'{self.author_name}, {self.creation_time}'



# if __name__ == '__main__':
#     s = MyStr('Новая Строка Теста', 'Sergey')
#     print(s)
#     print(MyStr.__doc__)




"""
Задание №2
📌 Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
📌 При создании нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-
архивов
📌 list-архивы также являются свойствами экземпляра
"""

class Archive:
    """Класс сохраняет в архиве атрибуты созданных эксземпляров класса"""
    nums_archive = []
    strs_archive = []
    last_num = None
    last_str = None

    def __init__(self, num, new_str):
        self.num = num
        self.new_str = new_str

        if Archive.last_num is not None:
            Archive.nums_archive.append(Archive.last_num)
        if Archive.last_str is not None:
            Archive.strs_archive.append(Archive.last_str)

        Archive.last_num = num
        Archive.last_str = new_str

    def __str__(Archive):
        return f'{Archive.strs_archive},\n {Archive.nums_archive}'



# if __name__ == '__main__':
#     arc1 = Archive(1, "Строка 1")
#
#     arc2 = Archive(2, "Текст 2")
#
#     print(Archive)


"""
Задание №4
📌 Доработаем класс Архив из задачи 2.
📌 Добавьте методы представления экземпляра для программиста
и для пользователя.
"""

class Archive:
    """Класс сохраняет в архиве атрибуты созданных эксземпляров класса (Переопределены методы __str__ и __repr__"""
    nums_archive = []
    strs_archive = []
    last_num = None
    last_str = None

    def __init__(self, num, new_str):
        self.num = num
        self.new_str = new_str

        if Archive.last_num is not None:
            self.nums_archive.append(Archive.last_num)
        if Archive.last_str is not None:
            self.strs_archive.append(Archive.last_str)

        Archive.last_num = num
        Archive.last_str = new_str

    def __str__(self):
        res = f'номер: {self.num}, строка: {self.new_str}, архив: {list(zip(self.nums_archive, self.strs_archive))} '
        return res

    def __repr__(self):
        return f'Archive({self.num = },{self.new_str = })'


# if __name__ == '__main__':
#     arc1 = Archive(1, "Строка 1")
#     print(arc1)
#     print(arc1.__repr__())
#     arc2 = Archive(2, "Текст 2")
#     arc3 = Archive(3, "Symbols 3")
#     print(arc3)


"""
Задание №5
📌 Дорабатываем класс прямоугольник из прошлого семинара.
📌 Добавьте возможность сложения и вычитания.
📌 При этом должен создаваться новый экземпляр
прямоугольника.
📌 Складываем и вычитаем периметры, а не длинну и ширину.
📌 При вычитании не допускайте отрицательных значений.
"""

class Rectangle:
    """Класс позволяет складывать и вычитать периметры треугольников"""
    def __init__(self, side_a, side_b=0):
        self.side_a = side_a
        if side_b == 0:
            side_b = side_a
        self.side_b = side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def get_area(self):
        return self.side_a * self.side_b

    def __add__(self, other):
        # (self.side_a + other.side_a, self.side_b + other.side_b)
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def __str__(self):
        return f"a = {self.side_a}, b = {self.side_b}, периметр = {round(self.get_perimeter(),1)}"


rectangle1 = Rectangle(7.3)
rectangle2 = Rectangle(5.6, 10.2)
rectangle3 = rectangle1 + rectangle2
rectangle4 = rectangle3 - rectangle2

print(f'Периметр 1 прямоугольника = {rectangle1.get_perimeter():.2f}')
print(f'Периметр 2 прямоугольника = {rectangle2.get_perimeter():.2f}')

print(f'Периметр 3 прямоугольника = {rectangle3.get_perimeter():.2f}')
print(f'Периметр 4 прямоугольника = {rectangle4.get_perimeter():.2f}')

print(rectangle1)

print(rectangle2)


"""
Задание №6
📌 Доработайте прошлую задачу.
📌 Добавьте сравнение прямоугольников по площади
📌 Должны работать все шесть операций сравнения
"""

class Rectangle:
    """Класс позволяет складывать и вычитать периметры треугольников,
    а также поддерживает операции сравнения треугольников"""

    def __init__(self, side_a, side_b=0):
        self.side_a = side_a
        if side_b == 0:
            side_b = side_a
        self.side_b = side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def get_area(self):
        return self.side_a * self.side_b

    def __str__(self):
        return f"a = {self.side_a}, b = {self.side_b}, периметр = {round(self.get_perimeter(),1)}"

    def __add__(self, other):
        # (self.side_a + other.side_a, self.side_b + other.side_b)
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def __eq__(self, other):  # равно ==
        return self.get_area() == other.get_area()

    def __ne__(self, other):  # неравно !=
        return self.get_area() != other.get_area()

    def __gt__(self, other):  # больше >
        return self.get_area() > other.get_area()

    def __ge__(self, other):  # больше или равно >=
        return self.get_area() >= other.get_area()

    def __lt__(self, other):  # метод меньше <
        return self.get_area() < other.get_area()

    def __le__(self, other):  # меньше или равно <=
        return self.get_area() <= other.get_area()



rectangle1 = Rectangle(7.3)
rectangle2 = Rectangle(5.6, 10.2)

print(f'площадь 1 прямоугольника = {rectangle1.get_area():.2f}')
print(f'площадь 2 прямоугольника = {rectangle2.get_area():.2f}')
# print(rectangle1 == rectangle2)
print(f'({rectangle1.get_area():.2f} = {rectangle2.get_area():.2f}):', rectangle1 == rectangle2)
print(f'({rectangle1.get_area():.2f} != {rectangle2.get_area():.2f}):', rectangle1 != rectangle2)
print(f'({rectangle1.get_area():.2f} > {rectangle2.get_area():.2f}):', rectangle1 > rectangle2)
print(f'({rectangle1.get_area():.2f} <= {rectangle2.get_area():.2f}):', rectangle1 <= rectangle2)
print(f'({rectangle1.get_area():.2f} < {rectangle2.get_area():.2f}):', rectangle1 < rectangle2)
print(f'({rectangle1.get_area():.2f} >= {rectangle2.get_area():.2f}):', rectangle1 >= rectangle2)

print(rectangle2)
