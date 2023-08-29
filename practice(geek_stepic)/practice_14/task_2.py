"""
������� �3
? �������� ��� ������ 1 ����� unittest. ���������
��������� ��������:
? ������� ������ ��� ���������
? ������� ������ � ��������������� �������� ��� ������
��������
? ������� ������ � ��������� ������ ����������
? ������� ������ � ��������� ���� ������ ���������
? ������� ������ � ������ ���� ����������������� �������
(����� �. 1)
"""


from task_1 import convert_str
import unittest


class TestCaseName(unittest.TestCase):
    '''������������ ������� convert_str'''

    def test_method(self):
        self.assertEqual(convert_str('hello world'), 'hello world')

        self.assertEqual(convert_str('HelLO WorlD'), 'hello world')

        self.assertEqual(convert_str('Hello, world!'), 'hello world')

        self.assertEqual(convert_str('hello ��� world'), 'hello  world')

        self.assertEqual(convert_str('HelLO# ���$ WorlD!!'), 'hello  world')


if __name__ == '__main__':
    unittest.main(verbosity=2)

2