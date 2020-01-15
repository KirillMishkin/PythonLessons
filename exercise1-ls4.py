#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.


from sys import argv


def salary(*args):
    my_list = []
    for i in args:
        my_list.append(int(i))
    my_salary = my_list[0] * my_list[1] + my_list[2]
    print('My salary = ', my_salary)


params = argv
salary(params[1], params[2], params[3])
