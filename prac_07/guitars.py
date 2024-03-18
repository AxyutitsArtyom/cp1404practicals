"""
Estimated time: 15 min
Actual time: 19 min
"""

from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []

    with open("guitars.csv", "r") as in_file:
        for line in in_file:
            parts = line.split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name,year,cost))
            print(f"{name} ({year}) : ${cost} added.")

    print("These are my guitars:")
    print_guitars(guitars)


def print_guitars(guitars):
    """Display sorted collection of guitars"""
    guitars.sort(key=lambda x: x.year)
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()
