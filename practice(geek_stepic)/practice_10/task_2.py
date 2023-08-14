"""
������� �2
�������� ����� �������������.
����� ������ ��������� ����� � ������ ��� ��������
����������.
� ������ ������ ���� ��� ������, ������������ ��������
� �������.
���� ��� �������� ���������� ��������� ������ ����
�������, ������� ��� � ��� �������.
"""

class Rectangle:

    def __init__(self, side_a, side_b=0):
        self._side_a = side_a
        if side_b == 0:
            side_b = side_a
        self._side_b = side_b

    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)

    def get_area(self):
        return self._side_a * self._side_b


rectangle1 = Rectangle(7.3)
rectangle2 = Rectangle(5.6, 10.2)

print(f'�������� �������������� = {rectangle1.get_perimeter():.2f}, \n'
      f'������� �������������� = {rectangle1.get_area():.2f}')
print(f'�������� �������������� = {rectangle2.get_perimeter():.2f}, \n'
      f'������� �������������� = {rectangle2.get_area():.2f}')

