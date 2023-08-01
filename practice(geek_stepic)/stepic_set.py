# n, m, k, x, y, z = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
# print(n + m + k - x - y + z)
#
# n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(
#     input()), int(input())
# print(x + y - n - m - k + t + y + z - n - m - k + t + x + z - n - m - k + t)
# print(n + m - x - t + m + k - y - t + k + n - z - t)
# count1 = (k - (n + m - x - t) - (n + k - z - t) - t) + (n - (m + k - y - t) - (n + m - x - t) - t) + (
#             m - (m + k - y - t) - (n + k - z - t) - t)
# count2 = (n + m - x - t) + (m + k - y - t) + (n + k - z - t)
# print(a - (count1 + count2) - t)

# a= 25,
# s ={10}
# b = 30,
# s.add(a)
# print(s.isdisjoint(b))
# print(s)
# print(__name__)

numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
print(sum([el**2 for el in numbers]))


a = input()
print("YES" if len(set(a)) == len(list(a)) else "NO")


s = set(input() + input())
print("YES" if s == set("0123456789") else "NO")


print("YES" if set(input()) == set(input()) else "NO")


temp = input().split()
print("YES" if set(temp[0]) == set(temp[1]) == set(temp[2]) else "NO")


n = int(input())
res = [len(set(input().lower())) for _ in range(n)]
print(*res,sep="\n")


n = int(input())
s = set()
{s.update(list(input().lower())) for _ in range(n)}
print(len(s))



import re
words = re.sub(r'[.,;:-?-!]', '', input().lower()).split()
print(len(set(words)))


temp = set()
s = [int(el) for el in input().split()]
for el in s:
    if el in temp:
        print("YES")
    else:
        print("NO")
        temp.add(el)





