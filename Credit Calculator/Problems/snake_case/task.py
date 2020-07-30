word = input()
for i in range(len(word)):

    if str.isupper(word[i]) is True and str.islower(word[i - 1]) is True:
        word = word[0:i] + '_' + word[i:len(word)]

print(word.lower())
