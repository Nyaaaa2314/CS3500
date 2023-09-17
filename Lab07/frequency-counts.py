f = open("LOTR-words", "r")
letters = {}
words = {}
for word in f:
    word = word.strip("\n")
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
    for letter in word:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
for word in words:
    print(word + " " + str(words[word]))
for letter in letters:
    print(letter + " " + str(letters[letter]))