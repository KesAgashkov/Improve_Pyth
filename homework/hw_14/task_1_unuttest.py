import io
from unittest.mock import patch
from task_1_func import horse_move
import unittest


class TestCaseHorse_Move(unittest.TestCase):
    '''Тестирование функции horse_move'''

    def test_positiv(self):
        self.assertEqual(horse_move(4, 4), [['.', '.', '.', '.', '.', '.', '.', '.'],
                                            ['.', '.', '.', '.', '.', '.', '.', '.'],
                                            ['.', '.', '*', '.', '*', '.', '.', '.'],
                                            ['.', '*', '.', '.', '.', '*', '.', '.'],
                                            ['.', '.', '.', 'H', '.', '.', '.', '.'],
                                            ['.', '*', '.', '.', '.', '*', '.', '.'],
                                            ['.', '.', '*', '.', '*', '.', '.', '.'],
                                            ['.', '.', '.', '.', '.', '.', '.', '.']], "Ошибка позиций")

    def test_neg1(self):
        self.assertRaises(TypeError, horse_move, ("dsds", 4))

    def test_neg2(self):
        self.assertRaises(TypeError, horse_move, (5, "dsdsd"))

    def test_out_board_1(self):
        self.assertEqual(horse_move(10, 4), "Выход за пределы доски", "Не сработала валидация выхода за границы")

    def test_out_board_2(self):
        self.assertEqual(horse_move(2, 15), "Выход за пределы доски", "Не сработала валидация выхода за границы")


if __name__ == '__main__':
    unittest.main(verbosity=2)
