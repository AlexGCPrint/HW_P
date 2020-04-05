class Car():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} Едет!")

    def stop(self):
        print(f"{self.name} Остановилась!")

    def direction(self, direction):
        print(f"{self.name} повернула {direction} ")

    def show_speed(self):
        print(f"Текущая скорость {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости 60 км/ч")
        print(f"Текущая скорость {self.speed} км/ч")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости 40 км/ч")
        print(f"Текущая скорость {self.speed} км/ч")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


lada = TownCar(90, "красная","lada")

lada.go()
lada.show_speed()

ferrari = SportCar(180, "желтая", "ferrari")

ferrari.go()
ferrari.show_speed()
ferrari.direction("направо")

ford = PoliceCar(70, "белый", "ford", True)

ford.go()
ford.direction("налево")
ford.stop()
print(ford.is_police)