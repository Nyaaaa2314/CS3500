months = int(input("Enter total months: "))
ppairs = 0
mpairs = 0
bpairs = 1
for i in range(months):
    ppairs = ppairs + mpairs
    mpairs = bpairs
    bpairs = ppairs

print("There will be %d pairs of rabbits." % (ppairs + mpairs + bpairs))