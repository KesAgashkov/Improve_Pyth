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

#
# with open('goats.txt') as inp, open("answer.txt", "w") as out:
#     data = inp.readlines()
#     ind = data.index("GOATS\n")
#     l = len(data[ind+1:])
#     print(l)
#     print(data[ind + 1:])
#     dct = []
#     count = 0
#     for col in data[1:ind]:
#         for el in data[ind:]:
#             if col==el:
#                 count+=1
#         dct.append(f'{col.strip()} {count}')
#         count = 0
#     dct = sorted(dct, key=lambda x: int(x.split()[2]))
#     print(dct)
#     for el in dct:
#         if int(el.split()[2])/l * 100 > 7.1:
#             out.write(f'{el.split()[0]} {el.split()[1]}\n')
#
#
#
# with open('output.txt', 'a') as out:
#     for _ in range(int(input())):
#         with open(input()) as inp:
#              print(inp.read(),file=out, end="")




# with open('output.txt', 'w') as out, open("logfile.txt", "r", encoding='utf-8') as log:
#     data = log.readlines()
#     res = []
#     for el in data:
#         el = el.split(',')
#         st = int(el[1].split(':')[0])*60 + int(el[1].split(':')[1])
#         stop = int(el[2].split(':')[0])*60 + int(el[2].split(':')[1])
#         if stop - st >= 60:
#             res.append(el[0])
#     for i in range(len(res)):
#         if i == len(res)-1:
#             out.write(res[i])
#         else:
#             out.write(res[i]+"\n")
#
#
# with open(input()) as inp:
#     print(len(inp.readlines()))
#
#
# with open("ledger.txt") as inp:
#     data = inp.readlines()
#     print(f'${sum(list(map(lambda x: int(x[1:]),data)))}')
#

# with open("grades.txt") as inp:
#     data = inp.readlines()
#     print(len(list(filter(lambda x: int(x.split()[1]) > 64 and int(x.split()[2]) > 64 and int(x.split()[3]) > 64, data))))
#     size = max(data,key=len)
#     print(size)
#

# with open("words.txt") as inp:
#     data = inp.read().split()
#     size = len(max(data,key=len))
#     print(*list(filter(lambda x: len(x)==size, data)), sep="\n")



# with open(input()) as inp:
#     data = inp.readlines()
#     for i in range(len(data)-10,len(data)):
#         print(data[i])
#
#
#
# with open(input()) as inp:
#     data = inp.readlines()
#     data = list(map(lambda x: x.strip(), data))
#     if len(data)>10:
#         print(*data[-10:], sep='\n')
#     else:
#         print(*data, sep='\n')
#
# with open("data_new.txt") as inp, open("forbidden_words.txt") as fo:
#     new = []
#     temp = ''
#     data1 = inp.read().split()
#     print(data1)
#     data2 = fo.read().split()
#     for el1 in data1:
#         for el2 in data2:
#             if el2 in el1.lower().strip():
#                 size = len(el2)
#                 if temp.endswith("\n"):
#                     temp = '*' * size + el1[size:]+"\n"
#                 else:
#                     temp = '*' * size + el1[size:]
#                 break
#             else:
#                 temp = el1
#                 print(temp,sep='')
#         print(temp,sep='')


#
# with open("cyrillic.txt", encoding="utf-8") as file, open("transliteration.txt", "w") as out:
#     text = file.read()
#     d = {
#     'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
#     'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
#     'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
#     'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya',
#     'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch',
#     'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*',
#     'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je',
#     'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya',
#     }
#     res = ''
#     for ch in text:
#         try:
#             res += d[ch]
#         except:
#             res += ch
#
#     out.write(res)




with open(input())as c:
    data = c.readlines()
    data.insert(0,"empty\n")
    res = []
    for i in range(1, len(data)):
        if data[i].startswith("def") and not data[i-1].startswith("#"):
            res.append(data[i].split()[1].split("(")[0])
        else:
            pass

    if len(res) != 0:
        for el in res:
            print(el)
    else:
        print("Best Programming Team")



