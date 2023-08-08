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


# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'.split()
#
# result = {int(el.split(":")[0]): el.split(":")[1] for el in s}


# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
#
# result = {i: [j for j in range(1, i+1) if i%j ==0] for i in numbers}


# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#
# result = {w: [ord(j) for j in w] for w in words}
# print(result)
#
#
# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
#
# result = {k: v for k,v in letters.items() if k not in remove_keys}
#
#
# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {k: v for k,v in students.items() if v[0]>167 and v[1]<75}
#
#
# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
#
# result = {el[0]:(el[1],el[2]) for el in tuples}
#
#
#
# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
#
# result = [{k: {n: g}} for k,n,g in zip(student_ids, student_names, student_grades)]
#
#
# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
# my_dict = {k: [el for el in v if el<=20] for k,v in my_dict.items()}
#
#
# dct = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
# print(*[dct[el] for el in input()], sep="")
#
#
# d = str.maketrans({'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'})
# s = input()
# print(s.translate(d))
#
#
# d = {'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3,
#      'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}
# res = 0
# for l in input():
#     res += d[l]
# print(res)
#
# d = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }
# sum = 0
# for el in input():
#     for k in d:
#         if el in d[k]:
#             sum += k
#             break
# print(sum)
#
#
# def build_query_string(params):
#     sp = []
#     for k, v in params.items():
#         sp.append(k + "=" + str(v))
#
#     return "&".join(sorted(sp))



# n = int(input())
# dct1={}
# check =  {'write' : 'W', 'read': 'R', 'execute': 'X'}
# for i in range(n):
#     fir,*sec = input().split()
#     dct1[fir] = sec
# m = int(input())
# for i in range(m):
#     oper, filename = input().split()
#     if filename in dct1 and check[oper] in dct1[filename]:
#         print("OK")
#     else:
#         print("Access denied")



data = {}
for i in range(int(input())):
    name, product, count = input().split()
    data.setdefault(name, {})
    data[name][product] = data[name].setdefault(product, 0) + int(count)

for name in sorted(data):
    print(name + ":", sep="\n")
    for pos in sorted(data[name]):
        print(pos, data[name][pos])