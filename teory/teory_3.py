# # a, b, c, *_ = input().split()
# # print(f"{a: ^25}")
# tup = (5,6)
# tup1 = (1,)
# print(type(tup1))
#
# my_set = {1,1,2,3,4,5} #принимает только неизменяемые типы данных
# print(my_set)
#
# print(my_set)
# my_set.remove(5)
# print(my_set)
# my_set.discard(100) #нет ошибки при удалении несущ элемента
# more_set = {4,45,202,1}
# new_set = more_set & my_set
# new2_set =  my_set.intersection(more_set)
# new_set.add(frozenset({444,555})) #можем добавить и фрозен сет
# print(new_set)
#
# union_set = my_set | more_set
# union2_set = my_set.union(more_set)
# print(union_set)
# print(union2_set)
#
# diff_set =my_set - more_set
# diff2_set =  my_set.difference(more_set)
# print(diff_set)
# print(diff2_set)
#
# text =  "Привет"
# text = text.encode("utf-8")
# print(text,type(text).mro(), sep="\n")
#
#
