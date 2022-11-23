"""
CP1404 - Practical 7
my_guitars
"""

from Practicals.prac_06.guitar import Guitar


def main():

    guitars = []

    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            # Strip newline, split it into parts
            parts = line.strip().split(',')
            # Create a Guitar object
            # year should be an int, cost should be a float
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)

        name = input("Name: ")
        while name != "":
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            print(f"{name} ({year}) : ${cost:,.2f} added.")
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
            name = input("Name: ")

            guitars.sort()
            with open('guitars.csv', 'w') as out_file:
                for guitar in guitars:
                    print(guitar)
                    print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
