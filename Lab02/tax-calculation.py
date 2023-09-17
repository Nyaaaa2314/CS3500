print("This program computes taxes for the year 2018 for singles.")
income = float(input("Enter taxable income: "))
tax = 0
if income >= 9700:
    tax = tax + 970
else:
    tax = income * 0.1
if income >= 39475:
    tax = tax + (39475 - 9701) * 0.12
else:
    if income - 9701 < 0:
        print("Total tax owed: %0.2f" % tax)
        exit()
    tax = tax + (income - 9701) * 0.12
if income >= 84200:
    tax = tax + (84200 - 39476) * 0.22
else:
    if income - 39476 < 0:
        print("Total tax owed: %0.2f" % tax)
        exit()
    tax = tax + (income - 39476) * 0.22
if income >= 160725:
    tax = tax + (160725 - 84201) * 0.24
else:
    if income - 84201 < 0:
        print("Total tax owed: %0.2f" % tax)
        exit()
    tax = tax + (income - 84201) * 0.24
if income >= 204100:
    tax = tax + (204100 - 160726) * 0.32
else:
    if income - 160726 < 0:
        print("Total tax owed: %0.2f" % tax)
        exit()
    tax = tax + (income - 160726) * 0.32
if income >= 510300:
    tax = tax + (510300 - 204101) * 0.35
else:
    if income - 204101 < 0:
        print("Total tax owed: %0.2f" % tax)
        exit()
    tax = tax + (income - 204101) * 0.35
if income >= 510301:
    if income - 510301 < 0:
        print("Total tax owed: %0.2f" % tax)
        exit()
    tax = tax + (income - 510301) * 0.37
print("Total tax owed: %0.2f" % tax)

# Rate Taxable Income Bracket
# 10% $0 to $9,700
# 12% $9,701 to $39,475
# 22% $39,476 to $84,200
# 24% $84,201 to $160,725
# 32% $160,726 to $204,100
# 35% $204,101 to $510,300
# 37% $510,300+

