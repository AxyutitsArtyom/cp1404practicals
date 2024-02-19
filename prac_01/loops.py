for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

count = 1
for i in range(int(input("How many stars do you want?: "))):
    print("*" * count)
    count += 1
print()
