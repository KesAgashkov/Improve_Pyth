# ������� �1
# ? �������� �������, ������� ������� �� ������ ��� �������
# ����� ���� ���������� �������� � ��������.
# ? ������������ ������ � ������ ��������

import re


def convert_str(text):
    '''������� �� ������ ��� �������, ����� ���� ���������� �������� � �������� '''

    new_str = re.compile('[^a-zA-Z ]')
    res = new_str.sub('', text).lower()
    return res


if __name__ == '__main__':
    print(convert_str('HelLO# ���$ WorlD!!'))


# ������� �2
# ? �������� ��� ������ 1 ����� doctest. ���������
# ��������� ��������:
# ? ������� ������ ��� ���������
# ? ������� ������ � ��������������� �������� ��� ������
# ��������
# ? ������� ������ � ��������� ������ ����������
# ? ������� ������ � ��������� ���� ������ ���������
# ? ������� ������ � ������ ���� ����������������� �������
# (����� �. 1)



import re
import doctest


def convert_str(text):
    '''������� �� ������ ��� �������, ����� ���� ���������� �������� � ��������
    >>> convert_str('hello world')
    'hello world'
    >>> convert_str('HelLO WorlD')
    'hello world'
    >>> convert_str('Hello, world!')
    'hello world'
    >>> convert_str('hello ��� world')
    'hello  world'
    >>> convert_str('HelLO# ���$ WorlD!!')
    'hello  world'
    '''

    new_str = re.compile('[^a-zA-Z ]')
    res = new_str.sub('', text).lower()
    return res


if __name__ == '__main__':
    print(convert_str('HelLO# ���$ WorlD!!'))
    doctest.testmod(verbose=True)