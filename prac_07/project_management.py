"""
Estimated: 30 min
Actual: 100 min
"""
from prac_07.project import Project

VALID_CHOICES = "LSDFAUQ"
MENU = "- (L)oad projects\n" \
       "- (S)ave projects\n" \
       "- (D)isplay projects\n" \
       "- (F)ilter projects by date\n" \
       "- (A)dd new project\n" \
       "- (U)pdate project\n" \
       "- (Q)uit"


def main():
    projects = []
    with open("projects.txt", "r") as in_file:
        next(in_file)
        for line in in_file:
            line = line.strip("\n").split("	")
            name = line[0]
            start_date = line[1]
            priority = int(line[2])
            cost_estimate = float(line[3])
            completion_percentage = int(line[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from projects.txt")
        print(MENU)

        choice = get_valid_choice()

        while choice != "Q":
            if choice == "D":
                print("Incomplete projects: ")
                for i in projects:
                    if i.completion_percentage != 100:
                        print("  " + str(i))

                print("Complete projects: ")
                for i in projects:
                    if i.completion_percentage == 100:
                        print("  " + str(i))

            elif choice == "U":
                for i, project in enumerate(projects, 0):
                    print(f"{i} " + str(project))

                while True:
                    try:
                        project_choice = int(input("Project choice: "))
                        print(projects[project_choice])
                        break
                    except ValueError:
                        print("Invalid project number")
                    except IndexError:
                        print("Invalid project number")
                while True:
                    try:
                        percentage = int(input("Percent complete: "))
                        if 0 < percentage < 100:
                            break
                        else:
                            print("Number must be > 0 and < 100")
                    except ValueError:
                        print("Invalid input")
                projects[project_choice].completion_percentage = percentage

            elif choice == "A":
                print("Let's add a new project")
                name = input("Name: ")
                start_date = input("Start date (dd/mm/yy): ")
                while True:
                    try:
                        priority = int(input("Priority: "))
                        if 0 < priority:
                            break
                        else:
                            print("Number must be > 0")
                    except ValueError:
                        print("Invalid input")

                while True:
                    try:
                        cost_estimate = int(input("Cost estimate: $"))
                        if 0 < cost_estimate:
                            break
                        else:
                            print("Number must be > 0")
                    except ValueError:
                        print("Invalid input")
                while True:
                    try:
                        percentage = int(input("Percent complete: "))
                        if 0 < percentage < 100:
                            break
                        else:
                            print("Number must be > 0 and < 100")
                    except ValueError:
                        print("Invalid input")
                projects.append(Project(name, start_date, priority, cost_estimate, percentage))

            elif choice == "F":
                filter_date = input("Show projects that start after date (dd/mm/yy): ")
            print(MENU)
            choice = get_valid_choice()


def get_valid_choice():
    choice = input(">>> ").upper()
    while choice not in VALID_CHOICES:
        print("Invalid choice")
        choice = input(">>> ")
    return choice.upper()


main()
