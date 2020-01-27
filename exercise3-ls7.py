# еализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
# конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
# реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (
# __mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно
# осуществляться округление значения до целого числа.

# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме
# ячеек исходных двух клеток.

# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества
# ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
# количества ячеек этих двух клеток.

# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток.


# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
# метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
# то в последний ряд записываются все оставшиеся. Например, количество ячеек клетки равняется 12, количество ячеек в
# ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**. Или, количество ячеек клетки равняется 15,
# количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:
    def __init__(self, my_cell_1):
        self.my_cell_1 = len(my_cell_1)
        self.new_cell = []

    def __add__(self, other):  # сложение
        self.new_cell = ['*'] * (self.my_cell_1 + other.my_cell_1)
        return self.new_cell

    def __sub__(self, other):  # вычитание
        if self.my_cell_1 - other.my_cell_1 > 0:
            my_sum = self.my_cell_1 - other.my_cell_1
            self.new_cell = ['*'] * my_sum
            return self.new_cell

        elif other.my_cell_1 - self.my_cell_1 >= 0:
            my_sum = other.my_cell_1 - self.my_cell_1
            self.new_cell = ['*'] * my_sum
            return self.new_cell

        elif (self.my_cell_1 - other.my_cell_1) == 0:
            self.new_cell = ['*'] * 0
            return self.new_cell

        elif other.my_cell_1 - self.my_cell_1 == 0:
            self.new_cell = ['*'] * 0
            return self.new_cell

        else:
            return 'Не верные данные для вычитания'

    def __mul__(self, other):  # умножение
        self.new_cell = ['*'] * (self.my_cell_1 * other.my_cell_1)
        return self.new_cell

    def __truediv__(self, other):  # деление
        if self.my_cell_1 // other.my_cell_1 > 1:
            self.new_cell = ['*'] * (self.my_cell_1 // other.my_cell_1)
        elif other.my_cell_1 // self.my_cell_1 > 1:
            self.new_cell = ['*'] * (other.my_cell_1 // self.my_cell_1)
        else:
            'Не верный данный для деления'

    def __str__(self):
        return f'\n{self.make_order()}'

    def make_order(self):
        i = 5
        if i > len(self.new_cell):
            return ''.join(self.new_cell)
        else:
            while True:
                if i > len(self.new_cell):
                    break
                self.new_cell.insert(i, '\n')
                i += 6
            return ''.join(self.new_cell)


'''Первая клетка'''
x_cell_1 = 7
cell_1 = ['*' for m in range(x_cell_1)]

'''Вторая клетка'''
x_cell_2 = 2
cell_2 = ['*' for n in range(x_cell_2)]

all_cell = len(cell_2) + len(cell_1)
print(f'Первая клетка: {len(cell_1)} ячеек\nВторая клетка: {len(cell_2)} ячеек')

print('Всего ячеек в двух клетках:', all_cell)


c_1 = Cell(cell_1)
c_2 = Cell(cell_2)

c_1 - c_2
print('\nВычитание клеток', c_1)
c_1 + c_2
print('\nСложение клеток', c_1)
c_1 * c_2
print('\nУмножение клеток', c_1)
c_1 / c_2
print('\nДеление клеток', c_1)
