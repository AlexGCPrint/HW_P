class Road:

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
        self.weight = 25

    def asphalt(self, thicknes):
        print(self._lenght * self._width * self.weight * thicknes)


t = Road(20, 5000)

t.asphalt(25)
