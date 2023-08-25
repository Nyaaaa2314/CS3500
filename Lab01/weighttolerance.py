w = float(input("Enter desired weight: "))
n = float(input("Enter tolerance (as percentage): "))
print("The range of accepted weight for the part is from ", w - (w * (n / 100)), " to ", w + (w * (n / 100)))