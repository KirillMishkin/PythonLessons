from time import sleep
from random import randrange


class TrafficLight:
    __color_1 = {1: 'Red', 2: 'Yellow', 3: 'Green'}

    # Способ со словарем и так же с нарушением порядка выполнения
    def running_1(self):
        print('-------------- \nПервый светофор\n')
        for number, color in TrafficLight.__color_1.items():
            if number == randrange(1, 4):
                sleep(7)
                print(color)
            elif number == randrange(1, 4):
                sleep(2)
                print(color)
            elif number == randrange(1, 4):
                sleep(3)
                print(color)
            else:
                sleep(1)
                print('Светофор работате не корректно\n')
                break


t = TrafficLight()
t.running_1()
