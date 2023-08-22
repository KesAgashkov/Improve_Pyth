import csv
from functools import reduce


# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых

class Validator:
    def __init__(self, name):
        self.name = name

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, name):
        if not self.name.isalpha() and not self.name.istitle():
            raise ValueError('Атрибут "Name" должен начинаться с заглавной буквы и состоять только из букв')
        else:
            setattr(instance, self.param_name, name)


class Student:
    """Класс позволяет создавать эксземпляры с атрибутами id, имени, предмета, оценки по предмету и оценки по тесту
    Методы класса позволяют рассчитать среднюю арифметическую оценку по выбранному предмету
    (общая оценка и оценка по тесту), а также рассчитать среднюю арифметическую оценку по всем предметам"""

    def get_data():
        """Функция считывает данные по ученикам из файла csv и возвращает итератор"""
        with open('hw_12_data_stud.csv', 'r', encoding="windows-1251", errors='ignore') as c:
            c_read = csv.reader(c)
            res = list(c_read)
            result = []
            for i in range(1, len(res)):
                result.append(res[i])
            return iter(result)

    name = Validator(next(get_data())[1])

    def __init__(self, sp):
        self.id = int(sp[0])
        self.name = sp[1]
        self.subject = sp[2]
        self.sub_grade = int(sp[3])
        self.test_grade = int(sp[4])

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, subject: {self.subject}, subject_grade: {self.sub_grade}, test_grade: {self.test_grade}'

    def get_info_average_subj_grage(subj: str):
        """Функция возвращает среднюю оценку учащихся по предмету"""
        temp = list((Student.get_data()))
        temp = list(filter(lambda x: x[2] == subj, temp))
        if len(temp):
            print(f"Успешно: средняя оценка по предмету {subj}", end=": ")
            return round(sum(map(lambda x: int(x[3]), temp)) / len(temp), 2)
        else:
            print("Таких предметов не найдено. Попробуйте еще раз")

    def get_info_average_test_grage(subj: str):
        """Функция возвращает средний балл учащихся по предмету"""
        temp = list((Student.get_data()))
        temp = list(filter(lambda x: x[2] == subj, temp))
        if len(temp):
            print(f"Успешно: средняя оценка по тестам по предмету {subj}", end=": ")
            return round(sum(map(lambda x: int(x[4]), temp)) / len(temp), 2)
        else:
            print("Таких предметов не найдено. Попробуйте еще раз")

    def get_info_average_grage_all_subj():
        temp = list((Student.get_data()))
        if len(temp):
            print(f"Успешно: общая оценка по всем предметам", end=": ")
            return round(sum(map(lambda x: int(x[3]), temp)) / len(temp), 2)
        else:
            print("Журнал пустой")


if __name__ == '__main__':
    s1 = Student(next(Student.get_data()))
    print(s1)
    print(Student.get_info_average_subj_grage("География"))
    print(Student.get_info_average_test_grage("Физика"))
    print(Student.get_info_average_grage_all_subj())
