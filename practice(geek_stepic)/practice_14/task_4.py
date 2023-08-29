# Задание №5
# 📌 На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# 📌 Напишите 3-7 тестов unittest для данного класса.

from Rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):

    def test_1_area(self):
        self.assertEqual(Rectangle.get_area(Rectangle(7, 11)), 77)

    def test_2_perimeter(self):
        self.assertEqual(Rectangle.get_perimeter(Rectangle(5, 10)), 30)

    def test_sub(self):
        self.assertEqual(str(Rectangle(7, 11) - Rectangle(5, 10)), 'Прямоугольник со сторонами 6 и 6')

    def test_sum(self):
        self.assertEqual(str(Rectangle(7, 11) + Rectangle(5, 10)), 'Прямоугольник со сторонами 66 и 66')

    def test_gt(self):
        self.assertEqual((Rectangle(7, 11) > Rectangle(5, 10)), True)

    def test_lt(self):
        self.assertEqual((Rectangle(7, 11) < Rectangle(5, 10)), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)