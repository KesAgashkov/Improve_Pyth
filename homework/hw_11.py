# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# Задание выполнено в модуле practice_11

# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

class Matrix:
    """Класс позволяет производить операции сравнения, сложения,
    умножения матриц с созданием нового экземпляра класса, а также просмотра созданных матрицы"""
    def __init__(self, matr):
        self.matr =  matr


    def look_matrix(self):
        matr =self.matr
        for el in matr:
            print(*el)
        print()

    def __eq__(self, other):
        return "Матрицы равны" if self.matr == other.matr else 'Матрицы не равны'

    def __add__(self, other):
        if len(self.matr) == len(other.matr):
            for i in range(len(self.matr)):
                if len(self.matr[i])!=len(other.matr[i]):
                    return print("Матрицы не соразмерны, сложение невозможно")

            new = [[0 for j in range(len(self.matr[i]))] for i in range(len(self.matr))]
            for i in range(len(other.matr)):
                for j in range(len(other.matr[i])):
                    new[i][j] = self.matr[i][j] + other.matr[i][j]
            return Matrix(new)

        else:
            return print("Матрицы не соразмерны, сложение невозможно")

    def __mul__(self, other):
        if len(self.matr[0]) == len(other.matr):

            res = []
            temp = []
            tot = 0
            for i in range(len(self.matr)):
                for k in range(len(other.matr[i])):
                    for p in range(len(other.matr[i])):
                        tot += self.matr[i][p] * other.matr[p][k]
                    temp.append(tot)
                    tot = 0
                res.append(temp)
                temp = []
            return Matrix(res)

        else:
            return print("Количество столбцов первой матрицы не равно количеству строк второй матрицы, умножение невозможно")


#
# new_matr1 = Matrix([[3, 8, 5], [4, 9, 1], [3, 4,15]])
# new_matr2 = Matrix([[3, 8, 3], [3, 4, 2],[8, 5, 1]])
#
# print(new_matr1 == new_matr2)
#
# new_matr1.look_matrix()
#
# new_matr2.look_matrix()
#
# new = new_matr1 + new_matr2
#
# new1 = new_matr1 * new_matr2
#
# new1.look_matrix()




