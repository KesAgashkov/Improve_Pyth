from random import randint
from task_3 import Human

"""
������� �4
�������� ����� ���������.
�������������� ������� �������� �� �������� �������.
� ���������� ������ ����:
? ������������ ����������������� �����
? ������� ������� ����������� ��� ������� �� �������
����� ���� id �� ����
"""

class Employee(Human):

    # def __init__(self, *args):
    #     # super().__init__(*args)
    #     self._id = randint(100000, 999999)
    #     self._level = sum(int(i) for i in str(self._id)) % 7

    def get_id(self):
        self._id = randint(100000, 999999)
        return self._id

    def get_level(self):
        self._level = sum(int(i) for i in str(self._id)) % 7
        return self._level


employee = Employee('������', '����', 45)

print(employee._last_name)
print(employee.get_age())

print(employee.get_fullname())
print(employee.get_id())
print(employee.get_level())