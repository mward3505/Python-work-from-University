class Tire:
    def __init__(self):
        self.size = 12


class Car:
    def __init__(self):
        self.tire = Tire()


car = Car()
print(car.tire.size)
