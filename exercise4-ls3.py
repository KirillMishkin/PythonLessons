# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.


def my_func(x, y):  # возведение в степерь с использваонием двойного символа **
    if x > 0 and y < 0:
        print(float((x ** y)))
    elif x <= 0:
        print('число X меньше или равно 0')
    else:
        print('Число Y больше или равно  0')


def my_func1(a, b):  # Использование цикла для возведение в степень (возведение в отрицательную степень)
    value = 1
    while True:
        b += 1
        if b > 0:
            break
        value *= a
    print(1 / value)


x1 = int(input('x = '))
y1 = int(input('y = '))
my_func(x1, y1)
my_func1(x1, y1)
