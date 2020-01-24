# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.
from time import sleep

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw_method(self):
        sleep(1)
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    pass


class Pencil(Stationery):
    pass


class Handle(Stationery):
    pass


go_pen = Pen('Pen(ручка)')
go_pen.draw_method()

go_pencil = Pencil('Pencil(карандаш)')
go_pencil.draw_method()

go_handle = Handle('Handle(маркер)')
go_handle.draw_method()
