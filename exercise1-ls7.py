# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы. Примеры матриц: 3 на 2, 3 на 3, 2 на 4. Следующий шаг —
# реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода
# __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна
# быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
from random import randrange


class Matrix:
    def __init__(self, value1, result):
        self.value1 = value1
        self.new_matrix = result

    def __str__(self):
        print("Сумма двух матриц")
        return f'\n'.join('\t'.join(str(j) for j in i) for i in self.new_matrix)

    # создаем новую матрицу которая соствляем сумму двух матриц
    def __add__(self, other):
        for i in range(len(self.value1)):
            for j in range(len(self.value1[0])):
                self.new_matrix[i][j] = self.value1[i][j] + other.value1[i][j]
        return self.new_matrix


# Создаем матрицу х_1 на у_1
x_1 = 5
y_1 = 5

# Матрица 1
value_1 = [[randrange(1, 10) for n in range(x_1)] for m in range(y_1)]
print('\n'.join('\t'.join(str(a_1) for a_1 in a) for a in value_1))
print()

#  Матрица 2
value_2 = [[randrange(1, 10) for n_1 in range(x_1)] for m_1 in range(y_1)]
print('\n'.join('\t'.join(str(b_1) for b_1 in b) for b in value_2))
print()

# сюда мы вписываем ответы. Нулевая матрица
result_1 = [[0 for n_2 in range(x_1)] for m_2 in range(y_1)]

my_matrix_1 = Matrix(value_1, result_1)
my_matrix_2 = Matrix(value_2, result_1)
my_matrix_1 + my_matrix_2
print(my_matrix_1)
