from .teory_14_doctest import is_prime
import pytest


def test_is_prime():
    assert not is_prime(42)
    assert is_prime(73)


def test_type():
    with pytest.raises(TypeError):
        is_prime(3.14)


def test_value():
    with pytest.raises(ValueError):
        is_prime(-100)


def test_value_with_text():
    with pytest.raises(ValueError, match=r'The number P must be greater than 1'):
        is_prime(1)


def test_warning_false(capfd):
    is_prime(100_000_001)
    captured = capfd.readouterr()
    assert captured.out == 'If the number P is prime, the check may take a long time. Working...\n'


def test_warning_true(capfd):
    is_prime(100_000_007)
    captured = capfd.readouterr()
    assert captured.out == 'If the number P is prime, the check may take a long time. Working...\n'


if __name__ == '__main__':
    pytest.main()


#Пример использования фикстур
# import pytest
# @pytest.fixture
# def data():
#     return [2, 3, 5, 7]
# def test_append(data):
#     data.append(11)
#     assert data == [2, 3, 5, 7, 11]
# def test_remove(data):
#     data.remove(5)
#     assert data == [2, 3, 7]
# def test_pop(data):
#     data.pop()
#     assert data == [2, 3, 5]
#
#
# if __name__ == '__main__':
#     pytest.main(['-v'])
