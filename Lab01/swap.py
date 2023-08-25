x = int(input("Enter the first integer, x: "))
y = int(input("Enter the second integer, y: "))
print ("Before Swapping")
print ("The value of x is", x)
print ("The value of y is", y)

x = x + y
y = x - y 
x = x - y

print ("After Swapping")
print ("The value of x is", x)
print ("The value of y is", y)