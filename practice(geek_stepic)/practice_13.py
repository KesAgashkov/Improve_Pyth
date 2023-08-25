"""
������� �1
? �������� �������, ������� ����������� �������� ������ ��
������������ �� ��� ���, ���� �� �� ����� ����� ���
������������ �����.
? ������������� �� �������� ������ ��� ����������.
"""


def get_number():
    while True:
        num = input('������� �����:> ')
        try:
            return int(num)
        except ValueError as e:
            try:
                return float(num)
            except ValueError as e:
                print(f'�������� ������ �����, {e}')


# print(get_number())


"""
������� �2
? �������� ������� ������ get ��� �������.
? ������ ������ ������� ������� ��������� ���� �
�������� �� ���������.
? ��� ��������� � ��������������� ����� ������� ������
���������� ��������� ��������.
? ���������� ������ ����� ��������� ����������.
"""

my_dict = {1: "����", 2: "����������", 3: "��� ����", 4: "��� ����������"}


def get_dict(my_dct, key, value="��� ��������"):
    try:
        return my_dct[key]
    except KeyError:
        return value


print(get_dict(my_dict, 4))
print(get_dict(my_dict, 7))


"""
������� �3
? �������� ����� � ������� ����������� � �������� ������-
����������:
? ������ ������,
? ������ �������.
"""

MIN_LEVEL = 5


class BasedExep(Exception):
    pass


class LevelErr(BasedExep):
    def __init__(self, value, need_value):
        self.value = value
        self.need_value = need_value

    def __str__(self):
        return f"������ ������ - level={self.value} ������ ������������ ������)"


class AccessErr(BasedExep):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'������ �������'


if __name__ == '__main__':
    try:
        num = int(input('������� ����� �����:> '))
        if num < 1:
            raise AccessErr(num)
        if num < MIN_LEVEL:
            raise LevelErr(num, MIN_LEVEL)
    except LevelErr as e:
        print(e)
    except AccessErr as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        print('������ ��������')


"""
������� �4
? ���������� ������ �� �������� 8 ��� ������������ ������,
��� � ����������� ����� ����������� ���, ������
������������� � ������� ������� (�� 1 �� 7) ��������
���������� � JSON ����.
? �������� ����� ������������, ������� ������ ��� ������ �
��������� ����������.
? �������� �������� �������, ������� ��������� ����������
�� JSON ����� � ��������� ��������� �������������.
"""


import json

class User:
    def __init__(self, name: str, user_id: str,  level: str = '0') -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'User:{self.name}, id:{self.user_id},  level:{self.level}'


user_group = set()
def load_users(path):
    with open(path, 'r', encoding='UTF-8') as js_f:
        user_dict = json.load(js_f)
    for level, user_list in user_dict.items():
        for id, name in user_list.items():
            user_group.add(User(name, id, level))


if __name__ == '__main__':

    load_users('data_prac_13.json')
    print(*user_group)

    # for el in user_group:
    #     print(el)


"""
������� �5
? ���������� ������ 3 � 4. �������� ����� �������, �������
����� ��������� ������:
? �������� ������ (������� �� ������� 4)
? ���� � ������� - ������� ������� ��� � id ������������. ���
�������� ������� ������������ � ��������� �����������
���������� ����� �������� �� ��������� �������������.
���� ������ ������������ ���, ��������� ����������
�������. � ���� ������������ ����, �������� ��� ������� ��
��������� �������������.
? ���������� ������������. ���� ������� ������������
������, ��� ��� �������, ��������� ���������� ������
�������.
"""



class User:
    def __init__(self, name: str, user_id: str, level: str = '0') -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id

    def __str__(self):
        return f'User:{self.name}, id:{self.user_id}, level:{self.level}|'


class CheckUserLogin:
    user_group = []

    def __init__(self):
        CheckUserLogin.load_users()
        pass

    @staticmethod
    def load_users():
        with open('task13_4.json', 'r', encoding='UTF-8') as js_f:
            user_dict = json.load(js_f)
        for level, user_list in user_dict.items():
            for id, name in user_list.items():
                CheckUserLogin.user_group.append(User(name, id, level))

    def create_user(self, name, id, level):
        a_name, a_id = input("������� ������������ � id ����� ������:> ").split()
        if current_level := self.get_login_level(a_name, a_id):
            try:
                if int(current_level) > int(level):
                    CheckUserLogin.user_group.append(User(name, id, level))
                    return User(name, id, level)
                else:
                    raise LevelErr(current_level, level)
            except LevelErr as e:
                print(e)

    def get_login_level(self, name, id):
        login_user = User(name, id)
        try:
            for user in CheckUserLogin.user_group:
                if login_user == user:
                    return user.level
            else:
                raise AccessErr(name)
        except AccessErr as e:
            print(e)


if __name__ == '__main__':
    group = CheckUserLogin()
    print(*group.user_group)
    print()
    print(group.create_user('��������', "08", 5))
    print()
    print(*group.user_group)



