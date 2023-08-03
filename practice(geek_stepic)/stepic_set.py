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

# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
# print(sum([el**2 for el in numbers]))
#
#
# a = input()
# print("YES" if len(set(a)) == len(list(a)) else "NO")
#
#
# s = set(input() + input())
# print("YES" if s == set("0123456789") else "NO")
#
#
# print("YES" if set(input()) == set(input()) else "NO")
#
#
# temp = input().split()
# print("YES" if set(temp[0]) == set(temp[1]) == set(temp[2]) else "NO")
#
#
# n = int(input())
# res = [len(set(input().lower())) for _ in range(n)]
# print(*res,sep="\n")
#
#
# n = int(input())
# s = set()
# {s.update(list(input().lower())) for _ in range(n)}
# print(len(s))
#
#
#
# import re
# words = re.sub(r'[.,;:-?-!]', '', input().lower()).split()
# print(len(set(words)))
#
#
# temp = set()
# s = [int(el) for el in input().split()]
# for el in s:
#     if el in temp:
#         print("YES")
#     else:
#         print("NO")
#         temp.add(el)


# s_1 = set(map(int,input().split(" ")))
# s_2 = set(map(int,input().split(" ")))
# res = s_1.intersection(s_2)
# print(*sorted(res))
#
#
# s_1 = set(map(int,input().split(" ")))
# s_2 = set(map(int,input().split(" ")))
# res = s_1.difference(s_2)
# print(*sorted(res))


# n = int(input()) - 1
# res = set(map(int, input()))
# for i in range(n):
#     temp = set(map(int, input()))
#     res.intersection_update(temp)
# print(*sorted(res))
#
#
# s1 = set(input())
# s2 = set(input())
# print("NO" if s1.isdisjoint(s2) else "YES")
#
#
# s1 = set(input())
# s2 = set(input())
# print("YES" if s2.issubset(s1) else "NO")
#
#
#
# p1 = set(map(int,input().split(" ")))
# p2 = set(map(int,input().split(" ")))
# p3 = set(map(int,input().split(" ")))
# res = p1.intersection(p2)
# res = res - p3
# print(*sorted(res)[::-1])
#
#
# p1 = set(map(int,input().split(" ")))
# p2 = set(map(int,input().split(" ")))
# p3 = set(map(int,input().split(" ")))
# res1 = p1 | p2 | p3
# res2 = res1 - p1.intersection(p2,p3)
# print(*sorted(res2))
#
#
# p1 = set(map(int,input().split(" ")))
# p2 = set(map(int,input().split(" ")))
# p3 = set(map(int,input().split(" ")))
# print(*sorted(p3 - (p1|p2))[::-1])
#
#
# p1 = set(map(int,input().split(" ")))
# p2 = set(map(int,input().split(" ")))
# p3 = set(map(int,input().split(" ")))
# whole = set(range(0,11))
# print (*sorted(whole - (p1|p2|p3)))
#
#
# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# myset = {int(el) for el in items}
# print(*sorted(myset))
#
#
# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
# myset = {el[0].lower() for el in words}
# print(*sorted(myset))



sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
sentence = sentence.lower()
myset = {el.strip('.,;:-?!()') for el in sentence.split()}
print(*sorted(myset))


sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
sentence = sentence.lower()
myset = {el.strip('.,;:-?!()') for el in sentence.split() if len(el.strip('.,;:-?!()'))<4 }
print(*sorted(myset))



files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']

myset = {el.lower() for el in files if el.lower().endswith(".png")}
print(*sorted(myset))


n = int(input())
test = []
for _ in range(n+1):
    town = input()
    if town not in test:
        test.append(town)
    else:
        print("REPEAT")
        break
else:
    print("OK")


n =  int(input())
m = int(input())
book_rus = {input() for _ in range(n)}
for _ in range(m):
    if input() in book_rus:
        print("YES")
    else:
        print("NO")


s_1 = set(map(int, input().split()))
s_2 = set(map(int, input().split()))
res = s_1 & s_2
print(*sorted(res,reverse=True) if res else ("BAD DAY",))


s_1 = set(map(int, input().split()))
s_ans = set(map(int, input().split()))
print("YES"if s_1 == s_ans else "NO")



m =  int(input())
n =  int(input())
mathematics_pupil = {input() for _ in range(m)}
informatics_pupil = {input() for _ in range(n)}
res = mathematics_pupil ^ informatics_pupil
print(len(res) if res else "NO")


s_1 = set(input().split())
s_2 = set(input().split())
res = s_1 | s_2
print(*sorted(res) )


m =  int(input())
res = {input() for _ in range(int(input()))}
for i in range(m-1):
    s = {input() for _ in range(int(input()))}
    res = res.intersection(s)

print(*sorted(res),sep="\n")