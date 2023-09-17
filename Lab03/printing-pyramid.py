n = int(input("How many rows to print: "))

for i in range(n):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1 + i * 2):
        print("*", end="")
    print()