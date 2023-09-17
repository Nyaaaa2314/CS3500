import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) 


x = math.pi / 4
a = x

for i in range(10):
    i += 1
    a += (-1) ** i * x ** (2 * i + 1) / factorial(2 * i + 1)
    print("Iteration ", i, ": ", a)
print("The sine of pi/4 is", a)
print("The sine of pi/4 is", math.sin(math.pi / 4))