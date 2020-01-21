# 4. Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
#
# Two — 2
#
# Three — 3
#
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
my_file = open('txt_exercise4_start.txt', 'r')
new_file_txt = open('txt_exercise4.txt', 'w')
my_list = []
for i in my_file:
    content = i.split('-')
    if 'One' in content:
        index = content.index('One')
        del content[index]
        content.insert(index, 'Один')
    elif 'Two' in content:
        index = content.index('Two')
        del content[index]
        content.insert(index, 'Два')
    elif 'Three' in content:
        index = content.index('Three')
        del content[index]
        content.insert(index, 'Три')
    elif 'Four' in content:
        index = content.index('Four')
        del content[index]
        content.insert(index, 'Четыре')
    new_file_txt.write('-'.join(content))
my_file.close()
new_file_txt.close()
