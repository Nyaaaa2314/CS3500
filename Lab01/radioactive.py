import math
e = 2.7183
k = 3.9 * 10 ** -12
t = 0
ini = float(input("Enter the initial amount of Carbon-14 in the artifact (in grams): "))
cur = float(input("Enter the current amount of Carbon-14 in the artifact (in grams): "))
t = ((-1 * math.log(cur / ini)) / k) / 3153600
print("The age of the artifact is %.2f" % t)