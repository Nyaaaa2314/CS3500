import math

def f(x, A):
    return x ** 2 - A

def f_prime(x):
    return 2 * x



A = int(input("Enter a number to find its square root: "))

cur = float(1)
pre = 0
i = 0
while abs(cur - pre) >= 1 * 10 ** -12:
    pre = cur
    cur = pre - f(pre, A) / f_prime(pre)
    print("Iteration ", i, ": ", cur)
    i += 1
print("The square root of", A, "is", cur)
print("The square root of", A, "is", math.sqrt(A))

