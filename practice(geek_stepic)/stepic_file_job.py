# file = open(input())
# print(file.read())
# file.close()
#
#
# file = open(input())
# print(file.readlines()[-2])
# file.close()
#
# import random
# file = open("lines.txt")
# dt = file.readlines()
# print(dt[random.randint(0,len(dt))])
# file.close()
#
#
# import random
# file = open("numbers.txt")
# dt = file.readlines()
# print(sum(list(map(int, dt))))
# file.close()
#
#
#
# import random
# file = open("nums.txt")
# dt = file.readlines()
# print(sum(list(map(lambda x: sum([int(el) for el in x.split()]), dt))))
# file.close()
#
# import random
# file = open("nums.txt")
# dt = file.readlines()
# print(sum(list(map(lambda x: sum([int(el) for el in x.split()]), dt))))
# file.close()
#
#
# file = open("prices.txt")
# dt = file.readlines()
# print(sum(list(map(lambda x: int(x.split('\t')[1])*int(x.split('\t')[2]), dt))))
# file.close()
#
#
# with open("text.txt") as f:
#     dt = f.read()
#     print(dt[::-1])
#
#
# with open("data.txt") as f:
#     dt = f.readlines()
#     for el in dt[::-1]:
#         print(el.strip())
#
#
#
# with open("lines.txt") as f:
#     dt = list(f.readlines())
#     ch = max(dt, key=len)
#     for el in dt:
#         if len(ch) == len(el):
#             print(el.strip())
#
#
# with open("numbers.txt") as f:
#     for el in f.readlines():
#         print(sum(list(map(int, el.split()))))
#
#
# with open("numbers.txt") as f:
#     for el in f.readlines():
#         print(sum(map(int, el.split())))
#
#
# import re
# with open("file.txt") as f:
#     res = f.read()
#     f.seek(0)
#     res1 = f.readlines()
#     match = re.findall(r'[a-zA-Z]', res)
#     print("Input file contains:")
#     print(f"{len(match)} letters")
#     print(f"{len(res.split())} words")
#     print(f"{len(res1)} lines")
#
#
#
# import random
# with open("first_names.txt") as f, open("last_names.txt") as l:
#     fir = f.readlines()
#     las = l.readlines()
#     for _ in range(3):
#         print(random.choice(fir).strip() + " " + random.choice(las).strip())
#
#
# with open("population.txt") as p:
#     res = p.readlines()
#     res = list(filter(lambda x: x.split("\t")[0].startswith('G') and int(x.split("\t")[1])>500_000, res))
#     for el in res:
#         print(el.split()[0])
#

# def read_csv():
#     with open("data.csv") as c:
#         file = c.readlines()
#         key = list(map(str.strip,file[0].split(",")))
#         print(key)
#         value = [el.strip().split(",") for el in file[1:]]
#         print(value)
#         dct = []
#         for el in value:
#             dct.append({k:v for k,v in zip(key,el)})
#         for el in dct:
#             print(el)
#
#
# read_csv()
#
#
# with open('books.txt', 'w', encoding='utf-8') as file:
#     li = '''Лев Толстой «Война и мир», Джордж Оруэлл «1984», Джеймс Джойс «Улисс», Владимир Набоков «Лолита», Уильям Фолкнер «Звук и ярость»'''.split(',')
#     file.writelines([f"{i.strip()}\n" for i in li])
#
#
# with open('output.txt', 'w') as o:
#     print(input(),file=o)
#
#
# from random import randint
# with open('random.txt', 'w') as r:
#     for _ in range(25):
#         r.write(f'{randint(111,777)}\n')
#
# from random import sample as r
#
# print(*r(range(111, 778), 25), file=open('random.txt', 'w'), sep='\n')
#
#
#
# from random import randint
# with open('input.txt', ) as inp, open("output.txt", "w") as out:
#     data = inp.readlines()
#     for i, v in enumerate(data,1):
#         out.write(f"{i}) {v}")
#
#
#
# from random import randint
# with open('class_scores.txt', ) as inp, open("new_scores.txt", "w") as out:
#     data = inp.readlines()
#     for el in data:
#         if int(el.strip().split()[1]) == 100:
#             out.write(el)
#         elif int(el.strip().split()[1])+5 >=100:
#             out.write(f"{el.strip().split()[0]} {100}\n")
#         else:
#             out.write(f"{el.strip().split()[0]} {int(el.strip().split()[1])+5}\n")
#


with open('goats.txt') as inp, open("answer.txt", "w") as out:
    data = inp.readlines()
    ind = data.index("GOATS\n")
    l = len(data[ind+1:])
    print(l)
    print(data[ind + 1:])
    dct = []
    count = 0
    for col in data[1:ind]:
        for el in data[ind:]:
            if col==el:
                count+=1
        dct.append(f'{col.strip()} {count}')
        count = 0
    dct = sorted(dct, key=lambda x: int(x.split()[2]))
    print(dct)
    for el in dct:
        if int(el.split()[2])/l * 100 > 7.1:
            out.write(f'{el.split()[0]} {el.split()[1]}\n')

