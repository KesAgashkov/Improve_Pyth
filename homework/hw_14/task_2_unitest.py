import unittest
from task_2_func import dat


class TestCaseHorse_Move(unittest.TestCase):
    '''Тестирование функции dat'''

    def test_positiv_1(self):
        self.assertEqual(dat("25.04.2012"), True, "Ошибка")

    def test_positiv_2(self):
        self.assertEqual(dat("29.02.2008"), True, "Ошибка")

    def test_neg_day(self):
        self.assertEqual(dat("32.02.2008"), False, "Ошибка")

    def test_neg_month(self):
        self.assertEqual(dat("15.15.2008"), False, "Ошибка")

    def test_neg_year(self):
        self.assertEqual(dat("15.12.100000"), False, "Ошибка")

    def test_catch_value_error(self):
        with self.assertRaises(ValueError):
            dat("blabla")


if __name__ == '__main__':
    unittest.main(verbosity=2)
