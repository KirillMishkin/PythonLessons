# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10
# строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
# подсчет средней величины дохода сотрудников.
import json

my_file = open('txt_exercise3.txt', 'r')
x = mid = 0
for i in my_file:
    new_i = i.split()
    data = dict([(new_i[0], float(new_i[1]))])
    '''Вычисляем какие работнники получают меньше 20000 рублей'''
    for name, salary in data.items():
        if salary < 20000:
            print(name, salary)
    for salary in data.values():
        mid += 1
        x += salary
print(f'Средняя заработная плата всех сотрудников {round(x / mid, 2)}')
