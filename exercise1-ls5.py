# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.

my_file = open('exercise2.txt', 'w')
while True:
    new_string = input('введите данные для записи\n')
    my_file.write(new_string + '\n')
    if new_string == '':
        my_file.close()
        break
my_file = open('exercise2.txt', 'r')
for line in my_file:
    print(line)
my_file.close()
