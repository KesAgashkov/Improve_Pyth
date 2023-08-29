"""
Задание №3
? Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
? возврат строки без изменений
? возврат строки с преобразованием регистра без потери
символов
? возврат строки с удалением знаков пунктуации
? возврат строки с удалением букв других алфавитов
? возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""


from task_1 import convert_str
import unittest


class TestCaseName(unittest.TestCase):
    '''Тестирование функции convert_str'''

    def test_method(self):
        self.assertEqual(convert_str('hello world'), 'hello world')

        self.assertEqual(convert_str('HelLO WorlD'), 'hello world')

        self.assertEqual(convert_str('Hello, world!'), 'hello world')

        self.assertEqual(convert_str('hello мой world'), 'hello  world')

        self.assertEqual(convert_str('HelLO# мой$ WorlD!!'), 'hello  world')


if __name__ == '__main__':
    unittest.main(verbosity=2)

2