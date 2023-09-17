fruits = open("fruits.txt", "r").read().split("\n")
i = 0
for s in fruits:
    if s == "avocado":
        i += 1
print("The number of avocados is", i)