"""
CP1404 - Practical 5
wimbledon
a program to read csv file, process the data and display processed information
"""

CSV_FILE = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data file and print details about Wimbledon champions and countries."""
    records = get_stats(CSV_FILE)
    champion_count, countries = process_stats(records)
    display_stats(champion_count, countries)


def process_stats(records):
    """Create dictionary of champions and set of countries from records (list of lists)."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries


def display_stats(champion_count, countries):
    """Display champions and countries"""
    print("Wimbledon Champions: ")
    for name, count in champion_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def get_stats(filename):
    """Get champion_wins from file in list of lists form."""
    champion_wins = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove header
        for line in in_file:
            parts = line.strip().split(",")
            champion_wins.append(parts)
    return champion_wins


main()
