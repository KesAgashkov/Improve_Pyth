# n, m = map(int, input().split())
# res = [["." if (i+j)%2 == 0 else "*" for j in range(m)] for i in range(n)]
# for el in res:
#     print(*el,sep=" ")
#
n = int(input())
res = [[1 if (i + j) == n - 1 else 2 if (i + j) >= n else 0 for j in range(n)] for i in range(n)]
for el in res:
    print(*el, sep=" ")


n, m = map(int, input().split())
count = 1
res = [[i * m + j + 1 for j in range(m)] for i in range(n)]
for el in res:
    for e in el:
        print(str(e).ljust(3),end="")
    print()


n, m = map(int, input().split())
count = 1
res = [[j * n + i + 1 for j in range(m)] for i in range(n)]
for el in res:
    for e in el:
        print(str(e).ljust(3),end="")
    print()


n = int(input())
res = [[1 if (i <= j and i <= n - 1 - j) or (i >= j and i >= n - 1 - j) else 0 for j in range(n)] for i in range(n)]
for el in res:
    for e in el:
        print(str(e).ljust(3), end="")
    print()


n, m = map(int, input().split())
num = 1
res = [[ 0 for j in range(m)] for i in range(n)]
for i in range(n+m):
    for j in range(n):
        for k in range(m):
            if (j+k) == i:
                res[j][k] = num
                num+=1
for el in res:
    for e in el:
        print(str(e).ljust(3),end="")
    print()
    

n, m = map(int, input().split())
a = [[0] * m for _ in range(n)]

i, j, d = 0, 0, 0
moves = ((0, 1,), (1, 0,), (0, -1,), (-1, 0,),)
for k in range(1, n * m + 1):
    a[i][j] = k
    for l in range(4):
        newD = (d + l) % 4
        di, dj = moves[newD]
        newI, newJ = i + di, j + dj
        if 0 <= newI < n and 0 <= newJ < m and a[newI][newJ] == 0:
            i, j, d = newI, newJ, newD
            break

for el in a:
    for e in el:
        print(str(e).ljust(3),end="")
    print()
