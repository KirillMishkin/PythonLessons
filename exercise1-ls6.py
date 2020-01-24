# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу
# можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.
from time import sleep
from random import randrange
from random import sample


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']
    second = [7, 2, randrange(1, 4)]

    # обычный вариант решения
    def running_1(self):
        i = 0
        print('-------------- \nПервый светофор\n')
        while True:
            if i > 2:
                break
            sleep(TrafficLight.second[i])
            print(TrafficLight.__color[i])
            i += 1
        print('Светофор исправен\n')

    # усложненное уловие когда вызывается рандомный свет светофора и если нарушается последовательность , то ошибка
    def running_2(self):
        i = 0
        print('-------------- \nВторой Светофор\n')
        new_color = [el for el in TrafficLight.__color]
        while True:
            if i > 2:
                break
            if new_color[randrange(0, 3)] == TrafficLight.__color[i]:
                sleep(TrafficLight.second[i])
                print(TrafficLight.__color[i])
            else:
                sleep(1)
                print('-------------- \nПорядок нарушен! Светофор не исправен')
                break
            i += 1
        #
    def running_3(self):
        i = 0
        print('-------------- \nТретий светофор')
        new_color = []
        for x in sample(TrafficLight.__color, 3):
            new_color.append(x)
            if new_color[i] == TrafficLight.__color[i]:
                sleep(TrafficLight.second[i])
                print(TrafficLight.__color[i])
            else:
                sleep(1)
                print('Порядоак нарушен! Перезапустите светофор')
                break
            i += 1


t = TrafficLight()
t.running_1()
t.running_2()
t.running_3()
