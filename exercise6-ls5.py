# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.


"""Написана функиця которая убират все буквы и символы и отавляет только цифры"""


def new_list(numbers):
    my_list = []
    for i in numbers:
        try:
            my_list.append(int(i))
        except ValueError:
            continue
    return ''.join(str(el) for el in my_list)  # создает str переменную которую потом переводим в int


my_file = open('txt_exercise6', 'r')
my_dict = {}
for content in my_file:
    z = content.split()  # перебираем строки отдельно создавая из каждой строки list
    print(z)
    final_list = []
    for content1 in z[1:]:  # начинаем перебирать с идекса 1 пропуская название предмета
        final_list.append(int(new_list(content1)))
    my_dict[z[0]] = sum(final_list)
print('\n', my_dict)
my_file.close()