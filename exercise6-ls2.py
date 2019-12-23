# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (
# характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя. Пример готовой структуры:
# [ (
# 1, {“название”: “компьютер”,
# “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2,
# “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”}) ]


how_much_product = int(input('Введите количество всего  товара '))
step = 0
new_list = []
while True:
    step += 1
    if step > how_much_product:
        break
    name = input(f'Название товара {step}: ')
    price = input(f'Цена товара {step}: ')
    quantity = input(f'Количество в ШТ {step}: ')
    product = {"Название": name,
               "Цена": price,
               "Количество": quantity,
               "ед": 'шт.'}
    answer = (step, product)
    new_list.append(answer)
for i in new_list:
    print(i)