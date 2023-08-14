# class Person:
#     max_up = 3
# p1 = Person()
# p2 = Person()
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
# p1.max_up = 12
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
# Person.max_up = 42
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')


# class Person:
#     max_up = 3
# p1 = Person()
# p2 = Person()
# Person.level = 1
# print(f'{Person.level = }, {p1.level = }, {p2.level = }')
# p1.health = 100
# print(f'{Person.health = }, {p1.health = }, {p2.health = }')
# print(f'{p1.health = }, {p2.health = }')
# print(f'{p1.health = }')

#
# p1 = Person()
# p1.level = 1
# p1.health = 100
# dict_p1 = {}
# dict_p1['level'] = 1
# dict_p1['health'] = 100
# print(f'{p1.health = }')
# print(f'{dict_p1["health"] = }')



# class Person:
#     max_up = 3
#     def __init__(self):
#         self.level = 1
#         self.health = 100
# p1 = Person()
# p2 = Person()
# print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
# print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
# print(f'{Person.max_up = }, {Person.level = }, {Person.health =}')
# Person.level = 100
# print(f'{Person.level = }, {p1.level = }, {p2.level = }')


# class Person:
#     max_up = 3
#     def __init__(self, name, race='unknown'):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
# p1 = Person('Сильвана', 'Эльф')
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу')
# print(f'{p1.name = }, {p1.race = }')
# print(f'{p2.name = }, {p2.race = }')
# print(f'{p3.name = }, {p3.race = }')
#
#
# class Person:
#     max_up = 3
#     def __init__(self, name, race='unknown'):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#     def level_up(self):
#         self.level += 1
# p1 = Person('Сильвана', 'Эльф')
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу')
# print(f'{p1.level = }, {p2.level = }, {p3.level = }')
# p3.level_up()
# p1.level_up()
# p3.level_up()
# print(f'{p1.level = }, {p2.level = }, {p3.level = }')
#
#
# class Person:
#     max_up = 3
#     def __init__(self, name, race='unknown'):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#     def level_up(self):
#         self.level += 1
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity
# p1 = Person('Сильвана', 'Эльф')
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу')
# print(f'{p1.health = }, {p2.health = }, {p3.health = }')
# p1.change_health(p2, 10)
# print(f'{p1.health = }, {p2.health = }, {p3.health = }')


# class Person:
#     max_up = 3
#     _max_level = 80
#     def __init__(self, name, race='unknown', speed=100):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#         self._speed = speed
#     def _check_level(self):
#         return self.level < self._max_level
#     def level_up(self):
#         if self._check_level():
#            self.level += 1
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity
# p1 = Person('Сильвана', 'Эльф', 120)
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу', speed=60)
# print(f'{p1._max_level = }')
# print(f'{p2._speed = }')
# p2._speed = 150
# print(f'{p2._speed = }')
# p3.level_up()
# print(f'{p3.level = }')
# p3.level = 80
# p3.level_up()
# print(f'{p3.level = }')
#
#
# class Person:
#
#     __max_up = 3
#     _max_level = 80
#     def __init__(self, name, race='unknown', speed=100):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#         self._speed = speed
#         self.up = 3
#     def _check_level(self):
#         return self.level < self._max_level
#     def level_up(self):
#         if self._check_level():
#             self.level += 1
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity
#     def add_up(self):
#         self.up += 1
#         self.up = min(self.up, self.__max_up)
# p1 = Person('Сильвана', 'Эльф', 120)
# print(f'{p1.up = }')
# p1.up = 1
# print(f'{p1.up = }')
# for _ in range(5):
#     p1.add_up()
# print(f'{p1.up = }')
#
# # print(p1.__max_up)
# # print(Person.__max_up)
#
# print(f'{p1._Person__max_up = }')



class Person:
    __max_up = 3
    _max_level = 80
    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3
    def _check_level(self):
        return self.level < self._max_level
    def level_up(self):
        if self._check_level():
            self.level += 1
    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)

# class Hero(Person):
#     def __init__(self, power, *args, **kwargs):
#         self.power = power
#         super().__init__(*args, **kwargs)
# p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
# print(f'{p1.name = }, {p1.up = }, {p1.power = }')



#Переопределение методов

class Hero(Person):
    def __init__(self, power, *args, **kwargs):
        self.power = power
        super().__init__(*args, **kwargs)
    def change_health(self, other, quantity):
        self.health += quantity * 2
        other.health -= quantity * 2
    def add_many_up(self):
        self.up += 1
        self.up = min(self.up, self._Person__max_up * 2)
p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
p2 = Person('Маг', 'Тролль')
print(f'{p1.health = }, {p2.health = }')
p1.change_health(p2, 10)
print(f'{p1.health = }, {p2.health = }')
p2.change_health(p1, 10)
print(f'{p1.health = }, {p2.health = }')
p1.add_many_up()
print(f'{p1.up = }')


class Person:
    __max_up = 3
    _max_level = 80
    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3
    def _check_level(self):
        return self.level < self._max_level
    def level_up(self):
        if self._check_level():
            self.level += 1
    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity
    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)
class Address:
    def __init__(self, country, city, street):
        self.country = country or ''
        self.city = city or ''
        self.street = street or ''
    def say_address(self):
        return f'Адрес героя: {self.country}, {self.city}, {self.street}'
class Weapon:
    def __init__(self, left_hand, right_hand):
        self.left_hand = left_hand or 'Клинок'
        self.right_hand = right_hand or 'Лук'
class Hero(Person, Address, Weapon):
    def __init__(self, power, name=None, race=None, speed=None, country=None, city=None, street=None,left_hand=None, right_hand=None):
        self.power = power
        Person.__init__(self, name, race, speed)
        Address.__init__(self, country, city, street)
        Weapon.__init__(self, left_hand, right_hand)
    def change_health(self, other, quantity):
        self.health += quantity * 2
        other.health -= quantity * 2
    def add_many_ups(self):
        self.up += 1
        self.up = min(self.up, self._Person__max_up * 2)


p1 = Hero('archery', 'Сильвана', 'Эльф', 120, country='Эльфляндия', street='Ночного эльфа', left_hand='Стрела')
print(f'{p1.say_address()}')
print(f'{p1.right_hand = }, {p1.left_hand = }')


class A:
    def __init__(self):
        print('Init class A')
        self.data_a = 'A'
class B:
    def __init__(self):
        print('Init class B')
        self.data_b = 'B'
class C:
    def __init__(self):
        print('Init class C')
        self.data_c = 'C'
class D:
    def __init__(self):
        print('Init class D')
        self.data_d = 'D'
class X1(A, C):
    def __init__(self):
        print('Init class X1')
        super().__init__()
class X2(B, D):
    def __init__(self):
        print('Init class X2')
        super().__init__()
class X3(A, D):
    def __init__(self):
        print('Init class X3')
        super().__init__()
class Z(X1, X2, X3):
    def __init__(self):
        print('Init class Z')
        super().__init__()

print(*Z.mro(), sep='\n')



class DivStr(str):
    def __init__(self, obj):
        self.obj = str(obj)
    def __truediv__(self, other):
        first = self.obj.endswith('/')
        start = self.obj
        if isinstance(other, str):
            second = other.startswith('/')
            finish = other
        elif isinstance(other, DivStr):
            second = other.obj.startswith('/')
            finish = other.obj
        else:
            second = str(other).startswith('/')
            finish = str(other)
        if first and second:
            return DivStr(start[:-1] + finish)
        if (first and not second) or (not first and second):
            return DivStr(start + finish)
        if not first and not second:
            return DivStr(start + '/' + finish)


path_1 = DivStr('/home/user/')
path_2 = DivStr('/my_project/workdir')
result = path_1 / path_2
print(f'{result = }, {type(result)}')
print(f'{result / "text" = }')
print(f'{result / 42 = }')
print(f'{result * 3 = }')






