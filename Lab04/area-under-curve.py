
def f(x):
	return x ** 2 + x + 1

print ("Computing the area under the curve x^2 + x + 1.")
a = int(input("Enter the left end point a: "))
b = int(input("Enter the right end point b: "))
c = float(a)
dx = float(1)
for i in range(0,6):
	c = a
	dx /= 10
	area = 0
	while c <= b:
		c += dx
		area += f(c) * dx
		
		#print("c =", c, "area =", area, "dx =", dx)
	print ("Area under the curve from ", a, " to ", b," using ", dx, " is ", area)


