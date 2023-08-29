# Задание №6
# 📌 На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# 📌 Напишите 3-7 тестов pytest для данного проекта.
# 📌 Используйте фикстуры.


import pytest
from people_access import AccessErr, LevelErr
from people import CheckUserLogin


@pytest.fixture()
def set_up():
    return CheckUserLogin()


def test_access(set_up):
    assert set_up.get_login_level('Новиков', '06') == '7'


def test_exception(set_up):
    with pytest.raises(AccessErr):
        set_up.get_login_level('Новинков', '16')


if __name__ == '__main__':
    pytest.main(['-v'])