"""
CP1404 - Practical 9
silver service taxi test
"""
from silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi("Toyota", 100, 2)
my_taxi.drive(18)
print(my_taxi)
print(my_taxi.get_fare())