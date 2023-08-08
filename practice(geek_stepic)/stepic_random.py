import random
# random.seed(18)
# print(random.getstate())
#
# import random
#
# length = int(input())
# for _ in range(length):
#     a = random.randint(65,90)
#     b = random.randint(97,122)
#     print(chr(random.choice([a,b])), end="")
#
# # from random import *
# #
# # for _ in range(int(input())):
# #     print(chr(choice([randint(65, 90), randint(97, 122)])), end='')
#
#
# import random
# res = [random.randint(1,49)  for _ in range(7)]
# print(*sorted(res), sep=" ")
#
#
# import random as rnd
# print(*sorted(rnd.sample(range(1, 50), 7)))


# import string
#
# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.punctuation)
# print(string.printable)
#
#
# import string
# import random
# def generate_index():
#
#     return "".join(random.sample(string.ascii_uppercase,2)) + "".join(map(str,(random.sample(range(10),2)))) + "_"\
#         + "".join((map(str,(random.sample(range(10),2))))) + "".join(random.sample(string.ascii_uppercase,2))
# print(generate_index())
#
#
# from random import randint
# def generate_index():
#     return f'{chr(randint(65, 90)) * 2}{randint(0, 99)}_{randint(0, 99)}{chr(randint(65, 90)) * 2}'
#
#
#
# import random
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# def chuf(matrix):
#     random.shuffle(matrix)
#     return matrix
#
# chuf(matrix)
#
#
# from random import randint
# for _ in range(100):
#     print(randint(1000000,9_999_999))


# from random import sample
# print(*sample(range(10 ** 6, 10 ** 7), 100), sep='\n')
#
#
# import random
# word = input()
# print(*random.sample(word, len(word)), sep='')
#
#
#
# import random
# lst= list(range(1,76))
# for i in range(5):
#     for j in range(5):
#         el = random.choice(lst)
#         lst.remove(el)
#         if i == j == 2:
#             print(str(0).ljust(3), end=" ")
#         else:
#             print(str(el).ljust(3), end=" ")
#     print()
#

# import random
# fir = [input() for _ in range(int(input()))]
# sec = fir.copy()
# for el in fir:
#     ad=el
#     while el == ad:
#         ad = random.choice(sec)
#     print(f'{el} - {ad}')
#     sec.remove(ad)
#
# import random
#
#
#
# def generate_password(length):
#     num = {'2', '3', '4', '5', '6', '7', '8', '9'}
#     low = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
#            'y', 'z'}
#     upp = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
#            'Y', 'Z'}
#     n = l = u = length // 3
#     u = u + length % 3
#     res = random.sample(num, n) + random.sample(low, l) + random.sample(upp, u)
#     random.shuffle(res)
#     return "".join(res)
#
#
# def generate_passwords(count, length):
#     num = {'2', '3', '4', '5', '6', '7', '8', '9'}
#     low = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
#            'y', 'z'}
#     upp = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
#            'Y', 'Z'}
#     n = l = u = length // 3
#     u = u + length % 3
#     fin = []
#     for _ in range(count):
#         num = {'2', '3', '4', '5', '6', '7', '8', '9'}
#         res = random.sample(num, n) + random.sample(low, l) + random.sample(upp, u)
#         random.shuffle(res)
#         fin.append("".join(res))
#     return fin
#
#
# n, m = int(input()), int(input())

# print(*generate_passwords(n, m), sep='\n')


import random
n = 10 ** 6  # количество испытаний
k = 0
s0 = 16
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)

    if x ** 3 + y ** 4 + 2 >= 0 and 3 * x + y ** 2 <= 2:
        k += 1

print((k / n) * s0)



import random

n = 10 ** 6
k = 0
s0 = 4
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 <= 1:
        k += 1
print((k / n) * s0)