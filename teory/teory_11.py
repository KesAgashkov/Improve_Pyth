import sys
from decimal import Decimal


class User:

    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3
        # принтим только в учебных целях, а не для реальных задач
        print(f'Создал {self} со свойствами:\n'f'{self.name = },\t{self.equipment = },\t{self.life= }')


# print('Создаём первый раз')
# u_1 = User('Спенглер')
# print('Создаём второй раз')
# u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print('Создаём третий раз')
# u_3 = User(equipment=['ловушка', 'прибор ночного видения'], name='Стэнц')


# Контроль создания класса через __new__
# Метод __new__ срабатывает раньше __init__ и определяет что должен вернуть
# класс в качестве себя - класса. Рассмотрим вначале общий пример.
class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(f'Создал класс {cls}')
        return instance
        print('Создаём первый раз')


u_1 = User('Спенглер')
print('Создаём второй раз')
u_2 = User('Венкман')
print('Создаём третий раз')
u_3 = User(name='Стэнц')


# Расширение неизменяемых классов
# Один из вариантов использования дандер __new__ — расширение
# функциональности уже имеющихся неизменяемых классов Python. Например мы
# хотим использовать переменную целого типа, которая дополнительно хранит
# присвоенное числу имя.
class NamedInt(int):
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        print(f'Создал класс {cls}')
        return instance


print('Создаём первый раз')
a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще')
print('Создаём второй раз')
b = NamedInt(73, 'Лучшее просто число')
print(f'{a = }\t{a.name = }\t{type(a) = }')
print(f'{b = }\t{b.name = }\t{type(b) = }')
c = a + b
print(f'{c = }\t{type(c) = }')


# Шаблон Одиночка, Singleton
# Ещё один вариант использования дандре __new__ — паттерн Singleton. Он
# позволяет создавать лишь один экземпляр класса. Вторая и последующие попытки
# будут возвращать ранее созданый экземпляр.
# 🔥 Внимание! Это не единственный вариант создания паттерна Одиночка в
# Python, а версия через __new__
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name: str):
        self.name = name


a = Singleton('Первый')
print(f'{a.name = }')
b = Singleton('Второй')
print(f'{a is b = }')
print(f'{a.name = }\n{b.name = }')


# Удаление экземпляра класса, __del__
class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')

    def __del__(self):
        print(f'Удаление экземпляра {self.name}')


# u_1 = User('Спенглер')
# print(sys.getrefcount(u_1))
# u_2 = u_1
# print(sys.getrefcount(u_1), sys.getrefcount(u_2))
# del u_1
# print(sys.getrefcount(u_2))
# print('Завершение работы')


# Строка документации
# Как и при создании функции, при создании классов принято оставлять
# документацию к нему. Для этого достаточно использовать многострочный
# комментарий сразу после определения класса — строки class ClassName:
# Посмотрите на пример
class User:
    """A User training class for demonstrating class
    documentation.
    Shows the operation of the help(cls) and the dander method
    __doc__"""

    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()


u_1 = User('Спенглер')
print('Справка класса User ниже', '*' * 50)
help(User)
print('Справка экземпляра u_1 ниже', '*' * 50)
help(u_1)


# Хранение документации в __doc__
# Любая многострочная строка после заголовка класса и метода автоматичские
# сохраняется в дандер переменную __doc__. Помимо вызова справки через
# функцию help можно прочитать отдельный мнострочник напрямую обратившись к
# переменной.
class User:
    """A User training class for demonstrating class
    documentation.
    Shows the operation of the help(cls) and the dander method
    __doc__"""

    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name
        print(f'Создал {self.name = }')

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()


u_1 = User('Спенглер')
print(f'Документация класса: {User.__doc__ = }')
print(f'Документация экземпляра: {u_1.__doc__ = }')
print(f'Документация метода: {u_1.simple_method.__doc__}')


# Представление для пользователя, __str__
# Дандер метод __str__ используется для получения удобного пользователю
# описания экземпляра.
class User:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

    def __str__(self):
        return f'Экземпляр класса User с именем "{self.name}'


user = User('Спенглер')
print(user)


# Представление для создания экземпляра,
# __repr__
# Дандер метод __repr__ аналогичен __str__, но возвращает максимально близкое к
# созданию экземпляра класса представление.
class User:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

    def __repr__(self):
        return f'User({self.name})'


user = User('Спенглер')
print(user)


# Если скопировать вывод метода repr и присвоить его переменной, должен
# получится ещё один экземпляр класса. Рассмотрим более сложный класс и его
# метод __repr__.
class User:

    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3

    def __repr__(self):
        return f'User({self.name}, {self.equipment})'


user = User('Венкман', ['протонный ускоритель', 'ловушка'])
print(user)
new_user = repr(user)
print(new_user)


# Приоритет методов
# Добавим классу из примера выше метод __str__ и посмотрим какой из них
# сработает.
class User:
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3

    def __str__(self):
        eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
        return f'Перед нами {self.name} с {eq}. Количество жизней - {self.life}'

    def __repr__(self):
        return f'User({self.name}, {self.equipment})'


user = User('Венкман', ['протонный ускоритель', 'ловушка'])
print(user)
print(f'{user}')

print(repr(user))
print(f'{user = }')


# Сложение через __add__
# Создадим класс вектор и научим вектора складываться.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


a = Vector(2, 4)
b = Vector(3, 7)
c = a + b
print(f'{a = }\t{b = }\t{c = }')


#
# Умножение текста на “продвинутый текст”
# методом __rmul__
# Создадим класс на основе str с методом __rmul__. Если слева оказывается обычная
# строка, будем между словами добавлять текст из “продвинутой строки”,
# перемножим их.
class StrPro(str):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        return instance

    def __rmul__(self, other: str):
        words = other.split()
        result = self.join(words)
        return StrPro(result)


text = 'Каждый охотник желает знать где сидит фазан'
s = StrPro(' (=^.^=) ')
print(f'{text = }\n{s = }')
print(text * s)


# print(s * text)


# Вычисление процентов вместо нахождения
# остатка от деления, __imod__
# Создадим простой класс Money, который будет увеличивать значение на указанный
# процент при записи Money %= float | int


class Money:
    def __init__(self, value: int | float):
        self.value = Decimal(value)

    def __repr__(self):
        return f'Money({self.value:.2f})'

    def __imod__(self, other):
        self.value = self.value * Decimal(1 + other / 100)
        return self


m = Money(100)
print(m)
m %= 50
print(m)
m %= 100
print(m)


# Сравнение на идентичность, __eq__
# Создадим класс треугольник, который хранит длины трёх сторон. В первом
# варианте не будем прописывать дандер __eq__ и попробуем сравнить экземпляры.
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b},{self.c}'


one = Triangle(3, 4, 5)
two = one
three = Triangle(3, 4, 5)
print(one == two)
print(one == three)


# Сравнение на идентичность, __eq__
# Создадим класс треугольник, который хранит длины трёх сторон. В первом
# варианте не будем прописывать дандер __eq__ и попробуем сравнить экземпляры.
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b},{self.c}'


one = Triangle(3, 4, 5)
two = one
three = Triangle(3, 4, 5)
four = Triangle(4, 3, 5)
print(f'{one == two = }')
print(f'{one == three = }')
print(f'{one == four = }')
print(f'{one != one = }')


from math import sqrt
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b},{self.c}'

    def __repr__(self):
        return f'Triangle({self.a}, {self.b}, {self.c})'

    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second

    def area(self):
        p = (self.a + self.b + self.c) / 2
        _area = sqrt(p * (p - self.a) * (p - self.b) * (p -
        self.c))
        return _area

    def __lt__(self, other):
        return self.area() < other.area()


one = Triangle(3, 4, 5)
two = Triangle(5, 5, 5)
print(f'{one} имеет площадь {one.area():.3f} у.е.')
print(f'{two} имеет площадь {two.area():.3f} у.е.')
print(f'{one > two = }\n{one < two = }')
data = [Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4),
Triangle(3, 5, 3)]
result = sorted(data)
print(result)
print(', '.join(f'{item.area():.3f}' for item in result))


# Получение значения атрибута,
# __getattribute__
# Дандер __getattribute__ вызывается при любой попытке обращения к атрибутам
# экземпляра.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)


a = Vector(2, 4)
print(a.x)
print(f'{a = }')


# Обращение к несуществующему атрибуту,
# __getattr__
# Если свойство отсутствует, в первую очередь вызывается дандер __getattribute__. В
# случае возврата им ошибки AttributeError вызывается метод __getattr__. Он также
# может поднять ошибку. А может как-то иначе обработать запрос.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__setattr__(self, key, value)
    def __getattr__(self, item):
        return None
a = Vector(2, 4)
print(a.z) # None
print(f'{a = }')
