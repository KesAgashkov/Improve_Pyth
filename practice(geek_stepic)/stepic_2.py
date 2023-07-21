# chars = list(input())
# res = []
# app = []
# for i in range(len(chars) - 1):
#     if chars[i] == chars[i + 1]:
#         app.append(chars[i])
#     else:
#         res.append(app)
#         app.clear()
#
# prim = input().split()
# pre = []
# res = []
# res.append([])
# for i in range(1, len(prim) - 1):
#     for j in range(0, len(prim)):
#         pre.append(prim)
#
#     else:
#         res.append(prim)
#         pre = []
#
#
#
# res.append(prim)
# print(res)
#
# prim = input().split()
# pre = []
# res = []
# res.append([])
# for i in range(len(prim)):
#     for j in range(len(prim)):
#         pre = prim[j:i + j + 1]
#         if len(pre) == i + 1:
#             res.append(pre)
#
# print(res)
# n = int(input())
# m = int(input())
# for i in range(n):
#     for j in range(m):
#         print(input(), end = " ")
#     print()

# n = int(input())
# m = int(input())
#
# lst = [[input() for i in range(m)] for i in range(n)]
#
# [print(*i) for i in lst]



# n = int(input())
# m = int(input())
#
# lst = [[input() for i in range(m)] for i in range(n)]
#
# [print(*i) for i in lst]
# print()
# for i in range(m):
#     for j in range(n):
#         print(lst[j][i], end=" ")
#     print()

# summ = 0
# for i in range(int(input())):
#     summ += list(map(int,input().split()))[i]
# print(summ)

# print()
# for i in range(m):
#     for j in range(n):
#         print(lst[j][i], end=" ")
#     print()

# n = int(input())
# temp = []
# count = 0
# for i in range(n):
#     lst = list(map(int, input().split()))
#     aver = sum(lst) / n
#     for el in lst:
#         if el>aver:
#             count+=1
#     print(count)
#     count=0



# matrix = [list(map(int,input().split())) for i in range(int(input()))]
# res = []
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         if i>=j:
#             res.append(matrix[i][j])
#
# print(max(res))



# n = int(input())
# matrix = [list(map(int,input().split())) for i in range(n)]
# res = []
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         if i>=j and i<=n-1-j:
#             res.append(matrix[i][j])
#         elif i<=j and i>=n-1-j:
#             res.append(matrix[i][j])
#
# print(max(res))

# n = int(input())
# matrix = [list(map(int,input().split())) for i in range(n)]
#
# print(matrix)
#
#
#
#
# n = int(input())
# matrix = [list(map(int, input().split())) for i in range(n)]
# top, bot, left, right = 0, 0, 0, 0
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         if i < j and i < n - 1 - j:
#             top += matrix[i][j]
#         elif i < j and i > n - 1 - j:
#             right += matrix[i][j]
#         elif i > j and i < n - 1 - j:
#             left += matrix[i][j]
#         elif i > j and i > n - 1 - j:
#             bot += matrix[i][j]
#
# print(f"Верхняя четверть: {top}")
# print(f"Правая четверть: {right}")
# print(f"Нижняя четверть: {bot}")
# print(f"Левая четверть: {left}")


data = {"Вася": ("Палатка", "Котелок", "Спички", "Шашлык", "Топор", "Мазик"),
        "Петя": ("Палатка", "Котелок", "Топор"),
        "Костя": ("Веревка", "Мыло", ),
        "Саша": ("Палатка", "Котелок", "Топор", "Спирт", "Масло"),
        }
lst = []
for k, v in data.items():
    lst.append(set(v))

temp_1 = lst[0]
res_all = set()
for i in range(1, len(lst)):
    temp_1 = temp_1.intersection(lst[i])

print(temp_1)