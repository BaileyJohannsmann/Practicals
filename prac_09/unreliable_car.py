"""
CP1404 - Practical 9
unreliable car class
"""
from random import randint
from Practicals.prac_09.car import Car


class UnreliableCar(Car):
    """Subclass of Car"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
