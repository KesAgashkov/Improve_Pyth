a = True
b = 10
c = 10.0
d = [1, 2, 3]
print(type(a))
print(id(a))
print(isinstance(a, (int, str, float)))
print(b is c)  # сравнение типов объектов
print(hash(a))  # c помощью хэша можем узнать является ли тип изменяемым или неизменяемым


def info_obj():
    value = input()
    print(type(value))
    print(id(value))
    print(hash(value))


a: int = 10  # так выглядит анотация для разработчиков/ ide подсказывает если переменной присвоен другой тип
b: int | str = 10 # можно и так сделать
b = "dsdsd"
print(a)


def func(data: list[int | float]) -> int: #пример анотации для функции/ ide подсвечивает ввод данных другого типа
    print("ok")
    return data

# print(func([10]))

# Атрибуты и методы объекта
print (str.__doc__)
print (dir(str)) #могу узнать об атрибутах и методах класса кратко

help(str) # полная инфа по методам класса

# help() #вход в интерактивный справочный режим

k=10
print(bin(k))
print(oct(k))
print(hex(k))
print(int("k", base=35))


# text = "dsdsdsds"
# print(text.__sizeof__())
# print(text.__len__())
# print(text.count(0))

num = input()
if len(num)<4:
    print(num)
elif len(num)%3 == 0:
    num = num.split('')
    for i in range(2,len(num)-2,3):
        num.insert(i)
    print(num.join())
