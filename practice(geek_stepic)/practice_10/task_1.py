"""
������� �1
�������� ����� ����������.
����� ������ ��������� ������ ���������� ��� ��������
����������.
� ������ ������ ���� ��� ������, ������������ �����
���������� � � �������.
"""

from math import pi


class Circle:

    def __init__(self, radius):
        self._radius = radius

    def get_len(self):
        return 2 * pi * self._radius

    def get_area(self):
        return pi * self._radius ** 2


circle = Circle(5)
print(f'����� ���������� = {circle.get_len():.3f}, \n������� ���������� = {circle.get_area():.3f}')