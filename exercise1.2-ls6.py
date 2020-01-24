from time import sleep


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    # Использую лист, топортный способ вызывать все по очереди и по идексам
    def running(self):
        print('-------------- \nПервый светофор\n')
        sleep(7)
        print(TrafficLight.__color[0])
        sleep(2)
        print(TrafficLight.__color[1])
        sleep(3)
        print(TrafficLight.__color[2])
        sleep(1)
        print('Светофор работает корректно\n')


t = TrafficLight()
t.running()
