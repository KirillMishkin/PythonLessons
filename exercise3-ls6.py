# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    name = 'Антон'
    surname = 'Федоров'
    _position = 'Слесарь'
    _income = {'wage': 20000, 'bonus': 5000}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.surname} {self.name}, работает на позиции {self._position}')

    def get_total_income(self):
        salary = []
        for x in self._income.values():
            salary.append(x)
        print(sum(salary))


p = Position()
p.get_full_name()
p.get_total_income()
