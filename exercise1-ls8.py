# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.


class Date:

    @staticmethod
    def first_method_date():
        date_list = [int(el) for el in my_date.split('-')]  # создаем список с int значениями
        if 1 <= date_list[0] <= 31 and 1 <= date_list[1] <= 12 and 1 <= date_list[2] <= 2021:
            for new_date in date_list:
                print(new_date, end=' ')
            print()
        else:
            print('Данные не корректные')

    @classmethod
    def second_method_date(cls, param):
        for x in param.split('-'):
            print(int(x), end=' ')


my_date = '10-05-1992'
Date.first_method_date()
Date.second_method_date(my_date)
