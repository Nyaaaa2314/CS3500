import math 
import random

facex = 0
facey = 0
facer = 10

ear1x = -8
ear1y = 8
ear1r = 3

ear2x = 8
ear2y = 8
ear2r = 3

def inside(x, y):
	#face calc
	if math.sqrt((x - facex)**2 + (y - facey)**2) < facer:
		return True
	#ear1 calc
	elif math.sqrt((x - ear1x)**2 + (y - ear1y)**2) < ear1r:
		return True
	#ear2 calc
	elif math.sqrt((x - ear2x)**2 + (y - ear2y)**2) < ear2r:
		return True
	else:
		return False;

	

def area(n):
	c = 0
	for i in range (n):
		x = random.randrange(-13, 14)
		y = random.randrange(-10,15)
		if inside(x,y):
			c += 1
	return (c/n) * 26 * 24


def area100Trials(n):
	avg = 0
	for i in range (100):
		avg += area(n)
	return (avg/100)


print("n = 100: " + str(area100Trials(100)))
print("n = 1000: " + str(area100Trials(1000)))
print("n = 10000: " + str(area100Trials(10000)))
print("n = 100000: " + str(area100Trials(100000)))



