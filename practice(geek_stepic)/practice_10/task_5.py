"""
������� �5
�������� ��� (��� �����) ��������� ������� ��������.
�������� ����, ����� � �.�.
� ������� ������ ������ ���� ��� ����� ��������,
�������� ���, ��� � ����������� ��� ������.
��� ������� ������ �������� �����, ���������
���������� ����������� ��� ������� ������.
"""

class Fishes:

def __init__(self, kind, name, age, size):
    self._kind = kind
    self._name = name
    self._age = age
    self._size = size


def get_kind(self):
    return self._kind


def get_name(self):
    return self._name


def get_age(self):
    return self._age


def up_age(self):
    self._age += 1


def get_specific(self):
    return self._size


class Birds:

    def __init__(self, kind, name, age, color):
        self._kind = kind
        self._name = name
        self._age = age
        self._color = color

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1

    def get_specific(self):
        return self._color


class Mammals:

    def __init__(self, kind, name, age, spec):
        self._kind = kind
        self._name = name
        self._age = age
        self._spec = spec

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1

    def get_specific(self):
        return self._spec


if __name__ == '__main__':
    f1 = Fishes('������', '����', 1, 15)
    print(f'���: {f1.get_kind()}')
    print(f'������: {f1.get_name()}')
    print(f'�������: {f1.get_age()} ���')
    print(f'������: {f1.get_specific()} ��.')