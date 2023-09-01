import pytest
from task_2_func import dat


def test_positiv_1():
    assert dat("25.04.2012") == True, "Ошибка"


def test_positiv_2():
    assert dat("29.02.2008") == True, "Ошибка"


def test_neg_day():
    assert dat("32.02.2008") == False, "Ошибка"


def test_neg_month():
    assert dat("15.15.2008") == False, "Ошибка"


def test_neg_year():
    assert dat("15.12.100000") == False, "Ошибка"


def test_catch_value_error():
    pytest.raises(ValueError, dat, "dsdsdsd")


if __name__ == '__main__':
    pytest.main(['-v'])
