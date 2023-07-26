from datetime import datetime
# Задание 1
# Напишите функцию для транспонирования матрицы
def transp_matrix(lst: list[list]):
    res = []
    if lst:
        res = [[lst[j][i] for j in range(len(lst[0]))] for i in range(len(lst))]
        return res
    else:
        print("Введенная матрица пустая")
        return res


lst = [[3, 8, 5], [4, 9, 1], [3, 4, 0]]


def look_matrix(matr):
    for el in matr:
        print(*el)
    print()


# look_matrix(lst)
# look_matrix(transp_matrix(lst))


# Задание 2
# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного
# аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def get_dict(**kwargs) -> dict:
    dct = dict()
    for key, el in kwargs.items():
        try :
            dct[el] = key
        except(TypeError):
            dct[str(el)] = key
    return dct


tup = (13, 16, 8, 9, 78)
lst2 = [13, 16, 8, 9, 78]

# print(get_dict(a = [], b = 15, c = 30, d = {}))

# Задание 3
# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


def start_atm(summ: int):
    count_add = 0
    count_out = 0
    bonus = 0
    lst_res = []

    while True:
        print("Ваша Сумма: ", summ)
        if summ > 5_000_000:
            summ = tax_rich(summ,lst_res)
        action = input("Действие: ")
        if action == "q":
            print("Выходим из банкомата")
            print("Сумма: ", summ)
            break
        elif action == "a":
            summ = add_money(summ, lst_res, count_add)
        elif action == "o":
            summ = withdraw_money(summ, lst_res, count_out)
        if action == "v":
            print(*lst_res, sep="\n")


def tax_rich(summ, lst_res):
    print("С вас сняли налог на богатство", summ * 0.1)
    lst_res.append(f"{datetime.now()} : Налог на богатство: -{summ * 0.1}. Баланс: {summ * 0.9}")
    summ *= 0.9
    return summ

def add_money(summ, lst_res, count_add):
    summ_add = int(input("Сумма: "))
    if summ_add % 50 == 0:
        summ += summ_add
        count_add += 1
        lst_res.append(f"{datetime.now()} : Внесение средств: {summ_add}. Баланс: {summ}")
        if count_add % 3 == 0:
            bonus = summ*0.03
            summ *= 1.03
            lst_res.append(f"{datetime.now()} : Бонус за пользование сервисом: {bonus}. Баланс: {summ}")
        return summ
    else:
        print("Введена некорректная сумма (не кратна 50)")
        return summ

def withdraw_money(summ, lst_res, count_out):
    summ_out = int(input("Сумма: "))
    comission = summ_out * 0.015
    if comission < 30:
        comission = 30
    elif comission > 600:
        comission = 600

    if summ_out + comission > summ:
        print("Недостаточно средств")
        return summ
    else:
        if summ_out % 50 == 0:
            summ -= summ_out + comission
            lst_res.append(f"{datetime.now()} : Снятие средств: {summ_out + comission}. Баланс: {summ}")
            count_out += 1
            if count_out % 3 == 0:
                bonus = summ * 0.03
                summ *= 1.03
                lst_res.append(f"{datetime.now()} : Бонус за пользование сервисом: {bonus}. Баланс: {summ}")
            return summ
        else:
            print("Введена некорректная сумма")
            return summ


# start_atm(500)