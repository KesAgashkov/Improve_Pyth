# num = 0.1 + 0.1 + 0.1
# eps = 0.000000001           # точность сравнения
#
# if abs(num - 0.3) < eps:    # число num отличается от числа 0.3 менее чем 0.000000001
#     print('YES')
# else:
#     print('NO')
#
#
# from decimal import Decimal as D
# s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
# sp = [D(el) for el in s.split()]
# print(max(sp) + min(sp))
#
#
# from decimal import Decimal as D
# s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
# sp = [D(el) for el in s.split()]
# print(sum(sp))
# print(*sorted(sp, reverse = True)[:5])


#
# from decimal import *
# num = Decimal(input())
# res1 =  list(num.as_tuple().digits)
# res1.extend(list(map(int,(str(num).lstrip("-").split(".")[0]))))
# print(max(res1) + min(res1))
import math
# from decimal import *
# d = Decimal(input())
# print(d.exp() + d.ln()+ d.log10() + d.sqrt())


# from fractions import Fraction
#
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
# [print(Fraction(el)) for el in numbers]
#
#
#
# from fractions import Fraction
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
# [print(f'{el} = {Fraction(el)}') for el in numbers]


# from fractions import Fraction
#
# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
# s = list(map(Fraction, s.split()))
# print( Fraction(min(s) + max(s)))
#
#
# from fractions import Fraction
# print(Fraction(int(input()), int(input())))
#
#
#
# from fractions import Fraction
# num1, num2 = input(), input()
# a,b = Fraction(num1), Fraction(num2)
# print(f'{num1} + {num2} = {a+b}',f'{num1} - {num2} = {a-b}', f'{num1} * {num2} = {a*b}', f'{num1} / {num2} = {a/b}', sep="\n")

# from fractions import Fraction
# import math
# res = 0
# n = int(input())
# for i in range(1,n+1):
#     res += Fraction(f'1/{math.factorial(i)}')
# print(res)
#
#
# from fractions import Fraction as F
# n = int(input())
# s, fctrl = F(0), 1
# for i in range(1, n+1):
#   fctrl *= i
#   s += F(1, fctrl)
# print(s)


# from fractions import Fraction
# import math
# n = int(input())
# up = n // 2
# low = n - up
#
# while math.gcd(up,low)!=1:
#     up-=1
#     low+=1
# print(Fraction(up,low))


from fractions import Fraction
import math
n = int(input())
lst = []
for i in range(1,n+1):
    for j in range(1,n+1):
        if math.gcd(i,j)==1 and i/j<1:
            lst.append(Fraction(i,j))

print(*sorted(lst), sep="\n")


a = complex(input())
b = complex(input())
print(f'{a} + {b} = {a+b}', f'{a} - {b} = {a-b}', f'{a} * {b} = {a*b}', sep="\n")



numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
max = -1
res = 0
for el in numbers:
    if abs(el)>max:
        max = abs(el)
        res =el
print(res, max, sep="\n")


numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
zmax = max(numbers, key = abs)
print(zmax)
print(abs(zmax))


n = int(input())
z1 = complex(input())
z2 = complex(input())
res = z1**n+ z2**n + z1.conjugate()**n + z2.conjugate()**(n+1)
print(res)