# lst = input().split()
# n = int(input())
# res = []
# temp = []
# for i in range(n):
#     for j in range(len(lst)):
#         if j % n == i:
#             temp.append(lst[j])
#     res.append(temp)
#     temp = []
#
# print(res)
#
#
# n = int(input())
# matr = [[int(j) for j in input().split()] for i in range(n)]
# new = [matr[i][j] for j in range(n) for i in range(n) if (i<=j and i>=n-1-j) or (i>=j and i>=n-1-j)]
# print(max(new))
#
#
# n = int(input())
# matr = [[int(j) for j in input().split()] for i in range(n)]
# for el in [[matr[j][i] for j in range(n)] for i in range(n)]:
#     print(*el)
#
#
# n = int(input())
# matr = [["." for j in range(n)] for i in range(n)]
#
# new = [["*" if i==n-1-j or i==j or i==n//2 or j==n//2 else "."  for j in range(n)] for i in range(n)]
# for el in new:
#     print(*el,sep=" ")
#
#
#
# point = list(input())
# x = 8 - int(point[1])
# y = ["a","b","c","d","e","f","g","h"].index(point[0])
# board = [["." for j in range(8)] for i in range(8)]
#
# moves = [["*" if abs(x - i) == abs(y - j) or x == i or y == j else  "." for j in range(8)] for i in range(8)]
# moves[x][y] = "Q"
# for el in moves:
#     print(*el)
#
#
#
# n = int(input())
# matr = [[int(el) for el in input().split()] for i in range(n)]
# matr.reverse()
# print("YES" if [[matr[j][i] for j in range(n)] for i in range(n)] == matr else "NO")
#
#
#
#
# n = int(input())
# flag = True
# check = [i for i in range(1, n + 1)]
# matr = [[int(el) for el in input().split()] for i in range(n)]
# for row in matr:
#     if sorted(row) != check:
#         flag = False
#         break
#
# for row in [[matr[j][i] for j in range(n)] for i in range(n)]:
#     if sorted(row) != check:
#         flag = False
#         break
#
# print("YES" if flag else "NO")
#



n = int(input())
board = [[0 for j in range(n)] for i in range(n)]
for f in range(n):
    for i in range(n):
        for j in range(n):
            if f == i - j or f == j - i:
                board[i][j] = f

for el in board:
    print(*el)



