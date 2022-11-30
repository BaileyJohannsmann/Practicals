"""
CP1404 - Practical 9
taxi simulator
This was quite time consuming and as a result i didnt complete fully
"""
from Practicals.prac_09.taxi import Taxi
from Practicals.prac_09.silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():

    total_trip_cost = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            chosen_taxi = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[chosen_taxi]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi:
               "I DONT KNOW HOW TO DO THIS PART"


    print("Taxis are now:")






main()
