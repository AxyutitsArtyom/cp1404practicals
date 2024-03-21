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
            guitars.append(Guitar(name, year, cost))
            print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")
        while name != "":
            year = get_valid_year()
            cost = get_valid_cost()
            guitars.append(Guitar(name, year, cost))
            print(f"{name} ({year}) : ${cost} added.")
            name = input("Name: ")

    with open("guitars.csv", "w") as in_file:
        for guitar in guitars:
            in_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    print("These are my guitars:")
    print_guitars(guitars)


def print_guitars(guitars):
    """Display sorted collection of guitars"""
    guitars.sort(key=lambda x: x.year)
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


def get_valid_cost():
    """Get valid guitar's cost"""
    while True:
        try:
            cost = float(input("Cost: $"))
            break
        except ValueError:
            print("Invalid cost")
            pass
    return cost


def get_valid_year():
    """Get valid guitar's year"""
    while True:
        try:
            year = float(input("Year: "))
            break
        except ValueError:
            print("Invalid year")
            pass
    return year


main()
