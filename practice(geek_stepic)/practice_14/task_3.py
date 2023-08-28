"""
Задание №4
? Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
? возврат строки без изменений
? возврат строки с преобразованием регистра без потери
символов
? возврат строки с удалением знаков пунктуации
? возврат строки с удалением букв других алфавитов
? возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""

import pytest
from script14_1 import convert_str


def test_1():
    assert convert_str('hello world') == 'hello world', 'ошибка тест 1'

def test_2():
    assert convert_str('HelLO WorlD') == 'hello world', 'ошибка тест 2'

    assert convert_str('Hello, world!') == 'hello world', 'ошибка тест 3'

def test_4():
    assert convert_str('hello мой world') == 'hello  world', 'ошибка тест 4'

def test_5():
    assert convert_str('HelLO# мой$ WorlD!!') == 'hello  world', 'ошибка тест 5'


if __name__ == '__main__':
    pytest.main(['-v'])