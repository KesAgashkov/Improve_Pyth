# n = int(input())
# fir = 0
# sec = 0
# thir = 0
# four = 0
# for i in range(n):
#     x, y = map(int, input().split())
#     if x > 0 and y > 0:
#         fir += 1
#     elif x < 0 and y > 0:
#         sec += 1
#     elif x < 0 and y < 0:
#         thir += 1
#     elif x > 0 and y < 0:
#         four += 1
#
# print(f"Первая четверть: {fir}")
# print(f"Вторая четверть: {sec}")
# print(f"Третья четверть: {thir}")
# print(f"Четвертая четверть: {four}")



# nums = list(map(int, input().split()))
# count = 0
# for i in range(len(nums)-1):
#     if nums[i]<nums[i+1]:
#         count+=1
# print(count)

# nums = list(map(int, input().split()))
#
# for i in range(0,len(nums)-1,2):
#     nums[i],nums[i+1]= nums[i+1],nums[i]
#
# print(*nums)

# nums = list(map(int, input().split()))
# nums.insert(0, nums[-1])
# print(nums[:-1])

# nums = list(map(int, input().split()))
# new = []
# for el in nums:
#     if el not in new:
#         new.append(el)
#
# print(len(new))


# nums = [int(input()) for _ in range(int(input()))]
# total = int(input())
# i = 0
# flag = False
# for fir in nums:
#     if flag==True:break
#     for i in range (nums.index(fir)+1, len(nums)):
#         if fir*nums[i] == total:
#             flag=True
#             break
# print("ДА" if flag else "НЕТ")

# fir = input()
# sec = input()
# if fir == "Камень" and sec == "Ножницы":
#     print("Тимур")
# elif fir == "Ножницы" and sec == "Камень":
#     print("Руслан")
# elif fir == "Бумага" and sec == "Камень":
#     print("Тимур")
# elif fir == "Камень" and sec == "Бумага":
#     print("Руслан")
# elif fir == "Ножницы" and sec == "Бумага":
#     print("Тимур")
# elif fir == "Бумага>" and sec == "Ножницы":
#     print("Руслан")
# else:
#     print("ничья")
#

# fir = input()
# sec = input()
# res = fir + sec
# if res in ['каменьножницы', 'ножницыбумага', 'бумагакамень', 'Споккамень', 'ножницыящерица', 'ящерицабумага',
#            'ящерицаСпок', 'каменьящерица']:
#     print("Тимур")
# elif fir == sec:
#     print("ничья")
# else:
#     print("Руслан")

# text = input()
# count = 1
# li = []
# if text.find("Р") == -1:
#     li.append(0)
# else:
#     for i in range(len(text) - 1):
#         if text[i] == "Р" and text[i] == text[i + 1]:
#             count += 1
#         else:
#             if count > 1:
#                 li.append(count)
#                 count = 1
#     else:
#         li.append(count)
#
# print(max(li))

# козырный вариант
# print(len(max(input().split("О"))))



# spis = []
# code = ""
# flag = False
# p = 0;
# example = "anton"
# for i in range(1, int(input()) + 1):
#     sample = input()
#     flag = False
#     code = ''
#     j = 0
#     p = 0
#     for ex in example:
#         if flag:
#             break
#         for j in range(p, len(sample)):
#             if ex == sample[j]:
#                 code += sample[j]
#                 p = j
#                 break
#         else:
#             flag = True
#
#         if example == code:
#             spis.append(i)
#             break
#
# print(*spis)


# alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
#             'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# text = input() + " запретил букву "
# for i in range(len(alphabet)):
#     if text.find(alphabet[i]) != -1:
#         text = text + alphabet[i]
#         text = text.lstrip(" ").replace("  ", " ")
#         print(text)
#         text = text.replace(alphabet[i], "")

# a = None
# print(type(a).mro())
# def test():
#     print("dsdsd")
# b = [10,5,12]
# print(id(b))
# #Три способо копирования списка с созданием нового обьекта
# c = list(b)
# print(id(c))
# c = b[:]
# print(id(c))
# c = b.copy()
# print(id(c))
# print(id(c))
#
#
# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']
# list1[2][1][2].extend(sub_list)
#
# print(list1)
#
# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for el in list1:
#     if max(el)>maximum: maximum = max(el)
#
# print(maximum)
#
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# for i in range(len(list1)):
#     list1[i].reverse()
#
# print(list1)
#
#
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for el in list1:
#     total+=sum(el)
#     counter+=len(el)
# print(total/counter)


#Выпрямить списочек
# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
# sum(my_list, [])
# >>>[1, 9, 8, 7, 4, 7, 3, 4, 2, 1]
# sum(sum(my_list, []))
# >>>46

# n = int(input())
#
# my_list = [[i for i in range(1,n+1)] for i in range(n)]
#
# print(sum(my_list,[]))
# for el in my_list:
#     print(el)
#
# n = int(input())
# i = 1
# my_list = []
# for _ in range(n):
#     my_list.append([i for i in range(1,i+1)])
#     i+=1
#
# for el in my_list:
#     print(el)
n = 10
lit = []
for i in range(n):
    lit.append([i for i in range(1, i + 1)])
print(lit)


def next_row(row):
    row = [1] + row
    for i in range(1, len(row)-1):
        row[i] += row[i+1]
    return row

row = []
res = []

n = int(input())
for i in range(n+1):
    row = next_row(row)
    res.append(row)


print(res[-1]) if n!=0 else print([1])


