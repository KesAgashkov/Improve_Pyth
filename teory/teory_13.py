# # Рассмотрим вариант обработки ошибки в нашем коде:
# def get(text: str = None) -> int:
#     data = input(text)
#     try:
#         num = int(data)
#     except ValueError as e:
#         print(f'Ваш ввод привёл к ошибке ValueError: {e}')
#         num = 1
#         print(f'Будем считать результатом ввода число {num}')
#     return num
#
#
# # if __name__ == '__main__':
# #     number = get('Введите целый делитель: ')
# #     print(f'100 / {number} = {100 / number}')
#
#
# def hundred_div_num(text: str = None) -> tuple[int, float]:
#     while True:
#         try:
#             num = int(input(text))
#             div = 100 / num
#             break
#         except ValueError as e:
#             print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'f'Попробуйте снова')
#         except ZeroDivisionError as e:
#             div = float('inf')
#             break
#     return num, div
#
#
# # if __name__ == '__main__':
# #     n, d = hundred_div_num('Введите целый делитель: ')
# #     print(f'Результат операции: "100 / {n} = {d}"')
#
#
#
# # Команда finally
# # Ещё одна команда для обработки исключений — finally. Она срабатывает во всех
# # случаях. И если была ошибка и отработал блок except. И если ошибки не было.
# def get(text: str = None) -> int:
#     num = None
#     try:
#         num = int(input(text))
#     except ValueError as e:
#         print(f'Ваш ввод привёл к ошибке ValueError: {e}')
#     finally:
#         return num if isinstance(num, int) else 1
#
#
# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     try:
#         print(f'100 / {number} = {100 / number}')
#     except ZeroDivisionError as e:
#         print(f'На ноль делить нельзя. Получим {e}')



from class_my_exception_13 import UserNameError, UserAgeError


class User:
    MIN_LEN = 6
    MAX_LEN = 30

    def __init__(self, name, age):
        if self.MIN_LEN < len(name) < self.MAX_LEN:
            self.name = name
        else:
            raise UserNameError(name, self.MIN_LEN, self.MAX_LEN)
        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError(age)
        else:
            self.age = age


user = User('Яковffff', "12")


