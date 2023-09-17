#alpha splits string into list of characters
global alpha
global cipher

alpha = [*"abcdefghijklmnopqrstuvwxyz"]
cipher = [*"defghijklmnopqrstuvwxyzabc"]

infile = open("ORWU - Wkh Ihoorzkls ri wkh Ulqj.txt", "r").read().split("\n")
out = list()
for line in infile:
    newline = list()
    for char in line:
        if char.lower() in alpha:
            if char.isupper():
                newline.append(alpha[cipher.index(char.lower())].upper())
            else:
                newline.append(alpha[cipher.index(char)])
        else:
            newline.append(char)
    out.append(newline)
outfile = open("LOTR - The Fellowship of the Ring.txt", "w")
for line in out:
    outfile.write("".join(line) + "\n")

