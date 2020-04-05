class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(self._income['wage']+self._income['bonus'])

a = Position("Вася", "Пупкин", "Слесарь", 25, 50)

a.get_full_name()
a.get_total_income()

b = Position("Леонид", "Михельсон", "Акционер", 80, 180)

b.get_full_name()
b.get_total_income()
