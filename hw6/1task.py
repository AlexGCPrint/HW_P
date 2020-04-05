from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый', 'Желтый']

    def running(self):
        i = 0
        while True:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
                i += 1
            elif i == 1:
                sleep(2)
                i += 1
            elif i == 2:
                sleep(7)
                i += 1
            elif i == 3:
                sleep(1)
                i = 0



t = TrafficLight()
t.running()