# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.


def user_date():
    result = [name, surname, date_of_birth, city, email, telephone]
    print(' '.join(result))


print('Введите данные пользователя ')
name = input('Name: ')
surname = input('Surname: ')
date_of_birth = input('Date of birth: ')
city = input('City: ')
email = input('Email: ')
telephone = input('Telephone: ')

user_date()
