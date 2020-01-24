# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.
from time import sleep


class Stationery:
    def __init__(self, title):
        self.title = title
        self.draw_method()

    def draw_method(self):
        sleep(1)
        print('Запуск отрисовки', self.title)


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)


go_pen = Pen('Pen')

go_pencil = Pencil('Pencil')

go_handle = Handle('Handle')
