s = input()
found = False
suf = ""
for c in s:
    if found:
        suf += c
    else:
        if c == 'a':
            suf += c
            found = True
print(suf)