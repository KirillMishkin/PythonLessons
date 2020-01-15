# еализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
from functools import reduce


def sum_range(x, y):
    return x * y


my_range = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(sum_range, my_range))

# проверка ответа
print(sum(my_range))
