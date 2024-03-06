def main():
    numbers = []
    print("Enter 5 numbers")
    for i in range(5):
        numbers.append(int(input("Number: ")))
    print_list_info(numbers)


def print_list_info(numbers):
    """Display information about list"""
    print(f"The first number is {numbers[0]}\n"
          f"The last number is {numbers[-1]}\n"
          f"The smallest number {min(numbers)}\n"
          f"The largest number {max(numbers)}\n"
          f"The average of the numbers is {sum(numbers) / len(numbers): .1f}")


main()
