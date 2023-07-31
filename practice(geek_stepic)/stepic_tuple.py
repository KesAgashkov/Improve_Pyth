# a = (1,)
# b = (2,)
# print(id(a))
# a+=b
# print(a)
#
# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples = [el for el in tuples if len(el) != 0]
#
# # print(non_empty_tuples)
# #
# # tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# # new_tuples = [el[:-1] + (100,) for el in tuples]
# # print(new_tuples)
#
#
# p = [5,6,8,8]
# print(id(p))
# p.sort()
# print(id(p))
# p = sorted(p)
# print(id(p))
#
# tup = (1,6,9,4,3)
#
# new = sorted(tup)
# print(tuple(new))


# number = 12345
# tpl = tuple(str(number))
# print(tpl)
#
#
# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# tot = 1
# for el in numbers:
#     tot*=el
# print(tot)
#
#
#
# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# print(poet_data[:-1]+("Москва",))
#
#
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# res = [sum(el)/len(el) for el in numbers]
# print(res)
#
#
# koor = int(input()), int(input()), int(input())
# print((-koor[1]/(2*koor[0]), (4 * koor[0] * koor[2] - koor[1]*koor[1])/(4*koor[0])))



n =  int(input())
res = [tuple(input().split()) for _ in range(n)]
for el in res:
    print(*el)
print()
for el in res:
    if int(el[1]) > 3:
        print(*el)


# pup = [input() for _ in range(int(input()))]
# print(*pup, sep='\n')
# print()
# [print(x) for x in pup if int(x[-1]) > 3]


n = int(input())


def tribonacci(param):
    f1, f2, f3 = 1, 1, 1
    for i in range(param):
        f1, f2, f3 = f2, f3, f1 + f2 + f3
        yield f1

lst = []
f = tribonacci(n)
for i in range(n):
    lst.append(next(f))

lst.insert(0, 1)
print(*lst[:-1])