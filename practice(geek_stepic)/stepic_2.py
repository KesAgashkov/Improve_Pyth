# n, m = map(int, input().split())
# res = [["." if (i+j)%2 == 0 else "*" for j in range(m)] for i in range(n)]
# for el in res:
#     print(*el,sep=" ")
#
# n = int(input())
# res = [[1 if (i + j) == n - 1 else 2 if (i + j) >= n else 0 for j in range(n)] for i in range(n)]
# for el in res:
#     print(*el, sep=" ")
#
#
# n, m = map(int, input().split())
# count = 1
# res = [[i * m + j + 1 for j in range(m)] for i in range(n)]
# for el in res:
#     for e in el:
#         print(str(e).ljust(3),end="")
#     print()
#
#
# n, m = map(int, input().split())
# count = 1
# res = [[j * n + i + 1 for j in range(m)] for i in range(n)]
# for el in res:
#     for e in el:
#         print(str(e).ljust(3),end="")
#     print()
#

# n = int(input())
# res = [[1 if (i <= j and i <= n - 1 - j) or (i >= j and i >= n - 1 - j) else 0 for j in range(n)] for i in range(n)]
# for el in res:
#     for e in el:
#         print(str(e).ljust(3), end="")
#     print()
#
#
# n, m = map(int, input().split())
# num = 1
# res = [[ 0 for j in range(m)] for i in range(n)]
# for i in range(n+m):
#     for j in range(n):
#         for k in range(m):
#             if (j+k) == i:
#                 res[j][k] = num
#                 num+=1
# for el in res:
#     for e in el:
#         print(str(e).ljust(3),end="")
#     print()
#
#
# n, m = map(int, input().split())
# a = [[0] * m for _ in range(n)]
#
# i, j, d = 0, 0, 0
# moves = ((0, 1,), (1, 0,), (0, -1,), (-1, 0,),)
# for k in range(1, n * m + 1):
#     a[i][j] = k
#     for l in range(4):
#         newD = (d + l) % 4
#         di, dj = moves[newD]
#         newI, newJ = i + di, j + dj
#         if 0 <= newI < n and 0 <= newJ < m and a[newI][newJ] == 0:
#             i, j, d = newI, newJ, newD
#             break
#
# for el in a:
#     for e in el:
#         print(str(e).ljust(3),end="")
#     print()


n1, m1 = map(int, input().split())
matr1 = [[int(i) for i in input().split()] for i in range(n1)]
input()
tot = 0
n2, m2 = map(int, input().split())
matr2 = [[int(i) for i in input().split()] for i in range(n2)]
res = []
temp = []
for i in range(n1):
    for k in range(n1):
        for p in range(n2):
            tot += matr1[i][p] * matr2[p][k]
        temp.append(tot)
        tot = 0
    res.append(temp)
    temp = []

for el in res:
    print(*el)



import copy
n = int(input())
init_matr = [[int(i) for i in input().split()] for i in range(n)]
poww = int(input())
res_matr = copy.deepcopy(init_matr)
temp = []
last = []
tot = 0
for f in range(poww-1):
    for i in range(n):
        for k in range(n):
            for p in range(n):
                tot += res_matr[i][p] * init_matr[p][k]
            temp.append(tot)
            tot = 0
        last.append(temp)
        temp = []
    res_matr = copy.deepcopy(last)
    last = []

for el in res_matr:
    print(*el)



