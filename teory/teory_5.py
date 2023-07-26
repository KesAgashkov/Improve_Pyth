# def new(a, b, c, *args, **kwargs):
#     print(a,b,c)
#     print(type(args))
#     print(args)
#     print(type(kwargs))
#     print(kwargs)
#
# new(15,10,40, k = 50)

#Распаковка и присваивание значений переменным
lst = [1,2,3,4,[5,6]]
# txt = "привет"
# d,*e = txt
# a,b,*c = lst
# print(a,b,c)
# print(*lst, sep="\t")
#
# f,d = (10,20),(30,40)
# print(f,d)
# p = o =None
# print(p,o)

it = iter(lst)
new ={34,56,76}
it2 = iter(new)
it3 = iter({"key":100}.values())
print(*it3)
print(it3)
gen = (i for i in lst)

print(*gen)
print(next(gen, "Астанавитесь!!!"))
# print(type(it2))
# print(type(it3))


# new_lst = [item for item in lst if type(item)!=list]
# print(new_lst)