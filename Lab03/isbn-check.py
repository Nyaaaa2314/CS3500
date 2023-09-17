isbn = str(input("Enter an ISBN number: "))
sum = 0
j = 10
for i in isbn:
    try:
        sum += int(i) * j
    except:
        sum += 10 * j
    finally:
        j -= 1
if sum % 11 == 0:
    print("ISBN number accepted.")
else:
    print("Invalid ISBN number.")