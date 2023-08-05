# import json
# import csv
# # принимаем в виде файла
# with open ("js.json", "r", encoding="utf-8") as j:
#     # print(type(j))
#     data = json.load(j)
# # print(type(data))
# # for el in data:
# #     print(el)
# #
# # print(data["members"])
#
# # принимаем в виде текста
# data2 = """
# [
#   {
#     "name": "Molecule Man",
#     "age": 29,
#     "secretIdentity": "Dan Jukes",
#     "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
#   },
#   {
#     "name": "Madame Uppercut",
#     "age": 39,
#     "secretIdentity": "Jane Wilson",
#     "powers": [
#       "Million tonne punch",
#       "Damage resistance",
#       "Superhuman reflexes"
#     ]
#   }
# ]
# """
#
# # data2 = json.loads(data2)
# # print(data2)
# # print(type(data2))
#
# # Обратно в json
#
# data3 = [
#     {
#         "value": "Иванов Виктор",
#         "unrestricted_value": "Иванов Виктор",
#         "data": {
#             "surname": "Иванов",
#             "name": "Виктор",
#             "patronymic": None,
#             "gender": "MALE"
#         }
#     },
#     {
#         "value": "Иванченко Виктор",
#         "unrestricted_value": "Иванченко Виктор",
#         "data": {
#             "surname": "Иванченко",
#             "name": "Виктор",
#             "patronymic": None,
#             "gender": "MALE"
#         }
#     },
#     {
#         "value": "Виктор Иванович",
#         "unrestricted_value": "Виктор Иванович",
#         "data": {
#             "surname": None,
#             "name": "Виктор",
#             "patronymic": "Иванович",
#             "gender": "MALE"
#         }
#     }
# ]
#
# #Сохраняем инфу в файл (принимает два аргумента что преобразуем и в какой файл)
# with open('new.json', 'w', encoding='utf-8') as d:
#     json.dump(data3,d, ensure_ascii = False)
#
# #Сохраняем инфу в виде текста
#
# text = json.dumps(data3, indent=3)
# print(text)
#
# # чтение csv
#
# with open('te.csv', 'r', newline='') as c:
#     csv_file = csv.reader(c)
#     for el in csv_file:
#         print(el)
#
# #запись csv
# with (
# open('biostats_tab.csv', 'r', newline='') as f_read,
# open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write
# ):
#     csv_read = csv.reader(f_read, dialect='excel-tab',quoting=csv.QUOTE_NONNUMERIC)
#     csv_write = csv.writer(f_write, dialect='excel', delimiter='', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     all_data = []
#     for i, line in enumerate(csv_read):
#         if i == 0:
#             csv_write.writerow(line)
#         else:
#             line[2] += 1
#     for j in range(2, 4 + 1):
#         line[j] = int(line[j])
#         all_data.append(line)
#         csv_write.writerows(all_data)
#
#
# #Запись в словарь
#
# with open('biostats_tab.csv', 'r', newline='') as f:
#     csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"],\
#                               restkey="new", restval="MainOffice", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(f'{line = }')
#         print(f'{line["name"] = }\t{line["age"] = }')
#
#
# # Запись из словаря
#
# import csv
# from typing import Iterator
# with (
# open('biostats_tab.csv', 'r', newline='') as f_read,
# open('biostats_new.csv', 'w', newline='', encoding='utf-8') as f_write
# ):
#     csv_read: Iterator[dict] = csv.DictReader(f_read,
#     fieldnames=["name", "sex", "age", "height", "weight", "office"],
#     restval="MainOffice", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     csv_write = csv.DictWriter(f_write, fieldnames=["id", "name", "office", "sex", "age", "height", "weight"],
#     dialect='excel-tab', quoting=csv.QUOTE_ALL)
#     csv_write.writeheader()
#     all_data = []
#     for i, dict_row in enumerate(csv_read):
#         if i != 0:
#             dict_row['id'] = i
#             dict_row['age'] += 1
#             all_data.append(dict_row)
#             csv_write.writerows(all_data)



# cериализация в поток байт и десериализация из потока байт
import pickle
# import os
# res = pickle.loads(b"cos\nremove\n(S'new.txt'\ntR.") # при распаковке потока байт можно удалить файлы
# print(res)


# Преобразуем словарь из главы про JSON в набор байт средствами модуля pickle.

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование", "путешествия"],
    "age": 35,
    "children": [
                    {
                        "first_name": "Алиса",
                        "age": 5
                    },
                    {
                        "first_name": "Маруся",
                        "age": 3
                    }
                ]
    }
print(my_dict)
res = pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL)
print(f'{res = }')



import pickle
def func(a, b, c):
    return a + b + c
my_dict = {
    "numbers": [42, 4.1415, 7+3j],
    "functions": (func, sum, max),
    "others": {True, False, 'Hello world!'},
    }
with open('my_dict.pickle', 'wb') as f:
    pickle.dump(my_dict, f)



new_dict = pickle.loads(res)
print(f'{new_dict = }')


def func(a, b, c):
    return a * b * c
with open('my_dict.pickle', 'rb') as f:
    new_dict = pickle.load(f)
print(f'{new_dict = }')
print(f'{new_dict["functions"][0](2, 3, 4) = }')

