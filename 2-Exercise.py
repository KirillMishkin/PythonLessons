# -*- coding: utf-8 -*-
# . Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


second = int(input('Введите количествоа секунд '))
minutes = (second // 60) % 60
hours = (second // 3600) % 24
second2 = second % 60
print(str(hours).rjust(2, '0'), str(minutes).rjust(2, '0'), str(second2).rjust(2, '0'), sep=':')
