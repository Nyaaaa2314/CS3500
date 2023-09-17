
f = open("weather-data.txt", "r")
xs = list()
ys = list()
xbase = 1929
for line in f:
	inp = line.split()
	xs.append(float(inp[0]) - xbase)
	ys.append(float(inp[1]))
xavg = sum(xs) / len(xs)
yavg = sum(ys) / len(ys)
mnum = 0
for i in range(len(xs)):
	mnum += (xs[i] - xavg) * (ys[i] - yavg)
mdom = 0
for i in range(len(xs)):
	mdom += (xs[i] - xavg) ** 2
m = mnum / mdom
c = yavg - m * xavg
print ("The slope is " + str(m))
print ("The y-intercept is " + str(c))

# Code to plot the graph

f = open("weather-data.txt", "r")
x = list()
y = list()
xlabels = list()

for line in f:
	inp = line.split()
	x.append(float(inp[0]) - xbase)
	y.append(float(inp[1]))
	xlabels.append(int(inp[0]))
f.close()

import matplotlib.pyplot as plt
plt.plot(x, y, 'bo')
line = [m * x[i] + c for i in range(len(x))]
plt.plot(x, line, 'r')

plt.xlabel("Year")
plt.ylabel("Temperature")
plt.show()
