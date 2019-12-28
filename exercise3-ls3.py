# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.


def my_func(num1, num2, num3):
    return max(num1, num2, num3)


print('Введиете три числа: ')
a = int(input('Number1 = '))
b = int(input('Number2 = '))
c = int(input('Number3 = '))

out = my_func(a, b, c)
print(out)

