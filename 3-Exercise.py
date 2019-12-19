# -*- coding: utf-8 -*-
# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

number = input('Введите число ')
result = int(number) + int(str(number) * 2) + int(str(number) * 3)
print(result)
