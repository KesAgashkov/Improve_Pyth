from task_1_doc import new
from task_1_func import horse_move
import pytest

def test_pos():
    assert horse_move(4, 4) == new, "Ошибка. Позиции ходов отображены не верно"

def test_neg1():
    with pytest.raises(ValueError):
        horse_move("dsdsds", 6)

def test_neg2():
    pytest.raises(ValueError, horse_move, 6, "fdfdfd")

def test_out_board_1():
    assert horse_move(10, 4) == "Выход за пределы доски", "Не появилось ошибки"

def test_out_board_2():
    assert horse_move(4, 10) == "Выход за пределы доски", "Ошибка"

if __name__ == '__main__':
    pytest.main(['-v'])
