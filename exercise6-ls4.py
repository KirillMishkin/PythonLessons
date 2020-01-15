# Реализовать два небольших скрипта: а) итератор, генерирующий целые числа, начиная с указанного, б) итератор,
# повторяющий элементы некоторого списка, определенного заранее. Подсказка: использовать функцию count() и cycle()
# модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть
# условие его завершения.


from itertools import count
from itertools import cycle

i = 0
for i in count(4):
    if i > 25:
        break
    print(i)


my_list = [1, 2, 3, 4, 5, 6]
new_list = []
c = 0
for x in cycle(my_list):
    if c > 20:
        break
    new_list.append(x)
    c += 1
print(new_list)