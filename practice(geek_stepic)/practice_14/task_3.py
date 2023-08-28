"""
������� �4
? �������� ��� ������ 1 ����� pytest. ��������� ���������
��������:
? ������� ������ ��� ���������
? ������� ������ � ��������������� �������� ��� ������
��������
? ������� ������ � ��������� ������ ����������
? ������� ������ � ��������� ���� ������ ���������
? ������� ������ � ������ ���� ����������������� �������
(����� �. 1)
"""

import pytest
from script14_1 import convert_str


def test_1():
    assert convert_str('hello world') == 'hello world', '������ ���� 1'

def test_2():
    assert convert_str('HelLO WorlD') == 'hello world', '������ ���� 2'

    assert convert_str('Hello, world!') == 'hello world', '������ ���� 3'

def test_4():
    assert convert_str('hello ��� world') == 'hello  world', '������ ���� 4'

def test_5():
    assert convert_str('HelLO# ���$ WorlD!!') == 'hello  world', '������ ���� 5'


if __name__ == '__main__':
    pytest.main(['-v'])