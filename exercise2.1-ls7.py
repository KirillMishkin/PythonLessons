# (V/6.5 +0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.

from abc import ABC, abstractmethod


class CoatMain(ABC):
    def __init__(self, value):
        self.value = value


    @abstractmethod
    def coat_method(self):
        solution = (self.value / 6.5) + 0.5
        print(solution)


class SuitMain(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def suit_method(self):
        solution = (2 * self.value) + 0.3
        print(solution)


class ClothesAll(CoatMain, SuitMain):
    @property
    def coat_method(self):
        print('Расходы на пальто', end=' = ')
        super().coat_method()

    @property
    def suit_method(self):
        print('Расходы на костюм', end=' = ')
        super().suit_method()


clothe = ClothesAll(40)
clothe.coat_method
clothe.suit_method

