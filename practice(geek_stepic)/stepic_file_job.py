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

import re
with open("file.txt") as f:
    res = f.read()
    f.seek(0)
    res1 = f.readlines()
    match = re.findall(r'[a-zA-Z]', res)
    print("Input file contains:")
    print(f"{len(match)} letters")
    print(f"{len(res.split())} words")
    print(f"{len(res1)} lines")



import random
with open("first_names.txt") as f, open("last_names.txt") as l:
    fir = f.readlines()
    las = l.readlines()
    for _ in range(3):
        print(random.choice(fir).strip() + " " + random.choice(las).strip())