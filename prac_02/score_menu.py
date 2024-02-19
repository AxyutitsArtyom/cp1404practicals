VALID_LOW_SCORE_THRESHOLD = 0
VALID_HIGH_SCORE_THRESHOLD = 100
EXCELLENT_SCORE_THRESHOLD = 90
BAD_SCORE_THRESHOLD = 50
VALID_CHOICES = "gpsq"
VALID_HIGH_THRESHOLD = 100
VALID_LOW_THRESHOLD = 0
DEFAULT_SCORE = 0
MENU = """(G)et a valid score 
(P)rint result 
(S)how stars 
(Q)uit"""


def main():
    score = DEFAULT_SCORE
    print(MENU)
    choice = get_valid_choice()

    while choice != "q":
        if choice == "g":
            score = get_valid_score()

        elif choice == "p":
            print(determine_score(score))

        elif choice == "s":
            print_asterisks(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = get_valid_choice()
    print("Farewell")


def get_valid_choice():
    choice = input(">>> ").lower()
    while choice not in VALID_CHOICES:
        print("Invalid choice")
        choice = input(">>> ")
    return choice


def get_valid_score():
    score = int(input("Enter score: "))
    while score < VALID_LOW_THRESHOLD or score > VALID_HIGH_THRESHOLD:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def print_asterisks(length):
    print("*" * length)


def determine_score(score):
    if score < VALID_LOW_SCORE_THRESHOLD or score > VALID_HIGH_SCORE_THRESHOLD:
        return "Invalid score"
    elif score >= EXCELLENT_SCORE_THRESHOLD:
        return "Excellent"
    elif score >= BAD_SCORE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()
