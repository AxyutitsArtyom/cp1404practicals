def main1():
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


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
             'bob']
if input("Enter your username: ") in usernames:
    print("Access granted")
else:
    print("Access denied")
