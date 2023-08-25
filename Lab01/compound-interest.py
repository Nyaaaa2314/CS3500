P = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: ")) / 100
n = float(input("Enter the number of times interest is compounded in a year: "))
t = float(input("Enter the total number of years borrowed: "))


A = P * (1 + (r / n)) ** (n * t)
print("The total amount paid is %.2f" % A)