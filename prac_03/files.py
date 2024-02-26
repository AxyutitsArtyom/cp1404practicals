with open("name.txt", "w") as in_file:
    in_file.write(input("Enter name: "))

with open("name.txt", "r") as in_file:
    print(f"Your name is {in_file.read()}")

with open("numbers.txt", "r") as in_file:
    print(int(in_file.readline()) + int(in_file.readline()))

with open("numbers.txt", "r") as in_file:
    total = 0
    for i in in_file.readlines():
        total += float(i)
    print(total)
