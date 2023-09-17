import math

x = math.pi / 3

a = 1

for i in range(9):
    a = (1 + 2 * (8 - i)) - (x ** 2 / a)
    print("Iteration ", i, ": ", a)
print("The tangent of pi/3 is", x / a)
print("The tangent of pi/3 is", math.tan(math.pi / 3))