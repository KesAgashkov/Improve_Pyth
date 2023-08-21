"""
������� �1
�������� �����-�������, ������� ������� ��������� ����� ���
������ ����������.
��������� ������ ���������� ��������� k ��������.
�������� k ��������� ��� �������� ����������.
�������� ����� ��� ��������� ����� ���������� �������� �
�� �����������.
"""

from math import factorial


class Factorial:

    def __init__(self, count: int = 1) -> None:
        self.history = []
        self.count = count

    def __call__(self, n: int = 1) -> list[int]:
        res = factorial(n)
        self.history.append({n: res})
        self.history = self.history[-self.count:]
        return res

    def get_history(self):
        return self.history


if __name__ == '__main__':
    f = Factorial(3)
    for i in range(1, 11):
        print(f'{i}! = {f(i)}')

    print(f.get_history())


"""
������� �2
���������� ������ 1.
�������� �������� ���������, ������� ��� ������
��������� �������� � JSON ����.
"""


from math import factorial
import json


class Factorial:

    def __init__(self, count: int = 1) -> None:
        self.history = []
        self.count = count

    def __call__(self, n: int = 1) -> list[int]:
        res = factorial(n)
        self.history.append({n: res})
        self.history = self.history[-self.count:]
        return res

    def get_history(self):
        return self.history

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('factorial.json', 'w', encoding="UTF-8") as js_f:
            json.dump(self.history, js_f)


if __name__ == '__main__':
    f = Factorial(6)
    with f as js_f:
        for i in range(1, 7):
            print(f'{i}! = {f(i)}')


"""
������� �3
�������� �����-���������.
��������� ������ ������ ������������ ��������� ����� �
��������� �� start �� stop � ����� step.
���� �������� ��� ���������, ������� step=1.
���� ������� ���� ��������, ����� ������� start=1.
"""

class Factorial:

    def __init__(self, *args) -> None:
        match args:
            case (stop, ):
                self.stop = stop
                self.start = 1
                self.step = 1
            case (start, stop, ):
                self.start = start
                self.stop = stop
                self.step = 1
            case (start, stop, step):
                self.start = start
                self.stop = stop
                self.step = step
        self.res = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            self.res *= self.start
            self.start += self.step
            return self.res
        raise StopIteration


if __name__ == '__main__':
    f = Factorial(1, 5, 1)
    print(list(f))
    f = Factorial(9)
    print(list(f))


"""
������� �4
����������� ����� ������������� �� ������� ���������.
�������� ����������� �������� ����� � ������
�������������� � �������� �������� ������������ ��������
(�������������).
����������� ���������� �������.
"""

class Rectangle:
    """
    ����� "�������������" ��� ���������� �������� � ����������������,
    ��������� ���������� �������������� �� �������,
    �������� ������� � �������� ���������������
    ���������� � �������� ��������������
    """

    # __slots__ = ('_width', '_length')

    def __init__(self, side_a, side_b=0):
        self._width = side_a
        if side_b == 0:
            side_b = side_a
        self._length = side_b

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new_len):
        if new_len <= 0:
            raise ValueError("����� ������ ���� ������ 0")
        self._length = new_len

    @width.setter
    def width(self, new_width):
        if new_width <= 0:
            raise ValueError("������ ������ ���� ������ 0")
        self._width = new_width

    def get_perimeter(self):
        return 2 * (self._width + self._length)

    def get_area(self):
        return self._width * self._length

    def __add__(self, other):
        """
        �������� ���������������, ������������ ��������� �������� ���������������
        :return: ��������� ������ "Rectangle" ���������� ����� �������� ����������
        """
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        """
        ��������� ���������������, ���������� ��������� �������� ���������������
        :return: ��������� ������ "Rectangle" ���������� ����� ��������� ����������
        """
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def __eq__(self, other):  # ����� ==
        return self.get_area() == other.get_area()

    def __ne__(self, other):  # ������� !=
        return self.get_area() != other.get_area()

    def __gt__(self, other):  # ������ >
        return self.get_area() > other.get_area()

    def __ge__(self, other):  # ������ ��� ����� >=
        return self.get_area() >= other.get_area()

    def __lt__(self, other):  # ����� ������ <
        return self.get_area() < other.get_area()

    def __le__(self, other):  # ������ ��� ����� <=
        return self.get_area() <= other.get_area()

    def __str__(self):
        res = f'������������� �� ��������� {self._width} � {self._length}'
        return res


rectangle1 = Rectangle(7, 11)

print(rectangle1)
rectangle1.width = 11
print(rectangle1)
rectangle1.length = -9
print(rectangle1)


"""
������� �6
�������� ����� ��������������.
�������� ���� ����������� ����������� ����� � ������
�� ���������� � ���������� �������.

"""

class Validator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'{value} ������, ��� {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'{value} ������, ��� {self.max_value}')
        setattr(instance, self.param_name, value)


class Rectangle:
    """
    ����� "�������������" ��� ���������� �������� � ����������������,
    ��������� ���������� �������������� �� �������,
    �������� ������� � �������� ���������������
    ���������� � �������� ��������������
    """
    width = Validator(10, 20)  # ����������
    length = Validator(10, 40)  # ����������

    def __init__(self, width, length):
        self.width = width
        if length == 0:
            length = width
        self.length = length

    def get_perimeter(self):
        return 2 * (self.width + self.length)

    def get_area(self):
        return self.width * self.length

    def __add__(self, other):
        """
        �������� ���������������, ������������ ��������� �������� ���������������
        :return: ��������� ������ "Rectangle" ���������� ����� �������� ����������
        """
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        """
        ��������� ���������������, ���������� ��������� �������� ���������������
        :return: ��������� ������ "Rectangle" ���������� ����� ��������� ����������
        """
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def __eq__(self, other):  # ����� ==
        return self.get_area() == other.get_area()

    def __ne__(self, other):  # ������� !=
        return self.get_area() != other.get_area()

    def __gt__(self, other):  # ������ >
        return self.get_area() > other.get_area()

    def __ge__(self, other):  # ������ ��� ����� >=
        return self.get_area() >= other.get_area()

    def __lt__(self, other):  # ����� ������ <
        return self.get_area() < other.get_area()

    def __le__(self, other):  # ������ ��� ����� <=
        return self.get_area() <= other.get_area()

    def __str__(self):
        res = f'������������� �� ��������� {self.width} � {self.length}'
        return res


rectangle1 = Rectangle(17, 35)

print(rectangle1)
rectangle1.width = 15
rectangle1.length = 40
print(rectangle1)