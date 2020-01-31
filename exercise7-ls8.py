# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, number_1):
        self.number_1 = number_1
        self.number_complex = 0

    def __add__(self, other):
        self.number_complex = self.number_1 + other.number_1
        return self.number_complex

    def __mul__(self, other):
        self.number_complex = self.number_1*other.number_1
        return self.number_complex

    def __str__(self):
        return f'\nКомплексное число {self.number_complex}\nДействительная часть {int(self.number_complex.real)}\n' \
               f'Мнимая часть ' \
               f'{int(self.number_complex.imag)}\nСопряженное комплексное число {self.number_complex.conjugate()}'


number1 = input('''Ввести  первое  комплексное число формата x+yj(без пробелов), 
где j мнимая единица и всегда указывается этой буквой\n''')
number2 = input('''Ввести  второе  комплексное число формата x+yj(без пробелов), 
где j мнимая единица и всегда указывается этой буквой\n''')

x = complex(number1)
y = complex(number2)

c_n_1 = ComplexNumber(x)
c_n_2 = ComplexNumber(y)

c_n_1 + c_n_2
print(c_n_1)

c_n_1 * c_n_2
print(c_n_1)

