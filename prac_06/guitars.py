"""
Estimated time: 15 min
Actual time: 19 min
"""

from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    name = input("Name: ")
    while name != "":
        while True:
            try:
                year = float(input("Year: "))
                break
            except ValueError:
                print("Invalid year")
                pass

        while True:
            try:
                cost = float(input("Cost: $"))
                break
            except ValueError:
                print("Invalid cost")
                pass
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()
