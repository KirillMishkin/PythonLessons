# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

# list

mes_number = int(input('Введите номер месяца '))
mes_list = ['Зима', 'Весна', 'Лето', 'Осень']

if mes_number < 3 or mes_number == 12:
    print(mes_list[0])
elif 3 <= mes_number < 6:
    print(mes_list[1])
elif 6 <= mes_number < 9:
    print(mes_list[2])
elif 9 <= mes_number < 12:
    print([3])
else:
    print('Нет такого месяца')

# dic

month_number = int(input('Month number: '))
month_dic = {1: 'Winter',
             2: 'Winter',
             3: 'Spring',
             4: 'Spring',
             5: 'Spring',
             6: 'Summer',
             7: 'Summer',
             8: 'Summer',
             9: 'Autumn',
             10: 'Autumn',
             11: 'Autumn',
             12: 'Winter'}
answer = month_dic.get(month_number)
if answer is None:
    print('Нет такого месяца')
else:
    print(answer)

# dic 2

answer_wen = []
mess = int(input('Введите месяц '))
mess_dic = {'Winter': [12, 1, 2],
            'Spring': [3, 4, 5],
            'Summer': [6, 7, 8],
            'Autumn': [9, 10, 11]}
for k, v in mess_dic.items():
    if mess in v:
        answer_wen.append(k)
print(''.join(answer_wen))
