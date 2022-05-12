from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):

        super().__init__(name, fuel)
        self.name = name
        self.fuel = fuel
        self.reliability = reliability

    def __str__(self):
        super(UnreliableCar, self).__str__()
        return "{}, fuel = {}, reliability = {}".format(self.name, self.fuel, self.reliability)

    def drive(self, distance):
        random_number = random.randint(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0
