"""
������� �6
����������� ������ 5.
�������� ����� �������� � ������ ������� � �����
��������.
��������� ������ ���������� �� ����.
���������, ��� � ��������� ����� ������ ������� ������.
"""


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


f1 = Fishes('������', '����', 1, 15)

print(f'���: {f1.get_kind()}')
print(f'������: {f1.get_name()}')
print(f'�������: {f1.get_age()} ���')
print(f'������: {f1.get_specific()} ��.')class Animal:
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


f1 = Fishes('������', '����', 1, 15)

print(f'���: {f1.get_kind()}')
print(f'������: {f1.get_name()}')
print(f'�������: {f1.get_age()} ���')
print(f'������: {f1.get_specific()} ��.')