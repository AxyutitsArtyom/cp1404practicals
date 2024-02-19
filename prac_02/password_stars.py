minimum_length = 8

password = input("Enter your password: ")
while len(password) < minimum_length:
    print("Too short")
    password = input("Enter your password: ")

print("*"*len(password))
