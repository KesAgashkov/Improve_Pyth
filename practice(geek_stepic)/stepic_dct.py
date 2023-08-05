# info_list = [[frozenset("dsdsdsds"), 'Gerasim'], ['age', 45], ['job', 'Janitor']]
# info_dict = dict(info_list)
# print(info_dict)
#
# # sorted(my_dict.items(), key=lambda x:(-x[1], x[0]))
#
#
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# sp = []
# for el in users:
#     if el["phone"][-1] == "8":
#         sp.append(el["name"])
# print(*sorted(sp))
#
#
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# sp = []
# for el in users:
#     if "email" not in el or el["email"] == "":
#         sp.append(el["name"])
# print(*sorted(sp))
#
#
# sp = list(input())
# d = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine"
# }
# for el in sp:
#     print(d[int(el)], end=" ")
#
#
#
# k = input()
# d= {'CS101': {'audience_number': '3004', 'teacher': 'Хайнс', 'time': '8:00'},
# 'CS102': {'audience_number': '4501', 'teacher': 'Альварадо', 'time': '9:00'},
# 'CS103': {'audience_number': '6755', 'teacher': 'Рич', 'time': '10:00'},
# 'NT110': {'audience_number': '1244', 'teacher': 'Берк', 'time': '11:00'},
# 'CM241': {'audience_number': '1411', 'teacher': 'Ли', 'time': '13:00'}}
# for key,v in d.items():
#     if key == k:
#         print(f"{k}: {v['audience_number']}, {v['teacher']}, {v['time']}")
#
#
#
# text = input().upper().replace('"', '')
# res = ""
# d = {
#     "1": ".,?!:",
#     "2": "ABC",
#     "3": "DEF",
#     "4": "GHI",
#     "5": "JKL",
#     "6": "MNO",
#     "7": "PQRS",
#     "8": "TUV",
#     "9": "WXYZ",
#     "0": " "
# }
# for ch in text:
#     for k, v in d.items():
#         if ch in v:
#             tap = v.index(ch) + 1
#             res += k * tap
#             break
# print(res)
#
#
#
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
#          '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
#          '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# dct = dict(zip(letters, morse))
#
# text = input().upper().replace(" ", "").replace(",", "").replace("!", "").replace("+", "").replace("=", "").replace("?",
#                                                                                                                     "").replace(
#     ".", "").replace("-", "")
#
# for ch in text:
#     print(dct[ch], end=" ")
#
#
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
# result = {}
# for num in numbers:
#     if num not in result:
#         result[num] = 1
#     else:
#         result[num] += 1
#
#
# result = {i: i*i for i in range(1,16)}
#
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
# result = {}
# for ch in text:
#     if ch in result:
#         result[ch] += 1
#     else:
#         result[ch] = 1
#
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# result = {}
# for letter in set(text):
#     result[letter] = text.count(letter)

# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'.split()
# result = {}
# for word in set(s):
#     result[word] = s.count(word)
#
# result =[k for k, v in result.items() if v==max(result.values())]
# print(sorted(result)[0])
#
#
# result = {l: s.split().count(l) for l in set(s.split())}
#
# print(min(l for l in result if result[l]==max(result.values())))
#
#
# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
# result ={}
# for el in pets:
#     result.setdefault(el[1:], []).append(el[0])
#
#
# lst = [word.strip('.,!?:;-') for word in input().lower().split()]
# res = {}
# for word in lst:
#     res[word]=(lst.count(word))
# print(min(res.items(), key=lambda x: (x[1],x[0]))[0])



# lst = input().split()
# d = {}
# for el in lst:
#     d[el] = d.get(el, 0) + 1
#     if d[el]==1:
#         print(el, end=" ")
#     elif d[el] > 1:
#         print(el +"_"+str(d[el]-1))

# dct = {}
# for _ in range(int(input())):
#     k, v = input().split(": ")
#     k = k.lower()
#     dct[k] = v
#
# for _ in range(int(input())):
#     word = input().lower()
#     if word in dct:
#         print(dct[word])
#     else:
#         print("Не найдено")
#
#
# print("YES" if sorted(input())==sorted(input()) else "NO")
#
#
#
# dct = {}
# for _ in range(int(input())):
#     k, v = input().split()
#     dct[v] = k
# word = input()
# for k,v in dct.items():
#     if word in dct:
#          print(dct[word])
#          break
#     elif v == word:
#          print(k)
#
#
# dct = {}
# for _ in range(int(input())):
#     k, *v = input().split()
#     dct[k] = v
# for _ in range(int(input())):
#     word = input()
#     for k, v in dct.items():
#         if word in v:
#             print(k)


# dct = {}
# for _ in range(int(input())):
#     ph, name = input().split()
#     name = name.lower()
#     dct[name] = dct.get(name, []) + [ph]
#
# for i in range(int(input())):
#     sear = input().lower()
#     if sear in dct:
#         print(*dct[sear])
#     else:
#         print("абонент не найден")


# dct1 = {}
# dct2 = {}
# inp = input()
# res = ""
# for el in inp:
#     dct1[el] = dct1.get(el, 0) + 1
#
# for el in inp:
#     res += str(dct1[el])
#
# for i in range(int(input())):
#     k, v = input().split(": ")
#     dct2[v] = k
#
# for k in res:
#     print(dct2[k], end="")


# squares = {i: {j: j**2 for j in range(i + 1)} for i in range(5)}
#
# for value in squares.values():
#     print(value)