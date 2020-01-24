# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
from itertools import cycle
from time import sleep
from random import sample
from random import randrange


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.show_speed()
        self.go_method()
        self.turn_method()
        self.stop_method()

    def show_speed(self):
        if not self.is_police:
            print(f'Максимальная скорость {self.name} =  {self.speed}')
        else:
            print(f'Максимальная скорость полицейской машины {self.name} = {self.speed}')

    def go_method(self):
        print('Машина поехала\n')

    def stop_method(self):
        sleep(1)
        print('Машина остановилась\n')

    def turn_method(self):
        turn = ['Налево', 'Направо', 'Едет прямо', 'Едет прямо', 'Едет прямо', 'Едет прямо']
        new_turn = []
        speed = randrange(1, 10)  # начальная скорость движения
        i = 0
        for x in cycle(sample(turn, 3)):
            new_turn.append(x)
            sleep(2)
            if 'Едет прямо' in new_turn[i]:
                speed += randrange(5, 20, 2)
            print(new_turn[i])
            print(f'Speed: {speed}')
            if speed > self.speed:
                print(f'Скорость больше {self.speed}')
                break
            i += 1


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCare(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


tc = TownCar(60, 'White', 'LADA', False)

wc = WorkCar(40, 'Red', 'BobCat', False)

pc = PoliceCare(100, 'Blue', 'Ford', True)

