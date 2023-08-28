from people_access import AccessErr, LevelErr
import json


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
        with open('js.json', 'r', encoding='Windows-1251') as js_f:
            user_dict = json.load(js_f)
        for level, user_list in user_dict.items():
            for id, name in user_list.items():
                CheckUserLogin.user_group.append(User(name, id, level))

    def create_user(self, name, id, level):
        a_name, a_id = input("Введите пользователя и id через пробел:> ").split()
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
        # try:
        for user in CheckUserLogin.user_group:
            if login_user == user:
                return user.level
        else:
            raise AccessErr(name)
        # except AccessErr as e:
        #     print("Произошла ошибка", e)


# if __name__ == '__main__':
#     # group = CheckUserLogin()
#     # print(*group.user_group)
#     # print(group.get_login_level('Новинков', '16'))