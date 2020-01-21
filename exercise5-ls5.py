# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.


my_file = open('sum_number_exercise5', 'w')
numbers = (input('Введиче числа через пробел \n'))

my_file.write(numbers)
my_file.close()
my_file = open('sum_number_exercise5', 'r')
content = my_file.read().split()
my_sum = []
for i in content:
    my_sum.append(int(i))
print(sum(my_sum))
